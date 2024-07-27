# Chapter 11
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

