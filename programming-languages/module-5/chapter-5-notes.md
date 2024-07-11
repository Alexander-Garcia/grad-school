# Chapter 5 video lecture notes
## Sec 5.1 - 5.3
- Imperative languages are abstraction of von neumann architecture
- 2 primary components of this architecture
    1. memory: stores both instructions and data
    2. processor: provides operations for modifying the contents of memory
- abstractions in a language for the memory cells of the machine are variables
- a variable can be characterized by a collection of properties, or attributes, the most important of which is `type`
## Sec 5.3
- The clearest way to explain the various aspects of variables as abstractions of memory cells, is to characterize a variable as a sextuple of attributes
    1. name
    2. address
    3. value
    4. type
    5. lifetime
    6. scope
#### Name
- `name << == >> identifier`
    - a string of characters used to identify some entity in a program
- Following are the primary design issues for names:
    * Are names case sensitive?
    * Are the special words of the language reserved words or keywords?
- In C-based languages, uppercase and lowercase letters in names are distinct. Names are case sensitve
    - It may be considered as a detriment to readability
- To some extent, case sensitivity violates the design principle that language constructs that look similar should have similar meanings
- **special words** -> an aid to readability
    - to name actions to be performed
    - to separate sytactic parts of programs
- **keyword** a word that is special ONLY in certain contexts (can be redefined -> like in fortran)
- **reserved word** special word that cannot be used as a user-defined name ever.
- Potential problem with reserved words: if there are too many, many collisions occur (cobol has 300 reserved words) hurts readability
- Name forms
    - length: from single character names in earliest programming languages (pre-fortran) to unlimited length in many modern languages
    - symbols in names: Names in most programming languages have the same form: a letter followed by a string consisting of:
        - letters
        - digits
        - underscore characters (use of underscores and mixed case in names is a programming style issue, not language design issue
    - all variable names in PHP must begin with a $
    - in Perl, special character at the beginning of a variables name specifies its type
    - in Ruby special characters (@ and @@) at the beginning indicate its an instance or a class variable
#### Address
- machine memory address with which it is associated (sometimes called an l-value)
- **aliases** - when more than one variable name can be used to access the same memory location
#### Type
- determines range of values and set of operations
- for floating point type also determines precision
#### Value
- is contents of memory cell or cells associated with the variable
- physical cells, or individually addressable units, most byte size, which is too small for most program variables
- convenient to think of computer memory in terms of abstract cells, rather than physical cells
- an abstract memory cell has the size required by the variable with which it is associated
- Variable's value is sometimes called its *r-value* because it is what is required when the name of the variable appears in right side of assignment statement
- value of each simple non-structured type is considered to occupy a single abstract cell. Memory cell will mean abstract memory cell
### Concept of Binding
- association between an attribute and an entity
    - such as between a variable and its type or value or between an operation and a symbol
- **binding time** time at which a binding takes place
- Possible binding times:
    - language design time - bind operator symbols to operations
    - language implementation time - bind floating point type to a representation
    - compile time - bind a variable to a type in C or Java
    - load time - bind a C or C++ static variable to memory cell
    - runtime - bind a non-static local variable to a memory cell
- **static** if it first occurs before run time begins and remains unchanged throughout program execution
- **dynamic** IF binding first occurs during runtime or can change in course of program execution
- before a variable can be referenced in a program, it must be bound to a data type
    - two important aspects of this binding are:
        1. how the type is specified
        2. when the binding takes place
- **static** can have
    1. Implicit declaration (Basic, Perl, Fortran) Perl example -> $items is a scalar (string or numerical value) -> @items is an array
        - default mechanism for specifying types of variables through default conventions rather than declaration statements
            - advantage - writability
            - disadvantage - reliability
        - Implicit can use *context* sometimes called *type inference*
            - context is type of value assigne to variable in a declaration statement
        - variable can be declared with `var` and an initial value; initial value sets type
        ```C#
        var total = 0.0;
        var name = "Fred";
        ```
    2. Explicit declaraction
        - program statement used for declaring types of variables
- **dynamic** specified through an assignment statement (JS, PHP, Python, Ruby)
- also binds variable to an address and a memory cell
- Names of variables are never bound to types: names can be bound to variables and variables can be bound to types
- Primary advantage of dynamic binding of variables -> provides more programming flexibility.
    - any variable can be assigned to any type
    - variable's type can be changed at any time
    - generic subprograms are possible
- Major disadvantages
    - Less reliability because type error detection is difficult
    - cost of implementing dynamic attribute binding is considerable particularly during execution time
        - type checking must be done at run time
        - every variable must have a run-time descriptor associated with it to maintain the current type
        - storage used for the value of a variable must be of varying size because different type values require different amounts of storage
- Languages that have dynamic type binding for variables are usually implemented using pure interpreters rather than compilers
#### Storage bindings and lifetime
- **allocation** getting a cell from some pool of available cells
- **deallocation** putting a cell back into the pool
- **lifetime** of a variable is the time during which it is bound to a particular memory cell
#### Categories of variables according to their lifetime
1. Static variables
    - bound to memory cells before execution begins and remains bound to same memory cell throughout execution
        - C and C++ static variables in functions; global variables
    - Advantages: efficiency (direct addressing) history-sensitive subprogram support
    - Disadvantage: lack of flexibility (no recursion; no memory sharing)
2. Stack-dynamic variable
    - storage bindings are created when their declaration statements are elaborated, but whose types are statically bound
    - elaboration of a declaraction referes to the storage allocation and binding process indicated by declaration
        - takes place when execution reaches code to which the declaration is attached (during run time)
    - allocated from run-time stack; all attributes other than storage are statically bound to stack-dynamic scalar variables
        - C subprograms
        - Java methods
    - advantages: recursion is possible, storage sharing for subprograms
    - disadvantages: overhead of allocation and deallocation, subprograms cannot be history sensitive, inefficient references (indirect addressing)
3. Explicit Heap-Dynamic variables
- variables are nameless (abstract) memory cells that are allocated and deallocated by explicity run-time instructions written by programmer
    - can only be referenced through pointer or reference variables
- some languages also include a subprogram or operator for explicitly destroying explicit heap-dynamic variables
- created by either an **operator** (C++) or call to **system subprogram** (in C)
```C++
int *intnode; // create pointer
intnode = new int; // create heap-dynamic variable
// often used to create dynamic structures such as linked lists and trees, that need to grow or shrink during execution

delete intnode; // deallocate variable to which intnode points
```
- Disadvantages
    - difficulty user pointer and reference variables correctly
    - cost of references to variables
    - complexity of required storage management
- Advantage
    - convenient dynamic storage management
4. Implicit Head-Dynamic variables
- bound to heap storage only when they are assigned values (JS, PHP, etc.)
- all attributes are bound every time they are assigned
- Advantage
    - highly generic code
- Disadvantage
    - inefficient because all attributes are dynamic
    - loss of error detection
## Sec 5.5
- **Scope** is range of statements over which it is visible
- variables is visible in a statement if it can be reference or assigned within that statement
- local variables of a program unit are those declared in that unit
- non-local variables are visible in unit but not declared within that unit
- global variables special category of non-local variables
- Scope Rules -> determine how references to names are associated with variables
    - **static scope** and **dynamic scope**
### Static scoping (lexical scoping)
- permits human reader (and compiler) to determine type of every variable in program simply by examing its source code (text)
- allows to determine scope of variable statically - prior to execution
- Assumptions
    - all scopes are associated with program units
    - all reference nonlocal variables are declared in other program units
    - scoping is only method of accessing nonlocal variables in language under discussion
- Variables in a block scope are typically stack-dynamic so their storage is allocated when section is entered and deallocated when section is exited
- scope of global variables extends from their declaration to the end of program but skips over any subsequent function definitions.
    - no implicitly visible in any function
- static scoping works well in many situations
- problems:
    - most cases, too much access is possible
    - as program evolves, initial structure is destroyed an dlocal variables often become global which damages reliability
    - subprograms also gravitate toward becoming global rather than nested
### Dynamic scoping
- based on calling sequence of subprograms, not on their spatial relationship to each other -> scope can only be determined at run time
- just assume dynamic-scoping rules apply to nonlocal
```javascript
function big() {
    function sub1() {
        var x = 7;
    }
    function sub2() {
        var y = x;
    }
    var x = 3;
}
```
- Two different call sequences for sub2
    1. big calls sub1 which calls sub2. Search proceeds from local procedure, sub2, to its caller, sub1, where declaration for x is found
        - so reference to x in sub2 in this case is to the x declared in sub1 => value of x = 7
    2. sub2 is called directly from big. dynamic parent of sub2 is big, and reference is to x declared in big => x = 3
- if static scoping were used in either calling sequence, reference to x in sub2 would be to big's x
- Advantage: convenience
- Disadvantages
    - while subprogram is executing, its variables are visible to all subprograms it calls
    - impossible to statically type check
    - poor readability - it is not possible to statically determine type of variable
    - programs work slower than in static-scoped language
## Sec 5.6 Scope and Lifetime
- Sometimes scope and lifetime of a variable appear to be related, but are different concepts
- Example:
    - static variable in C or C++ using `static`
    - statically bound to scope of function and also statically bound to storage
    - its scope is static and local to the function, but its lifetime extends over the entire execution of the program of which it is a part
## Sec 5.7 Referencing Env
- collection of all variables that are visible in the statement
- in a static-scoped language it includes all variables declared in its local scope plus collection of all variables of its ancestor scopes that are visible
- Example in python:
```python
g = 3 # a global
def sub1():
    a = 5 # creates a local
    b = 7 # creates another local
    # point 1
    def sub2():
        global g # global g is now assignable
        c = 9 # a new local
        # point 2
        def sub3():
            nonlocal c # makes nonlocal c visible
            g = 11
            # point 3
```
- Referencing envs
    - Point 1 -> local a and b of sub1, global g for reference, but for assignment
    - Point 2 -> local c of sub2, global g for both reference and assignment
    - Point 3 -> Nonlocal c of sub2, local g of sub3
## Sec 5.8 Named Constants
- variable that is bound to a value only once
    - aid to readability
    - improvement of reliability
    - parametrization of programs
- Binding of values to named constants can be either static (manifest constants) or dynamic
- languages:
    - C++ and Java: expressions of any kind; may be dynamically bound
    - C# has two kinds of name constants, **readonly** and **const**
        - values of **const** named constants are bound at compile time
        - values of **readonly** are dynamically bound
