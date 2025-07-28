# Exception Handling in Python

- Exception handling allows you to manage errors gracefully and write more robust and fault-tolerant code.

## 🔹 What is an Exception?

- An **exception** is an error that occurs during program execution. Python provides a way to catch and handle these errors using `try`, `except`, `else`, and `finally` blocks.

---

## 🔹 Basic Syntax

```python
try:
    # Code that might raise an exception
except SomeException:
    # Code that runs if an exception occurs
else:
    # Code that runs if no exception occurs
finally:
    # Code that always runs, whether an exception occurred or not
