# JavaScript Strings and String Methods

## What is string?
"I"n JavaScript, a string is a sequence of characters used to represent text. Strings are one of the primitive data types in JavaScript."

## Creating Strings
```js
let str1 = "Hello";
let str2 = 'World';
let str3 = `Hello, ${str2}`;
```

## Common String Methods

- `length`
- `toUpperCase()`, `toLowerCase()`
- `includes()`
- `indexOf()`
- `slice()`, `substring()`
- `replace()`
- `split()`
- `trim()`

### Examples
```js
let str = "  Hello JavaScript!  ";
console.log(str.trim().toUpperCase()); // "HELLO JAVASCRIPT!"
console.log(str.includes("JavaScript")); // true
```
