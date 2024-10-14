from pulp import PULP_CBC_CMD, LpMaximize, LpProblem, LpVariable, lpSum, value

# define problem
lp = LpProblem("Bakery_Problem", LpMaximize)

# define a dictionary of variables keyed by "indicies"
var_keys = [1, 2]
x = LpVariable.dicts("Bakery_item", var_keys, lowBound=0, cat="Integer")

# add objective func
lp += 10 * x[1] + 5 * x[2]

# add constraints
# inefficient way to create constraints
# lp += (5 * x[1] + x[2] <= 900, "oven_constraint")
lp += lpSum([5 * x[1], x[2]]) <= 90
lp += (x[1] + 10 * x[2] <= 300, "food_processor_constraint")
lp += (4 * x[1] + 6 * x[2] <= 125, "boiler_constraint")

# rewrite first constraint
coeff = [5, 1]  # may come from file i.e., csv
coeff_dict = dict(zip(var_keys, coeff))
lp += lpSum(coeff_dict[i] * x[i] for i in var_keys) <= 90

# solve the LP and don't show the log for the solver PULP_CBC_CMD
status = lp.solve(PULP_CBC_CMD(msg=False))
print("Status:", status)  # 1:optimal, 2: not solved, 3:infeasible, 4:unbounded

for var in lp.variables():
    print(var, "=", value(var))
print("OPT =", value(lp.objective))
