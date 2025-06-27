# Primitive vs Reference Data Types in JavaScript

## 🔹 Overview
JavaScript data types are categorized into **primitive** and **reference** types. They differ in how they are stored and how variable assignments affect them.

---

## 1. Primitive Data Types 🧱

- **directly on the stack**.
- Copying a primitive creates a **new value**, not a reference.

## 🔗 Reference Data Types

More complex data stored on the **heap**.

Variables store a **reference (pointer)** to the actual data.

### Types include:
- `Object`
- `Array`
- `Function`

### Example:
```js
let obj1 = { name: "khushi", age: 20 };
let obj2 = obj1;
obj1.age = 20;

console.log(obj2.age); // 20


