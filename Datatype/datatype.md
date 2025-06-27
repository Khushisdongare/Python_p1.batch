# JavaScript Data Types

Based on: https://www.freecodecamp.org/news/primitive-vs-reference-data-types-in-javascript/

## Primitive Data Types
- String
- Number
- Boolean
- Undefined
- Null
- Symbol
- BigInt

These store single values and are immutable.

```js
let name = "Khushi";
let age = 21;
let isActive = true;
```

## Reference Data Types
- Object
- Array
- Function
- Date

These are mutable and store references (not the actual value).

```js
let arr = [1, 2, 3];
let person = { name: "Khushi", age: 20 };
```

## Key Differences

### Primitive
```js
let a = 10;
let b = a;
b = 20;
console.log(a); // 10
```

### Reference
```js
let obj1 = { val: 1 };
let obj2 = obj1;
obj2.val = 2;
console.log(obj1.val); // 2
```
