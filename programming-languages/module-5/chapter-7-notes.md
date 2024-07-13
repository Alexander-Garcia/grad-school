# Chapter 7
## Sec 1 Intro
- Expressions are fundamental means of specifying computations in programming language
- Arithmetic expressions consist of operators, operands, parentheses, and function calls
    - Unary operator has one operand
    - Binary operator has two operands
    - ternary operator has three operands
- In most languages, binary operators are infix
- Most unary operators are prefix, but the ++ and -- can be either prefix or postfix
- Design issues for arithmetic expressions
    - Operator precedence rules
    - operator associativity rules
    - Order of operand evaluation
    - operand evaluation side effects
    - operator overloading
    - type mixing in expressions
- Typical precedence levels
    - parentheses
    - unary operators
    - ** (if language supports it)
    - `* , /`
    - `+, -`
- Compilers may change the order of operands based on associativity rules having no impact on value of expression
- Conditional expressions
    ```C
    average = (count == 0) ? 0 : sum /count
    ```
- In general -> `expressions1 ? expression2 : expression3`
- Operand evaluation order
    1. Variables: fetch the value from memory
    2. Constatns: sometimes a fetch from memory; sometimes the constant is in the machine language instruction
    3. Parenthesized expressions: evaluate all operands and operators first
    4. Most interesting case is when an operand is a function call
- Functional side effects: when a function changes a two-way parameter or a non-local variable
- Problem with functional side effects:
    - When a function referenced in an expression alters another operand of the expression; for a parameter change
    ```C
    a = 10;
    /* assum that fun changes its parameter */
    b = a + fun(&a)
    ```
- Two possible solutions to the problem
    1. Write the language definition to disallow functional side effects
        - No two-way parameters in functions
        - No non-local references in functions
        - Advantage: it works
        - Disadvantage: inflexibility of one-way parameters and lack of non-local references
    2. Write language definition to demand that operand evaluation order be fixed
        - Disadvantage: limits some compiler optimizations
        - Java requires operands appear to be evaluated in left-to-right order
### Referential Transparency
- Program has property of referential transparency if any two expressions in the program that have the same value can be
substituted for one another anywher in the program without affecting action of the program
```C
result1 = (fun(a) + b) / (fun(a) - c);
temp = fun(a);
result2 = (temp + b) / (temp - c);
```
- if `fun` has no side effects, `result1 = result2`
- otherwise, referential transparency is voilated
- Advantage of referential transparency
    - semantics of a program is much easier to understand if it has referential transparency
- Functional languages do not have variables and are referential transparent
    - functions cannot have state
    - if a function uses an outside value, it must be a constant (no variables) so value of a function depends only on its parameters
## Sec 3 and 4
### Overloaded Operators
- Use of an operator for more than one purpose is called operator overloading
- Are arithmetical operators + and / overloaded?
    - Both are overloaded (integer addition and floating point addition) same with /
- How about &?
    - as binary operator (x & y) ==> bitwise logical AND
    - as unary operator (&x) ==> address of a variable x
- `*` operator
    - Binary ( x * y) ==> multiplication
    - Unary (*px) ==> dereferenced pointer
- Problem: using same symbol for two completely unrelated operations
    - loss of compiler error detection (omission of an operand should be a detectable error)
    - some loss of readability
- Some languages allow user-defined overloading
    - C++, C#, F#
    - when sensibly used, such operators can be an aid to readability (avoid method calls, expressions appear natural)
    - Potential problems:
        - users can define nonsense operations
        - readability may suffer, even when the operators make sense
### Type Conversions
- **narrowing conversion** is one that converts an object to a type that cannot include all of the values of original type e.g., float to int
- **widening conversion** is one in which an object is converted to a type that can include at least approximations to all of the values of original type e.g., int to float
- *Accuracy may be lost even in some widening conversions* (see textbook for example)
- **mixed-mode expression** is one that has operands of different types
- **coercion** is an implicit type conversion
- Disadvantage of coercions:
    - they decrease in the type error detection ability of compiler
- most languages, all numeric types are coerced in expressions, using widening conversions
- **explicity type conversion (casting)**
    ```C
    (int) angle
    ```
    ```F#
    float(sum)
    ```
## Sec 5 and 6
- Relation expressions
    - use relational operators and operands of various types
    - evaluate to some boolean representation
    - operator symbols used vary somewhat among languages (!=, /=, ~=, .NE., <>)
- JS and PHP have two additional relation operator, === and !==
    - similar to their cousins, == and !=, except that they do not coerce their operands
    - Ruby uses == for equality relation operator that uses coercions and `eql?` for those that do not
- One odd characteristic of C's expressions:
```C
a > b > c
```
- Legal expression, but result is not what you might expect
- 9 > 7 > 5 ==> 1 > 5 ==> false
- 9 > 7 is evaluated to true which is 1 in early version of C
### 7.6 Short-circuit Evaluation
- Expression in which the result is determined without evaluating all of the operands and / or operators
- Example: (13 * a) * (b / 13 - 1)
- if value of a is 0 then final result is always 0
- For arithmetical expressions it is not easy to identify the situation of this type so shortcut is never taken
- For boolean expressions it can be easily identified and short circuit is taken
- Potential problem with non-short-circuit-evaluation Boolean expression
- Assume `list` has `listlen` elements, is the array to be searched for the value `key`
```C
index = 0;
while ( (index < listlen) && (list[index] != key) )
    index = index + 1;
```
- if short-circuiting is NOT used, expressions on both side of `&&` operator will be evaluated even when the first expressions has a `false` value => indexing error
- C, C++, Java: use short-circuit evaluation for Boolean operators (&& and ||) but also provide bitwise boolean operators that are not short circuit (& and |)
- Short-circuit evaluation exposes the potential problem of side effects in expressions
- (a > b) || (b++ / 3)
## Sec 7 Asisgnment Statements
- general syntax
- <target_var> <assign_operator> <expression>
- = can be bad when it is overloaded for the relational operator for equality (that is why C based languages use == as relational operator)
- conditional targets (perl)
```Perl
($flag ? $total : $subtotal) = 0
```
- Compound assignment operator
    - shorthand method of specifying a commonly needed form of assignment
    - introduced in ALGOL; adopted by C and C-based languages
    ```C
    a += b
    ```
- Unary assignment operators
    - combine increment and decrement operations with assignment
    ```C
    sum = ++count
    sum = count++
    -count++
    ```
- First statement -> count incremented, then assigned to sum
- Second -> count assigned to sum then incremented
- third -> count incremented then negated
    - 2 unary operators applied to the same operands => association is right to left (-(count++))
- In C based languages, Perl, and JS, assignment statement produces a result and can be used as an operand
```C
while ((ch = getchar()) != EOF) {...}
```
- `ch = getchar()` is carried out; the result (assigned to ch) is used as a conditional value for the while statement
- Disadvantage: another kind of expression side effect
```C
a = b + (c = d / b) - 1
```
- Denotes the instructions
    - assign d / b to c
    - assign b + c to temp
    - asisgn temp - 1 to a
```Python
sum = count = 0
```
- Assigns from right to left. count is assign to 0 then assigned to sum. Legal in python
- Assignment statements can also be mixed-mode
- In Java and C# only widening assignemnt coercions are done
- In Fortran, C, Perl, and C++ any numeric type value can be assigned to any numeric type variable
