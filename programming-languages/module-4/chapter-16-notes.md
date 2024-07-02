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
-**Term** is a constant, variable, or structure
-**Constant** is either an **atom** or an integer
-**atom** string of letters, digits, and underscores that begin with lowercase letter or string of any printable ASCII characters delimited by apostrophes
-**variable** any string of letters, digits, and underscores that begins with uppercase letter or underscore
    - variables are not bound to types by declaration
-**instantiation** the binding of a value, and thus a type, to a variable.
    - occurs only in the resolution process
    - last only as long as it takes to satisfy one complete goal
-**uninstantiated** a variable that has not been assigned a value
-**Structure** represent the atomic propositions of predicate calculus
    - the means of specifying facts in Prolog
    ```
    functor(parameter list)
    ```
- The functor is any atom and used to identify the structure
- parameter list can be any list of atoms, variables, or other structures

