# Final Exam Notes
- 12.1 - 12.3 & 12.5
## video lecture notes
- Subprogram call and return operations of a language are together called its **subprogram linkage**
- General semantics of calls to a subprogram
    - Parameter passing methods
    - Stack-dynamic allocataion of local variables
    - save execution status of calling program
    - Transfer control and arrange for the return
    - If subprogram nesting is supported, access to nonlocal variables must be arranged
- General semantics of suprogram returns
    - In mode and inout mode parameters must have their values returned
    - Deallocation of stack-dynamic locals
    - Restore execution of the status
    - Return control to the caller
- Implementing simple subprograms
    - Simple subprograms have only static local variables and nesting subprograms is not allowed
- Call semantics:
    - save execution status of the caller
    - pass parameters
    - pass return address to called
    - transfer control to the called
- Return semantics:
    - if pass-by-value-result or out mode parameters are used, move current values of those parameters to their corresponding actual parameters
    - if it is a function, move the functional value to a place the caller can get it
    - restore the execution status of the caller
    - transfer control back to the caller
- restore execution can be done by either caller or the called
- The first, second, and fourth actions of return semantics must be done by the called not the caller
- Linkage actions of the called can occur at two different times
    1. prologue at the beginning of execution
    2. epilogue at the end.
- in case of simple subprogram all of the linkage actions of the callee occur epilogue, no need for prologue
- Required storage: status information, parameters, return address, return value for functions, temporaries
- simple subprogram consists of 2 separate parts:
    1. actual code of the subprogram which is constant
    2. and local variables and datat listed previously which can change when subprogram is executed
- format or layout of non-code part of executing a subprogram is called activation record
- **activation record instance (ARI)** is a concrete example of an activation record (collection of data for a particular subprogram activation)
- Simple subprograms do not support recursion, there can be only one active version of a given subprogram at a time
- 3 fields of AR (read from bottom to top like a stack)
    3. Local Variables
    2. Parameters
    1. Return Address
- Saved execution status of caller is omitted
- Activation record format is static, but its size may be dynamic
- **dynamic link** points to the base of an instance of the activation record of the caller
- An activation record instance is dynamically created when a subprogram is called
- AR record instances reside on the run-time stack
- Environment Pointer (EP) must be maintained by the run-time system. It always points at the base of the activation record instance of the currently executing program unit
- Example
    - local variables
    - parameters
    - dynamic link
    - return address
- Revised semantic call / return actions
    - Caller Actions:
        - create an activation record instance
        - save execution status of the current program unit
        - compute and pass parameters
        - pass the return address to the called
        - transfer control to the called
    - Prologue actions of the called
        - save old EP in the stack as the dynamic link and create new value for EP
        - allocate local variables
    - Epilogue actions of the called
        - if there are pass-by-value-result or out-mode parameters, the current values of those parameters are moved to the corresponding actual paramters
        - if subprogram is a function, its value is moved to a place accessible to the caller
        - Restore stack pointer by setting it to teh value of teh current EP -1 and set the EP to old dynamic link
        - restore execution status of the caller
        - transfer control back to the caller
- Collection of dynamic links in the stack at a given time is called dynamic chain, or call chain
- Local variables can be accessed by their offset from the beginning of the AR, whose address is in EP. Called local_offset
- local_offset of a local variables can be determined by compiler at compile time
- Recursion ARI
    - Additional entry for teh return value of the function
        - Functional value
        - Parameter
        - dynamic link
        - Return to address
- All variables that can be non-locally accessed reside in some activation record instance in the stack
- The process of locating a non-local reference:
    - Find correct activation record instance
    - determine the correct offset within that activation record
- Static chains
    - static link (static scope pointer) is added to AR
- Static scoping
    - static chain is a chain of static links that connects certain activation record instances
    - static link in an activation record instance for subprogram A points to one of the activation record instances of A's static parent
    - static chain from an activation record instance connects it to all of its static ancestors
    - static_depth is an integer associated with a static scope whose value is the depth of nesting of that scope
    - chain_offset or nesting_depth of a nonlocal reference is the difference between the static_depth of the reference and taht of the scope when it is declared
    - reference to a variable can be represented by the pair (chain_offset, local_offset)
- ARI for static scoping
    - Local
    - Parameter
    - Dynamic link (points to caller)
    - Static link (points to ARI of static parent where it is defined)
    - return address
