# Chapter 3
## 3.1 - Introduction
- **Syntax** is the form of languages expressions, statements, and program units
- **Semantics** the meaning of those expressions, statements, and program units
- Example the syntax of a Java `while` statement is:
    ```java
    while (boolean_expression) statement
    ```

- Semtantics is when value of boolean_expression is `true`, statement is executed. Control implicitly returns to the Boolean expression
to repeat the process. If control of Boolean expression is false, control transfers to statement following `while` construct.

## 3.2 - General Problem of Describing Syntax
- **Sentences** or **statements** the string of characters over some alphabet
- **language** set of sentences
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
- Language generator is a device used to generate sentences of a language

## 3.3 - Formal Methods of Describing syntax
- **grammars** formal language-generation mechanisms commonly used to define syntax of programming languages
- Forms of the tokens of programming languages can be described by regular grammars
- Syntax of whole programming languages, with minor exceptions, can be described by context-free grammars
- **Backus-Naur Form (BNF)** natural notation for describing syntax created by John Backus for ALGO 58 and later modified by Peter Naur for ALGO 60
- Still the most popular method to concisely describe programming language syntax
- Context-free grammars are referred to as grammars and interchangably used with BNF
- ### Fundamentals
    - **metalanguage** language used to describe another language. BNF is a metalanguage for programming languages
    - BNF uses abstraction for syntactic structures
    - A simple Java statement might be represented by the abstraction `<assign>`
    - Actual definition of `<assign>` can be given by:
        ```
        <assign> -> <var> = <expression>
        ```
    - `->` means **is defined as**
    - Text on left of `->` is **left-hand side (LHS)** is the abstraction being defined
    - Text to the right of arrow is **the definition of the LHS** called **right-hand side (RHS)**
        - **RHS** consists of a mixture of tokens, lexemes, and references to other abstractions
    - Altogether this is called a **production rule**
    - In the above rule the abstractions `<var>` and `<expression>` must be defined for the `<assign>` definition to be useful
    - That particular rule specifies that the abstraction `<assign>` is defined as an instance of the abstraction
        `<var>` the lexeme `=` followed by the abstraction `<expression>`
    - One example sentence whose syntactic structure is described by the rule is:
        ```
        total = subtotal1 + subtotal2
        ```
    - The abstractions in an BNF description, or grammar, are often called **nonterminals**
    - The lexemes or tokens of the rule are called **terminals**
    - A BNF description, or grammar, is a collection of rules
    - **Nonterminals** can have two or more distinct definitions representing two or more possible syntactic forms in the language
    - Multiple definitions can be written with a single rule using ` | ` which is `logical OR`
        ```
        <if_stmt> -> if ( <logic_exp) > <stmt> | if ( <logic_exp> ) <stmt> else <stmt>
        ```
    - In these rules `<stmt>` represents either a single or compound statement
- ### Describing Lists
    - A rule is **recursive** if its LHS appears in its RHS
        ```
        <ident_list> -> identifier | identifier, <ident_list>
        ```
- ### Grammars and Derivations
    - A grammar is a generative device for defining languages
    - Sentences of the language are generated through a sequence of applications of the rules, beginning with a special nonterminal of the grammar called **start symbol**
    - The sequence of rule applications is called a **derivation** 
    - Each of the strings in a derivation is called **sentential form**
    - **Lefmost derivations** replace the leftmost nonterminal in the sentential form
        - derivations may be leftmost, rightmost, or an order that is neither
        - this can generate different sentences of the language
        - Example of a leftmost derivation:
            ```
            <program> => begin <stmt_list> <end>
                      => begin <stmt> ; <stmt_list> <end>
                      => begin <var> = <expression> ; <stmt_list> <end>
            ```
        - `=>` is read **derives**
- ### Parse Trees
    - One of most attractive features of grammars is they naturally describe the hierarchical syntactic structure of the sentences of the languages they define
    - Every node is labeled with a **nonterminal** every leaf is labeled with a **terminal**
- ### Ambiguity
    - A grammar that generates a sentential form for which there are two or more distinct parse trees is **ambiguous**
    - if a grammar generates a sentence with more than one leftmost derivation or more than one rightmost derivation then it is ambiguous
- ### Operator Precedence
    - An operator generated lower in the parse tree has to be evaluated first and therefore has precedence
    - **Associative predence** When a grammar rule has its LHS also appearing at the beginning of its RHS then it is **left recursive** and has left associativity

## 3.4 Attribute Grammars
- used to describe more of the structure of the programming language than can be defined with context-free grammar
- allows certain language rules to be conveniently described, such as type compatibility
- the size of the grammar determines the size of the syntax analyzer
- Example of a rule that cannot be described with BNF is a variable that must be declared before being referenced
- **Static Semantics** is only indirectly related to the meaning of programs during execution
- named so because the analysis required to check these specifications can be done at compile time
- **Attributes** are associated with grammar symbols (terminals and nonterminals) and are similar to variables in that they can have values assigned to them
- **Attribute computation functions** (semantics functions) are used to specify how attribute values are computed
- **Predicate functions** state the static semantic rules of the language and are associated with grammar rules
- **Synthesized attributes** are used to pass syntactic information up a parse tree
- **Inherited attributes** pass syntactic information down and across the parse tree

