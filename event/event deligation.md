# Event Delegation

## What is Event Delegation?

Event delegation is a technique where a single event listener is added to a parent element to manage events for its children.

## Example

```html
<ul id="list">
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<script>
  document.getElementById("list").addEventListener("click", (e) => {
    if (e.target.tagName === 'LI') {
      console.log("Clicked:", e.target.textContent);
    }
  });
</script>