- Static chain maintenance
    - At the call:
        - ARI must be built
        - dynamic link is just ol dstack top pointer
        - static link must point to most recent ARI of static parent
        - Static semantics error occurs when variable can't be found when searching the Static ancestors ARIs
- Evaluation of static chains
    - Problems
        - nonlocal reference is slow if nesting depth is large
        - Time-critical code is difficult
            - costs of nonlocal references are difficult to determine
            - code changes can change the nesting depth and therefore the cost
- number of languages provide for user-specified local scopes for variables called blocks.
- every block has an AR and an instance is created every time the block is executed
### Chapter 11
- abstraction is a view or representation of an entity that includes only the most significant attributes
    - a weapon against the complexity of programming; its purpose is to simplify the programming process
    - effective because it allows programmers to focus on essential attributes, while ignoring subordinate attributes
- 3 major characteristics of object-oriented programming languages:
    - abstract data types
    - inheritance
    - polymorphism (dynamic binding of messages to method defintions)
- **abstraction** is a view or representation of an entity that includes only the most significant attributes
- 1960 COBOL had record data structure
- C based languages have structs which are also records
- An abstract data type is a data structure, in the form of a record, but which includes subprograms that maniuplate data
- Abstract data type is a user defined data type that satisfies two conditions
    1. representation of objects of the type is hidden from program units that use these objects, so the only operations possible are those provided in types definition
    2. declarations of the type and the protocols of the operations on objects of the type ar eocntianed in a single syntactic unit
        - other program units are allowed to create variables of the defined type
- Advantages of condition 1
    - reliability by hiding data representations, user code cannot directly access objects of type or depend on representation
        - allows the representation to be changed without affecting user code
    - reduces range of code and variables of which the programmer must be aware
    - name conflicts are less likely
- advantages of condition 2
    - provides a method of program organization
    - aids modifiability (everything associated with a data structure is together)
    - separate compilation
- getters and setters
    - allow clients indirect access to the so called hidden data
    - better solution than simply making the data public
- 3 reasons why accessors are better
    1. read-only access can be provided, by having a getter method but no corresponding setter method
    2. contraints can be included in setters
        - if data value shoudl be restricted to a particular range, setter can enforce that
    3. actual implementation of data member can be changed withotu affecting clients if getters and setters are the only access
- specifying data in an abstract data type to be public and providing accessor methods for that data are violations of the principles of abstract data types
## 11.3 Design issues for abstract data types
- syntactic unit in which to encapsulate the type defintion
- a method of making type names and subprogram headers visible to clients, while hiding actual definitions
- some primitive operations must be buit into the language processor
## 11.4 language examples (C++, java, C#)
- class is the encapsulation device
- A class is a type
- All of the class instances of a class share a single copy of the member functions
- each instance of a class has its own copy of the class data members
- instances can be static, stack dynamic, or heap dynamic
- if static or stack dynami, they are referenced directly through value variables
    - lifetime of a stack-dynamic instance of a class ends when the end of a scope of its declaration is reached
- heap-dynamic instances are referenced through pointers    
    - created with new operator and destroyed with delete operator
- Member function can be defined in two ways
    1. complete definition may appear in the class (implicityly inlined)
    2. Only a header, then complete definition appears outside a class and is separately compiled
- infromation hiding
    - private clause for hidden entities
    - public clause for interface entities
    - protected clause for inheritance
- Constructors
    - functions to initialize data members of instances (they do not create the objects)
    - may also allocated storage if part of the object is heap-dynamic
    - can include parameters to provide parameterization of the objects
    - implicitly called when an instance is created
    - can be explicitly called
    - name is the same as the class name
    - Can be overloaded
    - No return type
- Destructors
    - functions to cleanup after an instance is destoryed; usually just to reclaim heap storage
    - implicitly called when the objects lifetime ends
    - can be explictly called
    - name is teh calss name preceded by a ~
    - Return type -> No
    - Parameters -> No
- Java
    - all user-defined types are classes
    - all objects are allocated from the heap and accessed through reference variables (no pointers in java)
    - individual entities in classes have access control modifiers (private or public) rather than clauses
    - implicit garbage collection of all objects
    - java has a second scoping mechanism, package scope, which can be used in place of friends
        - all entities in all classes in a package that do not have acecss control modifiers are visible throughout the package
    - encapsulation -> methods must be defined completely in a class; a method body must appear with its corresponding method header
        - java abstract type is both declared and defined in a single abstract syntactic unit
