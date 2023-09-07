const dropMenu= document.getElementById("drop_menu_cont")
const dropMenuBtn= document.getElementById("drop_menu_btn")
console.log(dropMenuBtn)
dropMenuBtn.addEventListener('click', () => {
    dropMenu.classList.toggle("show") 
 })

 let minRangeValueGap = 6;
const priceForm = document.getElementById("price-form");
const range = document.getElementById("range_track");
const minval = document.querySelector(".minvalue");
const maxval = document.querySelector(".maxvalue");
const rangeInput = document.querySelectorAll(".price-input");

let minRange, maxRange, minPercentage, maxPercentage;
const minRangeFill = () => {
    range.style.left =(( rangeInput[0].value - rangeInput[0].min) /(rangeInput[0].max  - rangeInput[0].min)  )*100  + "%";
    
  }
  const maxRangeFill = () => {
   
    range.style.right = 100 - ( ( rangeInput[1].value - rangeInput[0].min)/ (rangeInput[1].max  - rangeInput[0].min) )*100  +"%";
  }
 

  const setMinValueOutput = () => {
    minRange = parseInt(rangeInput[0].value);
    minval.innerHTML = parseFloat(rangeInput[0].value).toFixed(2)
  }
  const setMaxValueOutput = () => {
    maxRange = parseInt(rangeInput[1].value);
    maxval.innerHTML = parseFloat(rangeInput[1].value).toFixed(2)
  }

  setMinValueOutput()
  setMaxValueOutput()
  minRangeFill()
  maxRangeFill()


rangeInput.forEach((input) => {
input.addEventListener("input", (e) => {
  minRangeFill();
  maxRangeFill();
  setMinValueOutput();
  setMaxValueOutput();

  


  if (maxRange - minRange < minRangeValueGap) {     
    if (e.target.className === "min") {
      rangeInput[0].value = maxRange - minRangeValueGap;
      setMinValueOutput();
      minRangeFill();
      
      e.target.style.zIndex = "2"
    } 
    else {
      rangeInput[1].value = minRange + minRangeValueGap;
      e.target.style.zIndex = "2"
      setMaxValueOutput();
      maxRangeFill();
     
    }
  } 


});
});

