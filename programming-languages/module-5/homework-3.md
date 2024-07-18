# Homework 3
1. Define the concepts of static binding and dynamic binding.
    - A binding is static if it
        - first occurs before run time begins and remains unchanged throughout program execution
        - Static binding can have explicit or implicit declarations
    - A binding is dynamic if
        - it first occurs during run time or can change in the course of program execution.
        - With dynamic type binding, type of a vriable is not specified by a declaration statement

2. List all variables, along with program units where they are declared, that are visible in bodies of `sub1`, `sub2`, and `sub3` assuming static scoping is used.
    ```JavaScript
    var x, y, z;
    function sub1() {
        var a, y, z;
        function sub2() {
            var a, b, z;
            ...
        }
        ...
    }
    function sub3() {
        var a, x, w;
        ...
    }
    ```
- Visible in body of Sub1
    - Variables x, y, and z declared in the main program because it is a static parent of sub1
    - Variables a, y, and z declared in sub1
- Visible in body of Sub2
    - Variables x, y, and z declared in the main program because it is a static ancestor of sub2
    - Variables a, y, and z declared in sub1 because it is a static parent of sub1
    - Variables a, b, and z declared in sub2
- Visible in body of Sub3
    - Variables x, y, and z declared in main program because it is a static parent of sub3
    - Variables a, x, and w declared in sub3

3. Explain why it is difficult to eliminate functional side effects in C
    - One reason is C allows global variables. A variable outside the scope of a function can be accessed in a function and cause unintended side effects if that variable is modified elsewhere in the main program

4. Function `fun` defined as
```C
int fun(int* k) {
    *k += 4;
    return 3 * (*k) - 1;
}
```
- `fun` is used in a program as follows:
```C
void main() {
    int i = 10, j = 10, sum1, sum2;
    sum1 = (i / 2) + fun(&i);
    sum2 = fun(&j) + (j / 2);
}
```
- What are the values of sum1 and sum2
    - Operands in expressions are evaluated left to right?
        - Sum1
            - (10 / 2) + fun(10)
                - Inside fun(10)
                    - (3 * (14) - 1)
                    - (42 - 1)
            - 5 + 41
            - 46
        - Sum2
            - fun(10) + (j / 2)
                - Inside fun(10)
                    - ((3 * 14) - 1)
                    - (42 - 1)
            - (41 + 14) / 2)
            - 55 / 2
            - 27.5
    - Operands in expressions are evaluated right to left?
        - Sum1
            - (i / 2) + fun(10)
                - Inside fun(10)
                    - (3 * (14 - 1))
                    - (3 * 13)
            - 14 / (2 + 39)
            - 14 / 41
            - 0.34
        - Sum2
            -  fun(10) + (10 / 2)
            - Inside fun(10)
                - (3 * 14 - 1)
                - (3 * 13)
            - 39 + (10 / 2)
            - 39 + 5
            - 44

5. Consider following C program;
```C
int fun(int *i) {
    i += 5
    return 4;
}
void main() {
    int x = 3;
    x = x + fun(&x);
}
```
- What is the value of x after the assignment statement in main
    - Operands are evaluated left to right
        - 3 + fun(&i)
        - 3 + 4
        - 7
    - Operands are evaluated right to left
        - x + fun(&i)
        - x + 4
        - 8 + 4
        - 12

6. Make a table showing advantages and disadvantages of using local static and stack-dynamic variables

    - Advantages
        - Stack-dynamic
            - flexibility
            - storage for local variables in an active subprogram can be shared with local variables in all inactive subprograms  
        - Local Static
            - slightly more efficient, require no run-time overhead for allocation and deallocation 
            - allow subprograms to be history sensitive

    - Disadvantages
        - Stack-dynamic
            - cost of time required to allocate, initialize, and deallocate such variables for each call to subprogram  
            - accesses to stack-dynamic local variables must be indirect
            - when all local variables are stack-dynamic, subprograms cannot be history sensitive 
        -  Local Static
            - inable to support recursion
            - their storage cannot be shared with the local variables of other inactive subprograms

7. Define concepts of shallow binding and deep binding for referencing environments of subprograms that have been passed as parameters.
    - Shallow binding is the environment of the call statement that enacts the pass subprogram
        - most natural for dynamic-scope languages
    - Deep binding is the environment of the definition of the passed subprogram
        - most natural for static-scope languages
    - example
    ```JavaScript
    function sub1() {
        var x;
        function sub2() {
            alert(x);
        }
        function sub3() {
            var x;
            x = 3;
            sub4(sub2);
        };
        function sub4(subx) {
            var x;
            x = 4;
            subx();
        };
        x = 1;
        sub3();
    };
    ```
    - Consider execution of sub2 when it is called in sub4.
        - Shallow binding
            - the referencing environment of that execution is sub4, so the reference to x in sub2 is b oudn to local xi in sub4
            - output is then 4
        - Deep binding
            - referencing environment of sub2's execution is that of sub1, so reference to x in sub2 is bound to the local x in sub1
            - output is 1

8. Consider the following program written in C syntax and determine all the values of the variables value and list after each of the 3 calls to swap
    - Passed by value
        - After first call - value = 2, list[5] = {1, 3, 5, 7, 9}
        - After second call - value = 2, list[5] = {1, 3, 5, 7, 9}
        - After third call - value = 2, list[5] = {1, 3, 5, 7, 9}
    - Passed by reference
        - After first call - value = 1, list[5] = {2, 3, 5, 7, 9}
        - After second call - value = 2, list[5] = {3, 1, 5, 7, 9}
        - After third call - value = 5, list[5] = {1, 3, 2, 7, 9}

9. Consider program written in C, what are values of list array after execution?
    - Passed by value
        - value of list is {1, 3}
    - Passed by reference
        - value of list is {2, 6}
