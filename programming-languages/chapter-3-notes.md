# Chapter 3
## 3.1 - Introduction
- **Syntax** is the form of its expressions, statements, and program units
- **Semantics** the meaning of those expressions, statements, and program units
- Example the syntax of a Java `while` statement is:
    ```java
    while (boolean_expression) statement
    ```

- Semtantics is when value of boolean_expression is `true`, statement is executed. Control implicitly returns to the Boolean expression
to repeat the process. If control of Boolean expression is false, control transfers to statement following `while` construct.

## 3.2 - General Problem of Describing Syntax
- **Sentences** or **statements** the strings of a language
- **Lexemes** include its numeric, literals, operators, and special words.
    - think of programs as strings of lexemes rather than characters
- **Token** category of its lexemes
- Consider following Java statement:
    ```java
    index = 2 * count + 17;
    ```
- The **lexemes** and **tokens** are
| Lexemes | Tokens      |
| :---:   | :---:       |
| index   | identifier  |
| =       | equal_sign  |
| 2       | int_literal |
| *       | mult_op     |
| count   | identifier  |
| +       | plus_op     |
| 17      | int_literal |
| ;       | semi-colon  |

- Languages can be defined in two distinct ways: **recognition** and **generation**
- The syntax analysis part of a compiler is a **recognizer** for the language the compiler translates
