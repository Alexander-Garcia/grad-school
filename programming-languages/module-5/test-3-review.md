# Test 3 review
- **Sections covered - 5.1 -5.8, 7.1 - 7.7, 9.1 - 9.9**
## Chapter 5
### section 5.2 Names
- **name** string of characters used to identify some entity in a program
- In many languages names are **case sensitive**
    - in C++ `rose`, `ROSE`, and `Rose` are all distinct
    - Serious detriment to readability, because names that look very similar denote different entities.
    - avoided by conventions like camel case
- **reserved word** special word of a programming language that cannot be used as a name
- A variable is a sextuple of attributes
    - name
    - address
    - value
    - type
    - lifetime
    - scope
##### Address
- machine memory address with which a variable is associated
- In many languages it is possible for the same variable to be associated with different addresses at different times
- **l-value** address of a variable because the address is what is required when the name of a variable appears in left side of assignment
- Possible to have multiple variables that have same address
- **alias** when more than one variable name can be used to access same memory location
    - hinderance to readability because it allows a variable to have its value changed by assignment to a different variable
    - makes program verification more difficult
##### Type
- determines range of values the variable can store and set of operations that are defined for values of the type.
##### Value
- contents of the memory cell or cells associated with the variable.
- **r-value** because it is what is required when the name of the variable appears in right side of assignemnt statement.
    - to access r-value the l-value must be determined first
#### 5.4 Binding
- **binding** is association between an attribute and an entity
    - such as between a variable and its type or value, or between an operation and a symbol
- **binding time** time at which binding takes place
```C++
count = count + 5
```
- Type of count is bound at compile time
- set of possible values of count is bound at compiler design time
- meaning of operator symbol + is bound at compile time, when types of its operands have been determined
- Internal representation of literal 5 is bound at compiler design time
- Value of count is bound at execution time with this statement
- **static binding** if it first occurs before run time begins and remains unchanged throughout program execution
- **dynamic binding** if binding first occurs during run time or can change in course of program execution
##### Static Type Binding
- **explicit declaration** is a statement in a program that lists variable names and specifies that they are a particular type
- **implicit declaration** is a means of associating variables with types through default convetions, rather than declaration statements
    - both implicit and explicit declarations create static bindings to types
- Although minor convenience to programmers, implicit declarations can be detrimental to reliability
    - they prevent compilation process from detecting some typographical and programmer errors
- Another kind of implicit type declarations uses context
    - **type inference**
- context is the type of the value assigned to the variable in a declaration statement.
- Example C# has `var` declaration of a variable which must include an initial value, whose type is taken as the type of the variable
    ```C#
    var sum = 0;
    var total = 0.0;
    var name = "Fred";
    ```
- types of sum, total, and name, are int, float, and string.
-  these are statically typed variables - their types are fixed for the lifetime of the unit in which they are declared
##### Dynamic Type Binding
- type of a variable is not specified by a declaration statement, nor can it be determined by spelling of its name.
    - bound to a type when it is assigned a value in an assignment statement.
- Disadvantages:
    - causes programs to be less reliable because error-detection capability of compiler is diminished relative to static type bindings
    - cost -implementing dynamic attribute binding is considerable, particularly in execution time. Type checking must be done at run time
    - usually implemented using pure interpreters rather than compilers.
        - compiler cannot build machine instructions for the expression a + b if types of a and b are not known at compile time
        - pure interpretation typically takes at least 10 times as long as it does to execute equivalent machine code
##### Storage Bindings and Lifetime
- Process of **allocation**
    - when a memory cell to which a variable is bound somehow must be taken from a pool of available memory
- **deallocation** is process of placing a memory cell that has been unbound from a variable back into the pool of available memory
- **lifetime** of a variable is the time during which the variable is bound to a specific memory location
##### Static Variables
- **static variable** one that is bound to a memory cell before program execution begins and remains bound to that same memory cell until program execution terminates.
    - Advantages:
        - efficiency
        - all addressing of static variables can be direct; other kinds of variables often require indirect addressing, which is slower.
        - no run-time overhead is incurred for allocation and deallocation of static variables, although this time is often negligible
    - Disadvantage:
        - reduced flexibility; in particular, a language that has only stati cvariable cannot support recursive subprograms
        - storage cannot be shared among variables
