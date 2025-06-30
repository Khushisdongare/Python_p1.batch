// Select all button elements
const buttons = document.querySelectorAll('button');

// Loop through buttons and add click event listeners
for (let i = 0; i < buttons.length; i++) {
  buttons[i].addEventListener('click', function () {
    // Log the button text and its index (starting from 1)
    console.log(`You clicked button ${i + 1}: ${this.textContent}`);
  });
}
