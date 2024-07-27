# Chapter 10
- **subprogram linkage** subprogram call and return operations of a language
- General semantics of calls to subprogram
    - parameter passing methods
    - stack-dynamic allocation of local variables
    - save execution status of calling program
    - transfer of control and arrange for return
    - if subprogram nesting is supported, access to nonlocal variables must be arrange
- general semantics of subprogram returns
    - in mode and inout mode parameters must have their values returned
    - deallocation of stack-dynamic locals
    - restore execution status
    - return control to caller
## 10.2 Simple subprograms
- "simple" subprograms only have static local variables, and nested subprograms are not allowed
- Call semantics
    - save execution status of caller
    - pass parameters
    - pass return address to the called
    - transfer control to the called
- Return semantics
    - If pass-by-value-result or out mode parameters are used, move current values of those parameters to their corresponding actual parameters
    - if it is a function, move functional value to a place the caller can get it
    - restore execution status of the caller
    - transfer control back to caller
- Required storage
    - status information, parameters, return address, return value for functions, temporary variables
    - The format, or layout, of the non-code part of an executin subprogram is called an activation record
    - An active record instance is a concrete example of an activation record (the collection of data for a particular subprogram activation)
    - 
## 10.3 Implement Subprograms with Stack-Dynamic Local Variables
- More complex activation record
    - compiler must generate code to cause implicit allocation and deallocation of local variables
    - recursion must be supported (adds possibility of multiple simultaneous activations of a subprogram)
- activation record format is static, but its size may be dynamic
- **dynamic link** points to the base of an instance of the activation record of the caller
- An activation record instance is dynamically created when a subprogram is called
- activation record instances reside on the run-time stack
- **Environment Pointer (EP)** must be maintained by the run-time system.
    - always points at the base of activation record instance of the currently executing program unit
- Because return address, dynamic link, and parameters are placed in the activation record instance by caller, they must appear first in stack
```C
void sub(float total, int part) {
    int list[5];
    float sum;
}
```
- Call and return semantics specify that the subprogram last called is the first to complete
    - reasonable to create instance of these activation records on a stack (run-time stack)
    - every subprogram activation, recursive or not, creates a new instance of an activation record on a stack
    - provides
        - reasonable to create instance of these activation records on a stack (run-time stack)
        - every subprogram activation, recursive or not, creates a new instance of an activation record on a stack
            - provides required separate copies of parameters, local variables, and return address
- EP is NOT shown on diagrams because the EP currently being used is NOT stored in the run-time stack
    - only saved version are stored in the activation record instance as the dynamic links
- Caller actions:
    - create an activation record instance
    - save the execution status of the current program unit
    - compute and pass parameters
    - pass return address to the called
    - transfer control to the called
- Prologue actions of the called:
    - save the old EP in the stack as the dynamic link and create the new value
    - allocate local variables
- Epilogue actions of the called:
    - If there are pass-by-value-result or out-mode parameters, current values of those are moved to corresponding actual parameters
    - if subprogram is function, its value is moved to a place accessible to caller
    - restore the stack pointer by setting it to the value of the current EP-1 and set the EP to old dynamic link
    - restore execution status of the caller
    - transfer control back to caller
- Collection of dynamic links in stack at a given time is **dynamic chain** or call chain
- local variables can be acccessed by their offset from the beginning of the AR whose address is in the EP
    - **local offset**
- local_offset of a local variable can be determined by compiler at compile time
## 10.4 Nested subprograms
- all variables that can be non-locally accessed reside in some activation record instance in the stack
- Process of locating a non-local reference:
    - find correct activation record instance
    - determine the correct offset within that activation record instance
- Only variables that are declared in static ancestor scopes are visible and can be accessed
- activation record instances of all static ancestors are always on the stack when variables in them are referenced by a nested subprogram
- subprogram is callable onlyl when all of its static ancestor subprograms are active. 
- Static Chains
    - a new pointer **static link** (static scope pointer) is added to activation record
- Static scoping
    - **static chain** is a chain of static links that connects certain ARIs (activation record instances)
    - **static link** in ARI for subprogram A points to one of the ARI of A's static parent
    - static chain from an ARI connects it to all of its static ancestors
    - **static-depth** is an integer associated with a static scope whose value is the depth of nesting of that scope
    - **chain-offset** or nesting-depth of a nonlocal reference is difference between static depth of reference and that of the scope where it is declared
    - reference to a variable can be represented by the pair:
        - (chain offset, local offset)
            - where local offset is offset in the activation record of the variable being referenced
- Static chain maintenance
    - activation record instance must be built
    - dynamic link is just the old stack top pointer
    - static link must point to most recent ARI of static parent
- Problems:
    - nonlocal reference is slow if nesting depth is large
    - time critical code is difficult:
        1. costs of nonlocal references are difficult to determine
        2. code changes can change the nesting depth, and thus cost
```Python
# Global scope
def f1():
    def f2():
        def f3():
        # end f3
    # end f2
# end f1
```
- static-depths of global scope -> 0
- f1 -> 1
- f2 -> 2
- f3 -> 3
- if procedure f3 references a variable declared in f1, the chain_offset of that reference would be 2
    - static-depth of f3 - fatic-depth of f1
## 10.5 Blocks
- Blocks are user-specified local scopes for variables
- Lifetime of a block is only when control enters block
- advantage of using local variable like temp is that it cannot interfere with any other variables with same name
- Implementing Blocks
    1. Treat blocks as parameter-less subprograms that are always called from same location
        - every block has an AR; an instance is created every time the block is executed
    2. Since maximum storage required for a block can be statically determined, this amount of space can be allocated after local variables in AR
- Dynamic scoping
    - Deep access
        - non-local references are found by searching the AR instances on the dynamic chain
            - length of chain cannot be statically determined
            - every activation record instance must have variables names
- dynamic link is a pointer to the base of an activation record instance of the caller
- Shallow Access
    - put locals in a central place
        - one stack for each variable name
        - central table with an entry for each variable name
