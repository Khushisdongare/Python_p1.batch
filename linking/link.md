# Four Ways of Linking JavaScript Files 

## 1. External JavaScript File (at the bottom of body)

Recommended way to load JS without blocking HTML rendering.

```html
<body>
  <script src="script.js"></script>
</body>
```

---

## 2. External JavaScript File with `defer` (in head)

Loads script in background and executes after HTML parsing.

```html
<head>
  <script src="script.js" defer></script>
</head>
```

---

## 3. Inline JavaScript (Internal Script)

JavaScript code written directly inside the HTML using `<script>`.

```html
<body>
  <script>
    console.log("Inline JavaScript Example");
  </script>
</body>
```

---

## 4. Event-Driven Linking (e.g., onClick handler)

Call JavaScript via HTML attributes like `onclick`, `onload`.

```html
<button onclick="sayHello()">Click Me</button>

<script>
  function sayHello() {
    alert("Hello from JavaScript!");
  }
</script>
```
