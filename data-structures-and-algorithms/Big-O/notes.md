# Big O
```JavaScript
function addUpTo(n) {
    let total = 0;
    for (let i = 1; i <= n; i++) {
        total += i;
    }
    return total;
}
addUpTo(6);

// another way
function addUpTo2(n) {
    return n * (n + 1) / 2;
}
let t1 = performance.now();
addUpTo(1000000000);
let t2 = performance.now();
console.log(`Time Elapsed: ${(t2 - t1) / 1000} seconds`);
```
- Problem with time
    - different machines will record different times (margins will be different)
    - same machine still records different times
- Count *number* of simple operations the computer has to perform
- 
```JavaScript
function addUpTo2(n) {
    return n * (n + 1) / 2;
}
```
- 3 simple operations (*, +, /) regardless of the size of n

```JavaScript
function addUpTo(n) {
    let total = 0;
    for (let i = 1; i <= n; i++) {
        total += i;
    }
    return total;
}
```
- in this function `total += i` are n additions
- The number of operations grows roughly proportionally with n
- Big O Definition
    - an algorithm is O(f(n)) if the number of simple operations the computer has to do is eventually less than a constant times f(n) as n increases
    - f(n) could be linear -> f(n) = n
    - Quadratic -> f(n) = n^2
    - constant f(n) = 1
    - something entirely different
- `addUpTo2` always has 3 operations even as n grows O(1)
- `addUpTo` number of operations is eventually bounded by a multiple of n -> O(n)
- Arithmetic operations are constant
- Variable assignment is also constant
- Accessing elements in an array (by index) or object (by key) is constant
- In a loop, the complexity is the length of the loop times the complexity of whatever happens inside the loop
## Space complexity
- how much additional memory do we need?
- Focusing on **auxiliary space complexity** which is space by algorithm no space taken up by inputs
- Most primitives (booleans, numbers, undefined, null) are constant space
- Strings require O(n) space (where n is string length)
- Reference types are generally O(n) where n is the length (arrays) or number of keys (objects)
```JavaScript
let total = 0;
for (let i = 0; i < arr.length; i++) {
    total += arr[i];
}
return total;
}
```
- total and the i in loop takes space
- Not adding any other variables so that is constant space
```JavaScript
function double(arr) {
    let newArry = [];
    for (let i = 0; i < arr.length; i++) {
        newArr.push(2 * arr[i]);
    }
    return newArr;
}
```
- Creating a new element proportionate to the length of array so its O(n)
## Logarithms
- log,2 (8) = 3
- log base 2 of 8 
- 2 to what power = 8
- log, 2 (value) = exponent
- 2 ^ exponent = value
- The logarithm of a number roughly measure the number of times you divide that number by 2 before you get a values thats less than or equal to 1
- Logarithmic time complexity is great
## Objects
- Fast access / insertion and removal
- Times
    - Insertion - O(1)
    - Removal - O(1)
    - Searching - O(n)
    - Access - O(1)
- Methods
    - Object.keys - O(n)
    - Object.values - O(n)
    - Object.entries - O(n)
    - hasOwnProperty - O(1)
## Arrays
- Timing
    - Insertion... depends
    - Removal... depends
    - Searching - O(n)
    - Access -> O(1)
- Buil-in array methods
    - push / pop - O(1)
    - shift / unshift - O(n)
    - sort - O(n * log n)
    - forEach/map/filter/reduce/etc.. - O(n)
