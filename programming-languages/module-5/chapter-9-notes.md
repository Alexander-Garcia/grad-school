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
