#  Microtasks in JavaScript

##  What Are Microtasks?

**Microtasks** are asynchronous callbacks that are executed **immediately after the current synchronous code** and **before any macrotask** (like `setTimeout`) is run.

---

## Common Microtask Sources

- `Promise.then()`, `.catch()`, `.finally()`
- `queueMicrotask()`
- `MutationObserver` (in the browser)

---

## Event Loop and Microtasks

The **event loop** follows this order:

1. Execute all synchronous code in the **call stack**
2. Execute **all microtasks**
3. Then pick and run **one macrotask**
4. Repeat the cycle

---

## Example 1: Promise Microtask

```js
console.log('Start');

Promise.resolve().then(() => {
  console.log('Microtask');
});

console.log('End');
