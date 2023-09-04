    // JavaScript code
window.addEventListener('DOMContentLoaded', function() {
  // Get the container element
  var container = document.querySelector('.same-item-container');
  
  // Get the buttons
  var leftButton = document.getElementById('left2');
  var rightButton = document.getElementById('right2');
  
  // Set the initial scroll position
  var scrollPosition = 0;
  
  // Set the scroll amount for each button click
  var scrollAmount = 200;
  
  // Calculate the maximum scroll position
  var maxScrollPosition = container.scrollWidth - container.clientWidth;
  
  // Update the button states based on the initial scroll position
  updateButtonStates();
  
  // Add event listeners for the buttons
  leftButton.addEventListener('click', scrollLeft);
  rightButton.addEventListener('click', scrollRight);
  
  // Function to scroll left
  function scrollLeft() {
    scrollPosition -= scrollAmount;
    if (scrollPosition < 0) {
      scrollPosition = 0;
    }
    container.scrollTo({
      left: scrollPosition,
      behavior: 'smooth'
    });
    updateButtonStates();
  }
  
  // Function to scroll right
  function scrollRight() {
    scrollPosition += scrollAmount;
    if (scrollPosition > maxScrollPosition) {
      scrollPosition = maxScrollPosition;
    }
    container.scrollTo({
      left: scrollPosition,
      behavior: 'smooth'
    });
    updateButtonStates();
  }
  
  // Function to update the button states based on the scroll position
  function updateButtonStates() {
    leftButton.disabled = scrollPosition === 0;
    rightButton.disabled = scrollPosition === maxScrollPosition;
  }
});
