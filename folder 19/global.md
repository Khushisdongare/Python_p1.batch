#  Global Execution Context in JavaScript

##  What is Execution Context?

An **execution context** is an abstract environment where JavaScript code is evaluated and executed. It contains information about the variables, functions, and the scope chain currently in use.

---

##  Types of Execution Contexts

- **Global Execution Context (GEC)**
- **Function Execution Context (FEC)**
- **Eval Execution Context** (rarely used)

---

##  What is Global Execution Context?

The **Global Execution Context** is the default or base execution context. It is created when your JavaScript program starts running.

It represents the outermost environment and is associated with the **global object**:

- In browsers, the global object is `window`.
- In Node.js, the global object is `global`.

---

##  Creation of Global Execution Context

The GEC has two phases:

1. **Creation Phase**
   - The global object is created (`window` in browsers).
   - The `this` keyword is set to refer to the global object.
   - Variables and functions declared with `var` and function declarations are **hoisted** and added to the global object.
2. **Execution Phase**
   - The code runs line by line.
   - Variables are assigned their values.
   - Functions are executed when called.

---

## Example:

```js
var a = 10;
function greet() {
  console.log('Hello, World!');
}

console.log(a);      // 10
greet();             // Hello, World!
console.log(this);   // Window object (in browser)
