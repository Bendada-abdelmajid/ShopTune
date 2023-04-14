// const menu = document.querySelector(".nav-list");
// const menuTrigger = document.querySelector(".mobile-menu-trigger");
// const closeMenu = menu.querySelector(".mobile-menu-close");
// const fancytext = document.querySelector('.fancy');
// const splitfancytext = fancytext.textContent.split('')
// fancytext.textContent = ""
// for (let i = 0; i < splitfancytext.length; i++) {
//   fancytext.innerHTML += "<span>" + splitfancytext[i] + "</span>"
// }

// let char = 0;
// let n_char = 0;
// let addtimer;
// let removetimer;
// menuTrigger.addEventListener("click", () => {
//   menu.classList.add("active");
//   onTic()
// })
// closeMenu.addEventListener("click", () => {
//   menu.classList.remove("active");
//   char = 0;
//   n_char = 0;
//   clearInterval(removetimer)
//   clearInterval(addtimer)
//   addtimer = null
//   removetimer = null
// })

// const closeSearchBtn = document.querySelector(".close-form"),
//   searchIcon = document.querySelector('.search-icon');
// searchIcon.addEventListener('click', () => {
//   document.querySelector('.search-container').classList.add('show')
// })
// closeSearchBtn.addEventListener('click', () => {
//   document.querySelector('.search-container').classList.remove('show')
// })

// // fancy header styling


// function onTic() {
//   clearInterval(removetimer)
//   addtimer = setInterval(() => {
//     const span = fancytext.querySelectorAll('span')[char]
//     span.classList.add('fade')
//     char++;
//     if (char === splitfancytext.length - 1) {
//       complete()
//       n_char = 0;
//       console.log('yes');
//     }
//     console.log(char + "==> " + splitfancytext.length);
//   }, 50)

// }

// function complete() {
//   clearInterval(addtimer)

//   removetimer = setInterval(() => {

//     const span = fancytext.querySelectorAll('span')[n_char]
//     span.classList.remove('fade')
//     n_char++;
//     if (n_char === splitfancytext.length - 1) {
//       console.log('yes finished');
//       console.log(char);
//       char = 0;
//       onTic()
//     }
//   }, 50);


// }