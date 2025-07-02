# Event Bubbling

## What is Event Bubbling?

Event bubbling is a phase where the event starts at the target element and bubbles up through its ancestors.

## Example

```html
<div id="parent">
  <button id="child">Click Me</button>
</div>

<script>
  document.getElementById("parent").addEventListener("click", () => {
    console.log("Parent Clicked");
  });

  document.getElementById("child").addEventListener("click", () => {
    console.log("Child Clicked");
  });
</script>
