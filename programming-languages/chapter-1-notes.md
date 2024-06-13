# Chapter 1<br>
## 1.1 - Reasons for studying concepts<br>
    - Increased capacity to express ideas
    - Improved background for choosing appropriate languages
    - Increased ability to learn new languages
    - Better understanding of the significance of implementation
    - Better use of languages that are already known
    - Overall advancement of languages that are already known
## 1.2 - Programming Domains<br>
    - Scientific applications
        - Fortran was widely used
            - applications at that time had relatively simple data structures (arrays and matrices)
            - large numbers of floating-point arithmetic
            - control structures were counting loops and selections
    - Business applications
        - COBOL
            - produces elaborate reports
            - precise ways of describing and storing decimal numbers and character data with ability to specify decimal arithmetic operations
    - Artifical Intelligence
        - LISP used to be widely used for this but now Python has taken over
    - Web Software
        - supported by an ecletic collection of languages (JS, PHP, Java, etc...)
## 1.3 - Language Evolution Criteria
    - 3 main criteria
        - Readability
        - Writability
        - Reliability
    ### Readability
        - Before 1970 code was focused on efficiency and more from the machine orientation than user orientation
        - Overall simplicity strongly affects its readability
        - Complicating characteristic of programming languages is *feature multiplicity* having more than one way to accomplish a particular operation
        - **Operator overloading** a single operator can have more than one meaning. Although often useful can lead to reduced readability
        #### Orthogonality
            - Means a relatively small set of primitive constructs can be combined in a relatively small number of ways to build the control and data structures of the language
        #### Syntax Design
            - has significant effect on the readability
            - Special (reserved) key words
            - Form and meaning: design statements so their appearance indicates their usages
    ### Writability
        - how easily a language can be used to create programs for a chosen problem domain
        - **Type Checking** important factor in reliability
        - **Exception Handling** intercept run-time errors, make corrections, and then continue
        - **aliasing** two or more distinct names to access same memory call (dangerous) 
