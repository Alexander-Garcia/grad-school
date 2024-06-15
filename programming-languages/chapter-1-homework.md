# Module 1 homework<br>
## Chapter 1 Review Questions
#### 7. What is the disadvantage of having too many features in a language?
Too many features in language strong affects its readability. A language with a large number of features is more difficult to learn than a language with a smaller number.
This also leads to programmers learning a smaller subset of the language and ignoring other features.

#### 8. How can user-defined operator overloading harm the readability of a program?
The issue with user-defined operator overloading is that a user might not overload sensibly. This ambiguity may create issues with readability. For example, if a user
defines + between single-dimenisoned arrays to mean the sum of all elements in both arrays, this differs from usual vector addition. Doing so could cause confusion in both the author and program's readers.

## Chapter 1 Problem Set
#### 8. Many languages distinguish between uppercase and lowercase letters in user-defined names. What are the pros and cons of this design decision?
I primarily write JavaScript for work which does distinguish between uppercase and lowercase in user-defined names. This flexiblity allows for a greater combination of variable and function names.
However, a con is that a variable defined `someVar` is different than `SomeVar` even though they are the same words. If overlooked a programmer might unintentionally use the wrong variable
or function name. A pro for this is one used in the React framework in which components are named starting with an uppercase letter `SomeComponent`. This is a pro because as soon as a programmer
notices this uppercase format they understand immediately that it is a component instead of a normal variable or function.

## Chapter 2 Review Questions
#### 2. What two common data structures were included in Plankalkul?
The simplest data type was the single bit, but built on top of the single bit were integer and floating point types.
It also included arrays and records of which records could aslo be nested.

#### 5. Why was the slowness of interpretation of programs acceptable in the early 1950s?
This slowness in interpretive systems was tolerated because the lack of floating-point hardware in available computers. Floating-point operations
had to be simulated in software which was a very time consuming process. This time consuming process meant the overhead of interpretation was relatively insignificant and
an accetpable expense.

## Chapter 2 Problem Set
#### 1. What features of Plankalkul do you think would have had the greatest influence on Fortran 0 if the Fortran designers had been familiar with Plankalkul?
Given some of Plankalkul's most advanced features were in its data structures those would have had the greatest influence on Fortran 0. Although systems had floating-point
simulation in software there was no mention of arrays and records until Laning and Zierler which wasn't in usable from until May 1953. Given the work of Laning and Zierler never
escape MIT, even though it preceded Fortran, Plankalkul's implementation of these data structures would have had great influence.

