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
    - 

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
            - 5 + (3 * (14) - 1)
            - 5 + (42 - 1)
            - 5 + 41
            - 46
        - Sum2
            - fun(10) + (10 / 2)
            - ((3 * 14) - 1) + (10 / 2)
            - (42 - 1) + (10 / 2)
            - (41 + 10) / 2)
            - 51 / 2
            - 25.5
    - Operands in expressions are evaluated right to left?
        - Sum1
            - (10 / 2) * fun(10)
            - (10 / 2) * (3 * (14 - 1))
            - (10 / 2) * (3 * 13)
            - 10 / (2 * 39)
            - 10 / 78
            - 0.128
        - Sum2
            -  fun(10) + (10 / 2)
            - (3 * 14 - 1)
