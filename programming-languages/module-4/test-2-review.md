# Chapter 16 overview
- proposition is a logical statement that may or may not be true.
    - it consists of objects and relationships among objects
- `a cat is a mammal` -> has a logical value (true) and therefore is a proposition
- `read this sentence` -> does not have a logical value (true or false) and is not a proposition
- The objects in logic programming are represented by `simple terms`
- **simple term** - a constant which is a symbol that represents a specific object
    - a variable which is a symbol that can represent different objects at different times (different than variables in imperataive languages)
- symbolic logic can be used to:
    1. express propositions
    2. express relationships between propositions
    3. describe how new propositions can be inferred from other propositions
- **atomic propositions** consist of compound terms
- **compound terms** is composed of two parts
    1. **Functor** a function symbol that names the relationship
    2. **tuple** an ordered list of parameters
- Examples of **compound terms**
    1. `student(jon)` student is the functor, jon is the list of parameters
    2. `like(seth, dos)` like is functor, set, dos is parameters
- Each of those is also an atomic proposition
-  two modes of propositions
    - one in which the proposition is defined to be true => *FACT*
    - one in which the truth of the proposition is to be determined => *a query*
- A compound proposition consists of two or more atomic propositions that are connected by operators
- variables can appear in propositions but only when introduced by special symbols called *quantifiers*
- standard form for propositions is to eliminate ambiguity => **clausal form**
- operators allowed are **conjunction**, **disjunction**, and **implies**
- Characteristics for clausal form
    - existential quantifiers are not required
    - universal quantifiers are implicit in the use of variables in atomic propositions
    - no operators other than conjunction and disjunction are allowed and implication
    - conjunction and disjunction need appear only in the order shown in general clausal form: disjunction on left side and conjunction on right side
- Example of clausal form
- *likes(bob, trout) <- likes(bob,fish), fish(trout)`
- this reads IF bob likes fish and trout is a fish then bob likes trout
- **resolution** is an inference rule that allows inferred propositions to be computed from given propositions
- **unification** process of determining useful values for variables that allow matching process to proceed
- **instantiation** is temporary assigning of values to variables to allow unification
- a critically important property of resolution is its ability to detect any inconsistency in a given set of propositions
- given a set of inconsistent propositions resolution can prove them to be inconsistent which is *proof by contradiction*
- original propositions are **hypotheses** and negation of theorem is **goal**
- When propositions used for resolution, only restricted form can be used
    - **Horn clause** which can have only two forms
        1. **headed** with a single atomic proposition on left side
        2. **headless** with an empty left side (used to state facts)
    - Example
    1. `sister(mary, pete)` headless horn clause
    2. `eagle(fly) <- eagle(bird), bird(fly)` headed horn clause
- Logic programming are non-procedural
- programs do NOT state how the result is to be computed but rather the form of the result
- declarative languages - programs consist of declarations (propositions)
- declarative semantics - simple way to determine the meaning of each statement, and it does not depend on how statement is used in program
- **Term** a constant, variable, structure
- **constant** an atom or an integer
- atom consists of either
    - string of letters, digits, and underscores beginning with lowercase letter
    - string of printable ASCII characters delimited by apostrophes
- **Variable** any string of letters, digits, and underscores beginning with Uppercase letter
- **Instantiation** binding of a variable to a value; lasts only as long as it takes to stasify one complete goal
- **structure** represents atomic proposition `functor(parameter list)`
- **Statements** only 3 types
    1. Facts
    2. Rules
    3. Goals
### Fact statements
- facts are propositions that are assumed to be true
- used for hypotheses
- **Headless horn clauses**
- Examples (every prolog statement is terminated by a period)
    - `female(mary).`
    - `male(jake).`
    - `father(bill, jake).`
### Rule Statements
- used for hypotheses
- headed horn clauses (because they state rules of implications between propositions
- right side is antecedent (if part) (may be a single term or conjunction
- left side: consequent (then part) must be a single term
- conjunction: multiple terms separated by logical AND operations (denoted with a comma)
- Examples
    ```prolog
        grandmother(mary, nancy) :- mother(mary, paul), father(paul, nancy).
        grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
    ```
### Goal statements
- a *goal* or *query* is a proposition that should be proved or disproved by the system
- same format as **headless horn clause**
- goal: `man(fred)`
- possible responses: 
    - yes => system has proven the goal was true under given database of facts and rules
    - no => either the goal was determined to be false, or the system was simply unable to prove it
- Conjunctive propositions and propositions with variables are also legal **goals**
    - `father(X, mike).` the system will try, through unification to find an instantiation of X that results in a true value for the **goal**
### 16.6 Basic elements of prolog
- when a goal is a compound proposition each of the facts (structures) it is a **subgoal**
- process of proving a subgoal is called **matching**, **satisfying**, or **resolution**
- Two opposite approaches to attempting to match a given goal to a fact in database
    - **Bottom-up resolution** or **forward chaining**. 
        - system begins with facts and rules of the database and attempts to find a sequence of matches that lead to the goal
        - **Top-down resolution** or **backward chaining** system begins with the goal and attempts to find a sequence of matching propositions that lead to some set of original facts
- Prolog implementations use **backward chaining** for resolution
- when a goal has more than one subgoal, possible strategies are:
    - **depth-first search** find a complete proof for teh first subgaol before working on others
    - **breadth-first search** work on all subgoals in parallel
- Prolog uses **depth-first search** (can be done with fewer computer resources)
- when a goal with multiple subgoals is being processed and system fails to show truth of subgoal, it abandons subgoal it can't prove
- It then reconsiders previous subgoal, if there is one, and attempts to find an alternative solution (backtracking)
- multiple solutions to a subgaol may result from different instantiations to variables
- can take lots of time and space because may find all possible proofs to every subgoal
