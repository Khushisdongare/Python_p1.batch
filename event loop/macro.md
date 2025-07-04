# Macrotasks in JavaScript

##  What Are Macrotasks?

**Macrotasks** are asynchronous tasks queued in the **task queue** (also known as the **macrotask queue**) and executed **after the current call stack** is empty and **after all microtasks have been processed**.

---

##  Common Examples of Macrotasks

- `setTimeout`
- `setInterval`
- `setImmediate` (Node.js only)
- I/O events
- UI rendering tasks

---

## Event Loop & Macrotasks

1. JavaScript starts by running synchronous code.
2. Then it processes **all microtasks** (e.g., `Promise.then`, `queueMicrotask`).
3. Then it processes the **first macrotask** in the queue.
4. Repeats the cycle.

---

##  Example 1: setTimeout as a Macrotask

```js
console.log('Start');

setTimeout(() => {
  console.log('Inside setTimeout');
}, 0);

console.log('End');
