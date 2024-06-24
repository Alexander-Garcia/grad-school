# Module 2 homework
## Chapter 3 Problem Set
### 3. Rewrite the BNF of Example 3.4 to give + precedence over * and force + to be right associative.
```
    <assign> -> <id> = <expr>
    <id> -> A | B | C
    <expr> -> <expr> * <term> | <term>
    <term> -> <factor> + <term> | <factor>
    <factor> -> ( <expr> ) | <id>
```

### 6. Part B. Using grammar in Example 3.2 show a parse tree and a leftmost derivation for each of the following statements.
- b.) `B = C * (A * C + B)`
#### Leftmost derivation
```
    <assign> => <id> = <expr>
             => B = <expr>
             => B = <id> * <expr>
             => B = C * <expr>
             => B = C * ( <expr> )
             => B = C * ( <id> * <expr> )
             => B = C * ( A * <expr> )
             => B = C * ( A * <id> + <expr> )
             => B = C * ( A * C + <expr> )
             => B = C * ( A * C + <id> )
             => B = C * ( A * C + B )
```
#### Parse Tree
```
            <assign>
            /   |   \
        <id>    =    <expr>
          |         /   |   \
          B       <id>  *    <expr>
                   |       /   |   \
                   C      (  <expr>  )
                            /   |   \
                          <id>  *   <expr>
                            |       /   |   \
                            A     <id>  +    <expr>
                                   |           |
                                   C          <id>
                                               |
                                               B
```
### 7. Part A. Using grammar in Example 3.4 show a parse tree and a leftmost derivation for each of the following statements.
- a.) `A = (A + B) * C`
#### Leftmost derivation
```
    <assign> => <id> = <expr>
             => A = <expr>
             => A = <term>
             => A = <term> * <factor>
             => A = <factor> * <factor>
             => A = ( <expr> ) * <factor>
             => A = ( <expr> + <term> ) * <factor>
             => A = ( <term> + <term> ) * <factor>
             => A = ( <factor> + <term> ) * <factor>
             => A = ( <id> + <term> ) * <factor>
             => A = ( A + <term> ) * <factor>
             => A = ( A + <factor> ) * <factor>
             => A = ( A + <id> ) * <factor>
             => A = ( A + B ) * <factor>
             => A = ( A + B ) * <id>
             => A = ( A + B ) * C
```
#### Parse Tree
```
            <assign>
            /   |   \
        <id>    =    <expr>
          |            |
          A          <term>
                    /   |   \
                <term>  *    <factor>
                   |             |
                <factor>        <id>
               /   |   \         |
             (   <expr>  )       C
                /   |   \
            <expr>  +    <term>
              |            |
            <term>       <factor>
              |            |
            <factor>       <id>
              |             |
             <id>           B
              |
              A
```
### 12. Consider the following gramar:
```
    <S> -> a<S>c<B> | <A> | b
    <A> -> c<A> | c
    <B> -> d | <A>
```
The grammar can generate the following: a. "abcd" and e. "accc"

### 15. Convert the BNF of Example 3.1 to EBNF
```
    <program> -> begin <stmt_list> end
    <stmt_list> -> <stmt> { ( ; ) <stmt> }
    <stmt> -> <var> = <expression>
    <var> -> A | B | C
    <expression> -> <var> { ( + | - ) <var> }
```

### 17. Convert the follow EBNF to BNF:
#### EBNF
```
    S -> A {bA}
    A -> a[b]A
```

#### BNF Form
```
    S -> A | bA
    A -> aA | abA
```

### 23. Compute the weakest precondition for each of the following assignment statements and postconditions:
- a.) `a = 2 * (b - 1) - 1 {a > 0}`
To find weakest precondition substitute `2 * (b - 1) - 1` in the postcondition `{ a > 0 }` and solve which gives `{ b > 3/2 }` as weakest precondition

- b.) `b = (c + 10) / 3 {b > 6}`
To find weakest precondition substitue `(c + 10) / 3` in the postcondition `{ b > 6 }` and solve which gives `{ c > 8 }` as weakest precondition
