#  Primitive vs Reference Data Types in JavaScript

*Source: [freeCodeCamp: Primitive vs Reference Data Types in JavaScript](https://www.freecodecamp.org/news/primitive-vs-reference-data-types-in-javascript/)*

---

## 🧠 Overview

JavaScript divides data types into two main categories:

- **Primitive data types**  
- **Reference data types** :contentReference[oaicite:1]{index=1}

---

## 1. Primitive Data Types

Primitives are simple, immutable, and stored **directly in the stack**. They aren’t objects and don’t have methods—though JavaScript temporarily boxes some primitives (like strings) to provide methods :contentReference[oaicite:2]{index=2}.

**Examples:**
```js
let num = 42;
let str = "hello";
let bool = true;
let nothing = null;
let undef;


