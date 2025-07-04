# How JavaScript Works

JavaScript is a **single-threaded**, **non-blocking**, **asynchronous**, and **event-driven** programming language.

It is designed to execute code efficiently in the browser and in server environments (like Node.js) using an **event loop**, **call stack**, and **Web APIs**.

---

##  Core Components of JavaScript Runtime

| Component       | Description                                                                 |
|----------------|-----------------------------------------------------------------------------|
|  Call Stack    | Executes code line-by-line in a LIFO (Last In First Out) manner             |
|  Web APIs      | Browser features (e.g., `setTimeout`, DOM, HTTP requests)                   |
|  Callback Queue | Holds async callbacks waiting for execution                                 |
|  Microtask Queue | Priority queue for promises and mutation observers                         |
|  Event Loop     | Continuously checks and processes stack, microtasks, and macrotasks         |

---

##  Example: Synchronous Execution

```js
console.log("A");
console.log("B");
console.log("C");
