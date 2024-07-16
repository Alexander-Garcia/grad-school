# Chapter 9
## Sec 1 Introduction
- Two fundamental abstraction facilities
    1. Process abstraction
    2. Data abstraction
- Fundamentals of subprograms
    - Each subprogram has a single entry point
    - The calling program unit is suspended during the execution of the called subprogram,
    which implies that there is only one subprogram in execution at any given time
    - Control always returns to the caller when the subprogram execution terminates
- **subprogram** interface to and the actions of the subprogram abstraction
- **subprogram call** explicit request that the subprogram be executed
- **subprogram header** first part of the definition, including the name, kind of subprogram, and formal parameters
```Python
def adder(parameters):
```
- **parameter profile (signature)** of a subprogram is the number, order, and types of its parameters
- **protocol** is a subprogram's parameter profile and, if it is a function, its return type
- subprogram declaration provides the protocol, but not the body, of the subprogram
- Function declarations in C and C++ are often called prototypes
- Two ways that non-method subprogram may have access to data
    1. non-local variables
        - extensive access to non-local variables may reduce reliability
    2. parameters
        - parameterized computation
        - *methods* in OO languages may access both internal object data and outside data.
- Formal parameter is a dummy variable listed in the subprogram header and used in the subprogram.
    - bound to the memory only when a subprogram is called
## Sec 4 Referencing Env
- Subprograms can define their own (local) variables -> create their own local referencing envs
- Local Variables can be stack-dynamic
    - Advantages:
        - support for recursion
        - storage for locals is shared among some subprograms
    - Disadvantages:
        - allocation / deallocataion, initialization  time
        - indirect addressing
        - subprograms cannot be history sensitive
- Local variables can be static
    - Advantages and disadvantages are the opposite of those for stack-dynamic local variables
    - In most contemporary languages, locals are stack dynamic
    - In C-based languages, locals are by default stack dynamic, but can be declared `static`
    - Methods of C++, Java, Python, and C# only have stack dynamic locals
- Example from C/ C++
```C
int adder(int list[], int listlen) {
    static int sum = 0;
    int count;
    for (count = 0; count < listlen; count++)
        sum += list[count];
        return sum;
}
```
- Idea of nesting subprograms:
    - ALGOL60 -> ALGOL 68, Pascal, Ada
    - JS, Python, Ruby, Lua
    - some functional languages
    - Attractiveness: creating a hierarchy of both logic and scopes.
    - Associated problem: giving too much access to non-local variables
## Sec 5 Parameter - Passing methods
- the ways in which parameters are transmitted to and / or from called subprograms
- Semantics models of parameter passing
    - in mode
    - out mode
    - inout mode
- Two conceptual models of data transfer in parameter transmission copying or access path
### Pass-by-value (In Mode)
- Value of actual parameter is used to initialize the corresponding formal parameter
    - normally implemented by copying
    - can be implemented by transmitting an access path but not recommended (enforcing write protection is not easy)
    - Disadvantages (if by physical move):
        - additional storage is required (stored twice) and actual move can be costly (for large parameters)
    - Disadvantages (if by access path method):
        - must write-protect in the called subprogram and accesses cost more (indirect addressing)
### Pass-by-Result (Out Mode)
- When a parameter is passed by result, no value is transmitted to the subprogram; corresponding formal parameter acts as a local variable;
its value is transmitted to caller's actual parameter when control is returned to the caller, by physical move
    - require extra storage location and copy operation
### Pass-by-value-result (inout mode)
- combination of pass-by-value and pass-by-result
- sometimes called pass-by-copy
- formal parameters have local storage
- disadvantages:
    - those of pass-by-result
    - of pass-by-value
### Pass-by-reference (inout mode)
- pass an access path
- also called pass-by-sharing
- advantage
    - passing process is efficient (no copying and no duplicated storage)
- disadvantages
    - slower accesses (compared to pass-by-value) to formal parameters
    - potentials for unwated side effects (collisions)
    - unwated aliases (access broadened)
- Skip pass-by-name (not included on quizes and tests)
- Implementing parameter-passing methods
    - parameter communication takes place thru the run-time stack
    - Pass-by-refernce are simplest to implement; only an address is placed in the stack
- section 9.5.4 not on quizes or tests
### Type checking parameters
- considered very important for reliability
- FORTRAN77 and original C: none
```C
double sin (double x) {...}
double value;
int count;
value = sin(count);
```
- Is it legal?
    - Yes if coercion is allowed (it IS allowed in C)
    - No if coercion is not allowed -> mismatched types will be reported as a compile-type error
- Multidimensional arrays as parameters
    - programmer is required to include the declared sizes of all but the first subscript in the actual parameter (C and C++)
    - disallows writing flexible subprograms
