# Event Capturing

## What is Event Capturing?

Event capturing is a phase of event propagation in the DOM where the event starts from the root element and propagates down to the target element.

## Example

```html
<div id="parent">
  <button id="child">Click Me</button>
</div>

<script>
  document.getElementById("parent").addEventListener("click", () => {
    console.log("Parent Clicked");
  }, true); // Capture phase

  document.getElementById("child").addEventListener("click", () => {
    console.log("Child Clicked");
  }, true); // Capture phase
</script>
