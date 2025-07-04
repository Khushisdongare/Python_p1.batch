#  JavaScript Event Loop Practice

##  What is the Event Loop?

The **Event Loop** is a fundamental concept in JavaScript that allows asynchronous operations like `setTimeout`, `fetch`, and Promises to work. It coordinates the **call stack**, **Web APIs**, **callback queue**, and **microtask queue**.

---

## Components of the Event Loop

- **Call Stack**: Where functions are executed.
- **Web APIs**: Provided by the browser (e.g., `setTimeout`, DOM events).
- **Callback Queue (Macrotasks)**: Queued functions from `setTimeout`, `setInterval`, etc.
- **Microtask Queue**: Queued functions from Promises and `queueMicrotask`.

---

##  Example 1: Basic `setTimeout`

```js
console.log('Start');

setTimeout(() => {
  console.log('Timeout callback');
}, 0);

console.log('End');