```C
void fun(int matrix[][10]) {...}
void main() {
    int mat[5][10]
    fun(mat);
}
```
- Solution: pass a pointer to array and the sizes of dimensions as other parameters
- user must include the storage mapping function in terms of the size of parameters
- Example: 
```C
void fun(float *mat_ptr, int num_rows, int num_cols);
*(mat_ptr + (row * num_cols) + col) = x;
```
- Java and C#
    - similar to ada
    - arrays are objects; are all singe-dimensioned, but elements can be arrays
    - each array inherits a named constant (length in Java, Length in C#) that is set to length of array when array object created
- Design considerations
    - 2 important considerations
        1. efficiency
        2. one-way or two-way data transfer
    - but the above considerations are in conflict
        - good programming suggest limited access to variables, which means one-way whenever possible
        - pass-by-reference is more efficient to pass structures of significant size
- section 9.5.7 not included into quizzes and tests, but interesting
## Sec 6 Parameters that are subprogram names
- issues
    - are parameter types checked?
    - what is correct referencing environment for a subprogram that was sent as a parameter?
        -  only an issue for languages that allow nested subprograms
    - **shallow binding** environment of call statement that enacts the passed subprogram
        - most natural for dynamic-scoped languages
    - **deep binding** environment of the definition of the passed subprogram
        - for static-scoped languages
    - **ad hoc binding** env of the call statement that passed the subprogram
```JavaScript
function sub1() {
    var x;
    function sub2() {
        alert(x);
    };
    function sub3() {
        var x;
        x =3;
        sub4(sub2);
    };
    function sub4(sub2) {
        var x;
        x = 4;
        sub2();
    };
    x = 1;
    sub3();
};
```
- referencing env of execution of sub2 when it is called in sub4 will be
    - Shallow binding:
        - sub4 => x is 4
    - Deep binding
        - sub4 => x is 1
    - ad hoc binding
        - sub4 => x is 3
## Sec 7 Calling subprograms indirectly
-  when there are several possible subprograms to be called and correct one on a particular run of a program is not known until execution
- in C and C++ done with function pointers
- C# method pointers are implemented as obejcts called *delegates*
## 8 design issues for functions
- Are side effects allowed?
    - Parameters should always be in-mode to reduce side effect (like ada)
- Most imperative languages: functions can have either pass-by-value or pass-by-reference parameters => functions may have side effects and aliasing
- pure functional languages do not have variables so no side effects produced by functions
- Why types of return values are allowed?
    - most imperative languages restrict return types
    - C allows any type except arrays and functions
    - C++ allows user-defined types
    - Java and C# methods can return any type (but because methods are not types, they cannot be returned)
    - Python and Ruby treat methods as first-class objects, so they can be returned, as well as any other class
- Functional languages functions may be parameters and return values
- Number of returned values
    - in most languages only a single value may be returned from a function
    - however, using different syntax rules, some languages allow to return multiple values -> Ruby, Lua, Python, ML, F#
## Sec 9 Overloaded subprograms
- Overloaded operator is one that has multiple meanings
    - meaning of a particular instance of an overloaded operator is determined by types of its operands
- Overloaded subprogram is one that has same name as another subprogram in the same referencing environment
    - every version of an overloaded subprogram has a unique protocol
- meaning of the call is determined by the actual parameters list
- usually overloaded subprograms implement same process
- C++, Java, C#, and Ada include predefined overloaded subprograms
    - they allow users to write multiple versions of subprograms with same name
- In Ada, return type of an overloaded function can be used to disambiguate calls (thus two overloaded functions can have same parameters)
- Overloaded subprograms that have default parameters can lead to ambigous subprogram calls.
- C++ example
```C++
void fun(float b = 0.0);
void fun();
fun();
```
- this call is ambigous and will cause compilation error
## Sec 10 Generic subprograms
- Why generic? -> to increase productivity
- reusability of software is to lessen need to create different subprograms tha timplement same algorithm on different types of data
- **polymorphic** subprogram takes parameters of different types on different activations
- Overloaded subprograms provide a particular kind of polymorphism **ad hoc polymorphism**
    - overloaded subprograms need not behave similarly
- Lanugages that support OOP usually support subtype polymorphism
    - **subtype polymorphism** means that a variable of a parental type T can access any object of type T or any type derived from T
- Parametric polymorphism is provided by subprogram that takes generic parameters that are used in type expressions
## Sec 11 User-defined overloaded operators
```Python
def __add__(self, second):
    return Complex(self.real + second.real, self.image + second.image)
```
- to compute `x + y` -> `x.__add__(y)`
## Sec 13 Coroutines
- subprogram that has multiple entry points and controls them itself
- coroutine control mechanism is often called the **symmetric unit control model** 
    - caller and called coroutines are on a more equal basis
- secondary executions of a coroutine often begin at the point other than its beginning -> invocation of a coroutine is valled a **resume**
- First resume of a coroutine is to its beginning, but subsequent calls enter at the point just after the last executed statement in coroutine
    - coroutines repeatedly resume each other, possibly forever
- coroutines provide quasi-concurrent execution of program units (the coroutines); their execution is interleaved, but not overlapped
- just one of the usual characteristics of subprograms is maintained in coroutines
    - only one coroutine is actually in execution at a given time
- 
