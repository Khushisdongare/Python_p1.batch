

# Define the base directory and topic
base_dir = "python_practice"
topic = "1_datatypes"
topic_path = os.path.join(base_dir, topic)
# Create folder structure
os.makedirs(topic_path, exist_ok=True)

# Define README.md content
readme_content = """# Python Datatypes

Python has various built-in datatypes:

### 1. Numeric Types
- `int`: Integer numbers (e.g., `5`, `-3`)
- `float`: Floating-point numbers (e.g., `3.14`, `-0.001`)
- `complex`: Complex numbers (e.g., `2 + 3j`)

### 2. Sequence Types
- `list`: Ordered, mutable collection (e.g., `[1, 2, 3]`)
- `tuple`: Ordered, immutable collection (e.g., `(1, 2, 3)`)
- `range`: Sequence of numbers (e.g., `range(5)`)

### 3. Text Type
- `str`: String (e.g., `"hello"`, `'world'`)

### 4. Set Types
- `set`: Unordered, no duplicates (e.g., `{1, 2, 3}`)
- `frozenset`: Immutable version of set

### 5. Mapping Type
- `dict`: Key-value pairs (e.g., `{"name": "Alice", "age": 25}`)

### 6. Boolean Type
- `bool`: `True` or `False`

### 7. Binary Types
- `bytes`, `bytearray`, `memoryview`

## Example Usage

```python
a = 10              # int
b = 3.14            # float
c = "Hello"         # str
d = [1, 2, 3]       # list
e = (4, 5, 6)       # tuple
f = {7, 8, 9}       # set
g = {"x": 1, "y": 2}# dict
h = True            # bool

print(type(a))  # <class 'int'>
print(type(g))  # <class 'dict'>
