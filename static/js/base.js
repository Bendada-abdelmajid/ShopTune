const header=document.querySelector("header")
//menu 
const menu_btn= document.querySelector(".menu-btn")
menu_btn.addEventListener('click', () => { 
  header.classList.add('show-menu') 
})
header.querySelector('.menu-overlay').addEventListener('click', () => { 
  header.classList.remove('show-menu') 
})
header.querySelector('.mobile-menu .close ').addEventListener('click', () => { 
  header.classList.remove('show-menu') 
})
//basket 
const shopingCard = document.querySelector(".shoping-list"),
  shopingBtn = document.querySelector(".shoping-btn"),

  upBtn = document.getElementById('up_btn');


const closeBtn = document.querySelector('.shoping-list .close-btn');
const cart_ov = document.querySelector('.shoping-list .overlay');

shopingBtn.addEventListener("click", (eo) => {
  verList()
  shopingCard.classList.add("show-list");

});
closeBtn.addEventListener("click", (eo) => {

  shopingCard.classList.remove("show-list");
});

cart_ov.addEventListener("click", (eo) => {

  shopingCard.classList.remove("show-list");
});

function verList() {
  const shopingList = document.querySelector('.shoping-list .product-list')
  if (shopingList.childElementCount == 0) {
    shopingCard.querySelector('.vide').style = "display: flex;"
    shopingCard.querySelector('.not-vide').style = "display: none;"
    shopingCard.querySelector('#continue-btn').addEventListener("click", () => {

      shopingCard.classList.remove("show-list");
    });
  } else {
    shopingCard.querySelector('.not-vide').style = "display: block;"
    shopingCard.querySelector('.vide').style = "display: none;"
  }
}


// sub-menu-container
const sub_menu_cont= document.querySelector('.sub-menu-container')
sub_menu_cont.addEventListener("touchstart", (e) => { 
  sub_menu_cont.classList.toggle("active")
  })
// up button
if (window.scrollY > 360) {

  upBtn.classList.remove("hide");
} else {
  upBtn.classList.add("hide");
}
upBtn.addEventListener('click', () => {
  window.scrollTo(0, 0)
  setTimeout(() => {
    upBtn.classList.add("hide");
  
  }, 300);
})











/// serach 

const res = document.getElementById("result");
const search_btn = document.getElementById("search-btn");
const close_search = document.querySelector(".close-search");
const search_overlay = document.getElementById("search-overlay");


const search_cont=document.getElementById("search_cont")
const search_input=document.getElementById("search_input")
search_input.addEventListener('focus', () => { 
  header.classList.add("active-search")
})
search_overlay.addEventListener('click', () => { 
  res.classList.remove("active")
  header.classList.remove("active-search")

})
let silider= true
search_btn.addEventListener("click", () => { 
  search_cont.classList.add("show")
  silider= false
})
close_search.addEventListener("click", () => { 
  search_cont.classList.remove("show")
  silider= true
})

search_input.addEventListener('keyup', () => { 
  fetch("/search-json/?q=" +search_input.value )
  .then((res) => res.json())
  .then((res1) => {
    const result = res1.search;
    res.innerHTML = '';
    let list = '';
    for (let item of result) {
      const disc= item.discount ?`<p class="amount"> $ ${item.price}</p><p class="cut">$ ${item.oldprice}</p> <div class="offer center">-${parseInt(item.discount)}%</div>` :`<p class="amount"> $ ${item.price}</p>`
      list += `<li class="splide__slide"><a href="/product/${item.slug}" class="box">
      <div class="image">
          <img src="${item.img}" alt="" />
      </div>
      <div class="content">
          <h3>${item.title}</h3>
          <div class="price">
              ${disc}
          </div>
  
      </div>
    </a> </li>
   `;
  }
    
    if (list != '') {
      
      if (result.length > 3) {
        res.innerHTML = `   <div class="resulet space_between" dir="rtl">
        <p> أكتر من <span>${result.length}</span> منتوج</p>
        <button type="submit">أضهر الكل <i class="fa fa-angle-left"></i></button>
      </div> <div class="splide__track box-container">
      <ul class="splide__list">
      ${list}
      </ul>
      </div>
     `;
      } else {
        res.innerHTML = `<div class="splide__track box-container">
        <ul class="splide__list">
        ${list}
        </ul>
        </div>`;
      }
      
      if(silider){
        new Splide( '#result', {
          gap:"15px",
          drag:"free",
          padding: { left: 20, right: 20 },
          pagination:false,
        } ).mount();
      }
      
    } else {
      res.innerHTML = `<div class="vide center" dir="rtl">
      <svg stroke="currentColor" fill="currentColor" stroke-width="0" version="1.1" id="search" x="0px" y="0px" viewBox="0 0 24 24" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><g><path d="M20.031,20.79c0.46,0.46,1.17-0.25,0.71-0.7l-3.75-3.76c1.27-1.41,2.04-3.27,2.04-5.31
		c0-4.39-3.57-7.96-7.96-7.96s-7.96,3.57-7.96,7.96c0,4.39,3.57,7.96,7.96,7.96c1.98,0,3.81-0.73,5.21-1.94L20.031,20.79z
		 M4.11,11.02c0-3.84,3.13-6.96,6.96-6.96c3.84,0,6.96,3.12,6.96,6.96c0,3.84-3.12,6.96-6.96,6.96C7.24,17.98,4.11,14.86,4.11,11.02
		z"></path></g></svg>
      <p>No result found</p>
  </div>`;
    }
    res.classList.add("active")
    
  });
 
})



// mobile menu
const menu_cats= document.querySelectorAll('.mobile-menu .cat-menu .menu-head');
menu_cats.forEach((btn) => { 
  btn.addEventListener('click', () => { 
   const check=btn.parentElement.classList.contains("show")
    menu_cats.forEach((el) => { el.parentElement.classList.remove("show")})
    console.log(btn.parentElement.classList.contains("show"))
    if(!check){
      btn.parentElement.classList.add("show")
    }
    
   })
 })