##### Stack-Dynamic Variables
- **stack-dynamic variables** those whose storage bindings are created when their declaration statements are elaborated, but whose types are statically bound
- **Elaboration** of such a declaration referes to the storage allocation and binding process indicated by the declaration
    - takes place when execution reaches the code to which the declaration is attached
    - occurs during run time
- For example
    - variable declarations at beginning of a Java method are elaborated when method is called
    - variables defined by those declarations are deallocated when the method completes execution
- allocated from the run-time stack
- Advantages:
    - meets the needs of recursive subprograms
- Disadvantages (relative to stack variables):
    - run-time overhead of allocation and deallocation, possibly slower access because indirect addressing is required
- in Java, C++, and C# variables defined in methods are by default stack dynamic
##### Explicit Heap-Dynamic Variables
- nameless (abstract) memory cells that are allocated and deallocated by explicit run-time instructions written by the programmer.
- these variables, which are allocated from and deallocated to the heap, can only be referenced through pointer or reference variables
```C++
int *intnode; // create pointer
intnode = new int; // create heap-dynamic variable
delete intnode; // deallocate heap-dynamic variable to which intnode points
```
- C++ requires explicit deallocation operator `delete`, because it does not use implicit storage reclamation, such as garbage collection
- Java objects are explicitly heap dynami cand are accessed through reference variables
- Disadvantages
    - difficulty of using pointer and reference variables correclty
    - cost of references to variables
    - complexity of required storage management implementation
##### Implicit Heap-Dynamic Variables
- bound to heap storage only when they are assigned values
- all their attributes are bound every time they are assigned
```JavaScript
highs = [74, 84, 86, 90, 71];
```
- regardless of whether the variable named highs was previously used in the program or what it was used for, it is now an array of five numeric values
- Advantages:
    - highest degree of flexibility, allowing highly generic code to be written
- Disadvantag:
    - run-time overhead of maintaining all the dynamic attributes, which could include array subscript types and ranges, among others
    - loss of some error detection by compiler
#### 5.5 Scope
- **scope** of a variable is the range of statements in which the variable is visible
- Variable is **visible** in a statement if it can be referenced or assigned in that statement
- **static scoping** scope of variable can be statically determined - that is, prior to execution
    - permits a human program reader (and compiler) to determine the type of every variable in the program simply by examing source code
- Many languages allow new static scopes to be defined in midst of executable code.
    - these variables are typically stack dynamic, so their storage is allocated when the section is entered and deallocated when the section is exited.
    - This section is called a **block**
```C
if (list[i] < list[j] {
    int temp;
    temp = list[i];
    ...
}
```
- temp would be statically created during execution
- Dynamic-scoping is based on the calling sequence of subprograms, not on their spatial relationship to each other
    - can only be determined at run time
#### 5.7 Referencing Env
- **referencing environment** of a statement is the collection of all variables that are visible in the statement
- static-scoped -> variables declared in its local scope plus the collection of all variables of its ancestor scopes that are visible
- **named constant** - variable that is bound to a value only once
    - aids readability and program reliability
- important use is to parameterize a program
- **initialization** binding of a variable to a value at the time it is bound to storage

## Chapter 7
- **unary operator** operator with single operand
- **binary** two operands
- **ternary** three operands
- In most programming languages binary operators are **infix** they appear between their operands
- **operataor precedence rules** define the order in which the operators of different precedence levels are evaluated
- many languages also include unary versions of addition and subtraction.
    - **identity operator** unary addition or subtraction that usually has no associated operation and thus has no effect on its operand
- **side effect** of a function, functional side effect, occurs when the function changes either one of its parameters or a global variable
- **referential transparency** if any two expressions in the program that have the same value can be substituted for one another anywhere in the program, without affecting the action of the program
- **operator overloading** multiple use of an operator (like +)
- **narrowing conversion** converts a value to a type that cannot store even approximations of all the values of the original type
    - converting a double to a float in java is a narrowing conversion because range of double is much larger than float
