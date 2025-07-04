#  Callbacks in JavaScript

##  What Is a Callback?

A **callback** is a function passed as an argument to another function to be **executed later**, either **synchronously** or **asynchronously**.

---

##  Why Use Callbacks?

- To handle **asynchronous** operations (e.g., reading a file, making an API call)
- To allow **custom behavior** to be defined in function parameters
- To enable **reusability** and **functional composition**

---

##  Example 1: Synchronous Callback

```js
function greet(name, callback) {
  console.log('Hello, ' + name);
  callback();
}

function sayBye() {
  console.log('Goodbye!');
}

greet('Alice', sayBye);
