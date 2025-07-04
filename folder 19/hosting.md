#  Hoisting in JavaScript

##  What is Hoisting?

**Hoisting** is JavaScript’s default behavior of **moving declarations** (variables and functions) to the top of their containing scope during the compilation phase before execution.

This means you can use variables and functions **before** they are declared in the code.

---

##  Example 1: Variable Hoisting with `var`

```js
console.log(a); // Output: undefined
var a = 5;
console.log(a); // Output: 5
