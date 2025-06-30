// Function for Way 1 (inline)
function handleInlineClick(button) {
  console.log("Way 1 clicked");
  highlightButton(button);
}

// Way 2: Using element.onclick
const btn2 = document.getElementById('way2');
btn2.onclick = function () {
  console.log("Way 2 clicked");
  highlightButton(this);
};

// Way 3: Using addEventListener
const btn3 = document.getElementById('way3');
btn3.addEventListener('click', function () {
  console.log("Way 3 clicked");
  highlightButton(this);
});

// Reusable function to highlight button and revert
function highlightButton(button) {
  button.style.backgroundColor = 'green';
  setTimeout(() => {
    button.style.backgroundColor = '';
  }, 500);
}