- C#
    - includes both classes and structs
    - all class instances are heap dynamic
    - default constructors are available for all classes
    - garbage collection is used for most heap objects, so destructors are rarely used
    - Information hiding
        - default access modifier for a class is private, wheras for a struct its public
        - adds 2 access modifiers, internal and protected internale
        - to access data members -> getter and setter
        - provides properties as a way of implementing getters and setters without requiring explicit method calls (inherited from Delphi)
## 11.5 parameterized abstract data types
- parameterization of abstract data types allows designing an ADT that can store any type of element
- parameterized ADTs are also known as generic classes
- c++, java 5.0, and C# 2005 provide support for parameterized ADTs
- parameterized classes Java
    - LinkedList and ArrayList
    - collection types are able to store multiple types (as long as they are classes)
    - introduction of generic classes solved some previously existed issues, such as:
        - eliminated need to cast objects that are removed
        - eliminated problem of having multiple types in a structure
    - wildcard classes, which allows to specify a range of types (within inheritance hierarchy) that may be used in a code

## 12.2 OOP
- productivity increases can come from reuse
    - Abstract Data Types (ADTs) are difficult to reuse - always need changes
    - All ADTs are indepenedent and at the same level
- Inheritance allows new classes defined in terms of existing onees
    - allows them to inherit common parts
- Inheritance addresses both of the above concerns
    - reuse ADTs after minor changes and define classes in a hierarchy
- ADTs are usually called **classes**
- Class instances are called **objects**
- A class that inherits is a **derived class* or **subclass** or **child class**
- Class from which another class inherits is a base class, superclass, or parent class
- subprograms that define operations on objects are called methods
- calls to methods are called messages
- entire collection of methods of an object is called its message protocol or message interface
- messages have 2 parts
    - method name
    - destination object
- How is passing methods different from calling subprograms
    - methods have access to data members defined in same class
        - from this POV they are similar to global variables for subprograms
- Inheritance can be complicated by access control to encapsulated entities:
    - class can hide entities from its subclass
    - from its clients
    - from its clients while allowsing its subclasses to see them
- Besides inheriting a method as is a class can modify an inherited method
    - new one overrides inherited one
    - method in the parent is said to be overriden
- 3 ways a class can differe from its parent
    - subclass can add variables and / or methods to those inherited from the parent
    - subclass can modify behavior of one or more of its inherited methods
    - parent class can define some of its variables or methods to have private access, which means they will not be visible in subclass
- 2 kinds of variables in a class
    - class variables - one per class
    - instance variables - one per object
- 2 kinds of methods in a class
    - class methods -> accept messages to the class
    - instance methods -> accept messages to objects
- Disadvantage of inheritance for reuse
    - creates interdependencies among classes that complicate maintenance
- Polymorphism
    - provided by the dynamic binding of messages to method definitions is sometimes called **dynamic dispatch**
- Polymorphic variables can be defined in a class that is able to reference (or point to) objects of the class and objects of any of its descendants
## object allocation and deallocation
- Is deallocation explicit or implicit?
    - issue of dangling pointers or references
- From where are objects allocated?
    - If they behave like ADTs, they be allocated from anywhere
- Explicitly created on heap (via new)
    - if they are all heap-dynamic, references can be uniform through a pointer or reference variable
        - dereferencing can be implicit -> simplifies syntax
    - allocated from run-time stack
        - problem with regard to subtypes -> object slicing
- Dynamic and static binding
    - Should all binding of messages to methods be dynamic?
        - if none are, you lose advantages of dynamic binding
        - if all are it is inefficient
    - Alternative is to allow the user to specify whether binding should be static or dynamic
- Nested classes
    - one of the primary motivations for nesting class definitions is information hiding
        - if a new class is needed by only one class, there is no reason to define it in such a way that it can be seen by other classes
    - Can new class be nested insided the class that uses it?
    - in some cases the new class is nested inside a subprogram rather than directly in another class
- other issues
    - which facilities of the nesting class should be visible to the nested class and vice versa
- Initialization of  objects
    - are objects initialized to values when they are created?
        - implicit or explicit initialization