# Module 2 homework
## Chapter 3 Problem Set
#### 3. Rewrite the BNF of Example 3.4 to give + precedence over * and force + to be right associative.
```
    <assign> -> <id> = <expr>
    <id> -> A | B | C
    <expr> -> <expr> * <term> | <term>
    <term> -> <factor> + <term> | <factor>
    <factor> -> ( <expr> ) | <id>
```
