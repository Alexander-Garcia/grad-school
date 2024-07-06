# Chapter 16
## Logic Programming Languages
- Logic programming / declarative languages use logical inferencing to produce results
- Often a collection of **facts** and **rules**
- **proposition** logical statement that may or may not be true
- **symbolic logic** 3 basic needs of formal logic:
    1. express propositions
    2. express relationship between propositions
    3. describe how new propositions can be inferred from other propositions that are assumed to be true
- **first-order predicate calculus** form of symbolic logic used for logic programming
- **compound terms** one element of a mathematical relation
- A compound term is composed of two parts:
    1. **functor** the function symbol that names the relation, and an ordered list of parameters, which together represent an element of a relation
- Example of two propositions
    ```
    man(jake)
    like(bob, steak)
    ```
- {jake} is a 1-tuple in the relation named `man`
- {bob, steak} is a 2-tuple in the relation named `like`
- Variables can appear in propositions but only when introduced by special symbols called **quantifiers**
- The right side of a clausal form proposition is called **antecedent**
- The left side is **consequent** because it is the consequence of the truth of the antecedent
- **Resolution** an inference rule that allows inferred propositions to be computed from given propositions
- **unification** process of determining useful values for variables
- **instantiation** temporary assigning of values to variables to allow unification
- **refutation complete** critically important property of resolution is its ability to detect any inconsistency in a given set of propositions
- The original propositions are called **hypotheses** and negation of the theorem is **goal**
- The time for resolution can be a problem. The time required to find an inconsistency in a large database of propositions may be huge
- One useful way to simplify the resolution process is to restrict the form of the propositions
    - **horn clauses** only can be in one of two forms:
        1. Single atomic proposition on the left side (called **headed horn clauses**) used to state *relationships*
        2. empty left side (**headless horn clauses**) which is used to state *facts*
### 16.6 Terms
- **Term** is a constant, variable, or structure
- **Constant** is either an **atom** or an integer
- **atom** string of letters, digits, and underscores that begin with lowercase letter or string of any printable ASCII characters delimited by apostrophes
- **variable** any string of letters, digits, and underscores that begins with uppercase letter or underscore
    - variables are not bound to types by declaration
- **instantiation** the binding of a value, and thus a type, to a variable.
    - occurs only in the resolution process
    - last only as long as it takes to satisfy one complete goal
- **uninstantiated** a variable that has not been assigned a value
- **Structure** represent the atomic propositions of predicate calculus
    - the means of specifying facts in Prolog
    ```
    functor(parameter list)
    ```
- The functor is any atom and used to identify the structure
- parameter list can be any list of atoms, variables, or other structures
### 16.6 Elements of Prolog
- `=` is an infix operator for equality
- `is` operator take arithmetic expression as right operand and variable as left operand
    ```prolog
    A is B / 17 + C
    ```
- sets the value of A but not the same as assignment statement
- the following is illegal
    ```prolog
    Sum is Sum + Number
    ```
- variable on the left must be uninstantiated
- variable on the right side must be instantiated
### Trace
- built-in structure that displays instantiations at each step
- **Tracing model** of execution - four events:
    1. **Call** - beginning of attempt to satisfy goal
    2. **Exit** - when a goal has been satisfied
    3. **Redo** - when a backtrack occurs
    4. **Fail** - when a goal fails
### 16.6 List Structures
- An atomic proposition, which looks more like function call than data structure, is actually a form of a record.
- **List** another Prolog data structure - a sequence of any number of elements (can be atoms, atomic propositions, or other terms including other lists)
    ```prolog
    [apple, prune, grape, melon]
    [] (empty list)
    [X | Y] (head X and tail Y)
    ```
- `|` two meanings 
    1. used to dismantle lists
    2. used to create lists
- if `List_1` is instantiated to a list `[cs, math, physics]` and an atom `New_Elmnt` is an atom `chemistry` then statement
    ```prolog
    [New_Elmnt | List_1]
    ```
- creates a new list `[chemisty, cs, math, physics]`

