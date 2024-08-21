# Week 1 notes
### Coding standards
- Docstring and comments are crucial
- Max line length: 79 characters
- Add python type hints
- always use virtual envs
- Never upload with the virtual env files
- use the 'time' package to time algorithms
### Algorithm Review
- Input's size
    - size of the input value (number of input items; the bit size of the input value)
- Basic operation
    - operation that contributes the most to the running time of the algorithm
- T(n) = C<sub>op</sub> * C(n)
- T(n) -> running time of an algorithm
- C<sub>op</sub> -> execution time for the basic operation
- C(n) -> number of times the basic operation is executed
- Runnning time analysis of the Insertion sort
    - `while i > 0 and A[i] > key`
    - the basic operation run the most / most important is the A[i] > key because it contributes to the logic of the algorithm
- When we want to choose the basic operation that contributes to the runtime
- O-notation (Big-O): an asymptotic upper bound for a function
- Big-Omega: an asymptotic lower bound for a function
- Big-Theta: an asymptoticly tight bound for a function

