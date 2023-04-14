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
  const MinVlaueBubbleStyle = () => {
    minPercentage = ((rangeInput[0].value - rangeInput[0].min) / rangeInput[0].max) * 100 
    minval.style.left = minPercentage + "%"
    minval.style.transform = `translate(-${minPercentage /2}%, -80%)`
    
  }
  const MaxVlaueBubbleStyle = () => {
    maxPercentage = 100 -(maxRange / rangeInput[1].max) * 100
    maxval.style.right = maxPercentage + "%"
    maxval.style.transform = `translate(${maxPercentage / 2}%, 80%)`
  }

  const setMinValueOutput = () => {
    minRange = parseInt(rangeInput[0].value);
    minval.innerHTML = rangeInput[0].value
  }
  const setMaxValueOutput = () => {
    maxRange = parseInt(rangeInput[1].value);
    maxval.innerHTML = rangeInput[1].value
  }

  setMinValueOutput()
  setMaxValueOutput()
  minRangeFill()
  maxRangeFill()
  MinVlaueBubbleStyle()
  MaxVlaueBubbleStyle()

rangeInput.forEach((input) => {
input.addEventListener("input", (e) => {
  minRangeFill();
  maxRangeFill();
  setMinValueOutput();
  setMaxValueOutput();

  

  MinVlaueBubbleStyle();
  MaxVlaueBubbleStyle();

  if (maxRange - minRange < minRangeValueGap) {     
    if (e.target.className === "min") {
      rangeInput[0].value = maxRange - minRangeValueGap;
      setMinValueOutput();
      minRangeFill();
      MinVlaueBubbleStyle();
      e.target.style.zIndex = "2"
    } 
    else {
      rangeInput[1].value = minRange + minRangeValueGap;
      e.target.style.zIndex = "2"
      setMaxValueOutput();
      maxRangeFill();
      MaxVlaueBubbleStyle();
    }
  } 


});
});