- **widening conversion** converts a value to a type that can include at least approximations of all values of original type
    - converting int to a float
- **mixed-mode expressions** opeartor with operands of different types
    - must define conventions for implicit operand type conversions because computers do not have binary operations that take operands of different types
- explicit type conversions are called **casts**
```C
(int)angle
```
- most comon error occurs when result of an operation cannot be represented in the memory cell where it must be stored
    - **overflow** or **underflow** depending on whether the result was too large or too small
- One limitation of arithmetic is that division by zero is disallowed
- Floating-point overflow, underflow, division by zero are examples of run-time errors called **exceptions**
- **relational operator** is an operator that compares values of its two operands
    - has has two operands and one relational operator
- **short-circuit evaluation** of an expression is one in which the result is determined without evaluating all of the operands and / or operators
- **compound assignment operator** is a shorthand method of specifying a commonly needed form of assignment. 
```C
a = a + b; // can be shortened
a += b
```
- multiple-target, multiple-source assignment statements
```Perl
($first, $second, $third) = (20, 40, 60);
```
## Chapter 9
- **subprogram definition** describes the interface to and the actions of the subprogram abstraction
- **subprogram call** is the explicit request that a specific subprogram be executed
-  **subprogram header** is part of the definition, serves several purposes
    - specifies that the following syntactic unit is a subprogram definition of some particular kind
    - if the subprogram is not anonymous, the header provides a name for the subprogram
    - may specify a list of parameters
```Python
def adder (parameters):
```
- **parameter profile** of a subprogram contains the number, order, and types of its formal parameters
    - **protocol** of a subprogram is its parameter profile plus, if it is a function, its return type
        - in languages which subprograms have types, those types are defined by the subprogram's protocol
- can have declarations as well as definitions
- **formal parameters** the parameters in the subprogram header
    - dummy variables because they are not variables in the usual sense
    - in most cases, bound to storage only when subprogram is called, and that binding is often through some other program variables
- subprogram call statements must include the name of the subprogram and a list of parameters to be bound to the formal parameters
    - called **actual parameters**
- In most languages, correspondence between actual and formal parameters is done by position
    - called **positional parameters**
- **keyword parameters** the name of the formal parameter to which an actual parameters is to be bound is specified with the actual parameter in a call
```Python
sumer(length = my_length,
      list = my_array,
      sum = my_sum)
```
- formal parameters are `length`, `list`, and `sum`
- disadvantage is must know names of formal parameters
- can mix positional with keyword
    - restriction is after a keyword parameter appears in list, all remaining parameters must be keyworded since postion may no longer be well defined
- formal parameters can have default values
```Python
def compute_pay(income, exemptions = 1, tax_rate):

pay = compute_pay(20000, tax_rate = 0.15)
```
- No comma is included for absent actual parameter in a Python call
    - all actual parameters after an absent actual parameters must be keyworded
- procedures and functions defined in 9.2.4
### Design issues for subprograms
- **overloaded subprogram** is one that has the same name as another subprograms in the same referencing environment
- **generic subprogram** is one whose computation can be done on data of different types in different calls
- **closure** nested subprogram and its referencing environment, which together allow subprogram to be called anywhere in a program
### 9.4 Local referencing environments
- Variables defined inside subprograms are **local variables**, because their scope is usually the body of the subprogram in which they are defined
- if local variables are stack dynamic, they are bound to storage when the subprogram begins execution
    - advantages:
        - flexibility
        - essential that recursive subprograms have stack-dynamic local variables
        - storage for local variables in an active subprogram can be shared with the local variables in all inactive subprograms
    - disadvantag:
        - cost of time required to allocate, initialize (when necessary), and deallocate such variables for each call to subprogram
        - access to stack-dynamic local variables must be indirect
        subprograms cannot be history sensitive, cannot retain data values of local variables between calls
- Primary advantage of static local variables over stack-dynami local variables is that they are slightly more efficient
    - no run-time overhead for allocation and deallocation
    - allow subprograms to be history sensitve
    - disadvantage:
        - inability to support recursion
        - storage cannot be shared with the local variables of other inactive subprograms
### 9.5 Parameter-Passing methods
- 
