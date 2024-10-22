import pandas as pd
from pulp import PULP_CBC_CMD, LpMinimize, LpProblem, LpStatus, LpVariable, lpSum, value


def calculate_minimum_cost() -> None:
    r"""Calculate a set of proposed articles such that sum of costs is absolute minimum

    Returns
    -------
    None
    """
    # file name
    file_name: str = "tnn_data_1200_clicks.csv"
    # read the file
    data = pd.read_csv(file_name)
    # read minimum number of clicks constraint from filename
    minimum_clicks_constraint: str = file_name.split("_")[2]
    # define our problem - we are doing minimization
    problem = LpProblem("Articles_Problem", LpMinimize)
    # dynamically generate some reused helpers
    articles_index_list: list[int] = [i for i in range(0, len(data["Article"]))]
    # set of reporters because we want only unique values
    reporters_set: set[int] = set(data["Reporter"])
    # set of the types of articles.
    # G -> Global news
    # E -> Entertainment
    # S -> Science news
    # L -> Local news
    article_type_set: set[str] = set(data["Type"])
    # decision variable represents which article is chosen
    selected_article = LpVariable.dicts(
        "Article",
        indices=articles_index_list,
        lowBound=0,
        upBound=1,
        cat="Binary",
    )

    # aux variable to track total bonus articles i.e, >= 1 selected for a reporter
    reporters_bonus_articles = LpVariable.dicts(
        "Bonus articles of reporter", indices=reporters_set, lowBound=0, cat="Integer"
    )

    # aux variable to keep track of bonus types of articles selected
    types_bonus_articles = LpVariable.dicts(
        "Bonus articles of type",
        indices=article_type_set,
        lowBound=0,
        cat="Binary",
    )

    # build our objective function which is to minimize the cost of selected articles
    # while staying within constrains define below
    # add in the cost of bonus articles (more than 1 to a reporter)
    # subtract cost of bonus types of articles (if an article of a certain type is chosen 2 or more times)
    problem += (
        lpSum(
            [row["Cost"] * selected_article[rownum] for rownum, row in data.iterrows()]
        )
        + sum([100 * reporters_bonus_articles[i] for i in reporters_set])
        - sum([115 * types_bonus_articles[i] for i in article_type_set]),
        "Total cost of articles",
    )

    for reporter in reporters_set:
        # Constraint 1: Choose at least one article suggested each reporter
        problem += (
            lpSum(
                [
                    selected_article[rownum]
                    for rownum, row in data.iterrows()
                    if row["Reporter"] == reporter
                ]
            )
            >= 1,
            f"Include at least 1 article suggested by reporter {reporter}",
        )
        # sum all the articles selected for a specific reporter i.e, reporter {0,1,2}
        total_articles_for_reporter: int = sum(
            [
                selected_article[rownum]
                for rownum, row in data.iterrows()
                if row["Reporter"] == reporter
            ]
        )
        # Constraint 5: if more than 1 article to a reporter must pay additional
        # also reflected in objective function
        problem += (
            reporters_bonus_articles[reporter] >= total_articles_for_reporter - 1,
            f"Amount of bonus articles must be > than normal articles for reporter {reporter}",
        )
        # bonus can't be negative
        problem += (
            reporters_bonus_articles[reporter] >= 0,
            f"Bonus articles for reporter {reporter} must be positive",
        )
    # Constraint 2: Must have at least minimum_clicks which is parsed from file name
    problem += (
        lpSum(
            [
                row["Clicks"] * selected_article[rownum]
                for rownum, row in data.iterrows()
            ]
        )
        >= int(minimum_clicks_constraint),
        "Minimum clicks constraint",
    )

    # since we are looping over the article_type for constraint 3, 4, and 6 utilize the same outer loop (type)
    # for constraint 4 we need to know total selected articles. Sum up selected articles
    total_selected_articles: int = sum(
        [selected_article[i] for i in articles_index_list]
    )
    # outer loop is the type of article
    for article_type in article_type_set:
        # Constraint 3: At least one article of each type (G, E, S, L)
        problem += (
            lpSum(
                [
                    selected_article[rownum]
                    for rownum, row in data.iterrows()
                    if row["Type"] == article_type
                ]
            )
            >= 1,
            f"At least 1 article of type {article_type} constraint",
        )
        # Constraint 4: No article type (G, L, S, E) can have more than half the articles
        problem += (
            lpSum(
                [
                    selected_article[rownum]
                    for rownum, row in data.iterrows()
                    if row["Type"] == article_type
                ]
            )
            <= 0.5 * total_selected_articles,
            f"Article type {article_type} cannot have more than half {total_selected_articles}",
        )
        # Constraint 6: For each article type > 1 selected
        # similar to bonus reporters need to make sure bonus is > than selected articles of type
        # also reflected in objective function
        # collect total amount of articles selected by their type
        total_selected_articles_of_type = sum(
            [
                selected_article[rownum]
                for rownum, row in data.iterrows()
                if row["Type"] == article_type
            ]
        )
        problem += (
            types_bonus_articles[article_type] <= total_selected_articles_of_type / 2,
            f"Two or more articles of type {article_type}",
        )
        # Bonus articles can't go over 1 as this variable is binary but if
        # there are enough bonus articles i.e., 4 / 2 = 2 so constrain it
        problem += (
            types_bonus_articles[article_type] <= 1,
            f"Article of type {article_type} must be binary",
        )

    # solve the problem and supress additional console output of the solver
    status = problem.solve(PULP_CBC_CMD(msg=False))
    print("Status: ", LpStatus[status])
    print(problem)

    # print solution
    for var in problem.variables():
        if value(var) == 1:
            print(var, "=", value(var))
    print("Optimal value: ", value(problem.objective))


if __name__ == "__main__":
    calculate_minimum_cost()
