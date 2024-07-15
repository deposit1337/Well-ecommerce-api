const firstElement = document.getElementById("trigger-element");
const secondElement = document.getElementById("change-element");
const thirdElement = document.getElementById("element-replacement");

firstElement.addEventListener("mouseover", function () {
    
  secondElement.classList.add("not");
  thirdElement.classList.remove("not");
  
  thirdElement.classList.remove("none");
});

firstElement.addEventListener("mouseout", function () {
  firstElement.classList.remove("not");
  thirdElement.classList.add("not");
  secondElement.classList.remove("not");
});
