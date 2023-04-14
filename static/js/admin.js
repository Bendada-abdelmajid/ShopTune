if (localStorage.getItem("rokyashopdarkmodeclass")) {
  document.body.classList.add("dark");
}
let container = document.querySelector(".container");
let sidebarBtn = document.querySelector(".toggle");
const body = document.querySelector('body'),
  modeSwitch = body.querySelector(".mode");


  
sidebarBtn.onclick = function () {
  container.classList.toggle("active");
  if (container.classList.contains("active")) {
    sidebarBtn.classList.replace( "fa-chevron-right", "fa-chevron-left");
  } else {
    sidebarBtn.classList.replace("fa-chevron-left", "fa-chevron-right");
  }
}

modeSwitch.addEventListener("click" , () =>{
  if(body.classList.contains("dark")){
    body.classList.remove("dark");
    localStorage.removeItem("rokyashopdarkmodeclass");
  }else{
    body.classList.add("dark");
    localStorage.setItem("rokyashopdarkmodeclass", "dark");
  }
  
  
});
function showdeleteBox(num){
  const box_con=document.querySelector('.delete-box-container')
  const num_con=document.getElementById('num')

  box_con.classList.add('show')
  num_con.innerHTML=`Delete ${num} items`


}

const blox_con=document.querySelector('.delete-box-container')
blox_con.addEventListener('click' ,(e) => {
  if(e.target.classList.contains('overlay') || e.target.classList.contains('hide-box')) {
    blox_con.classList.remove('show')
  } 
})



const nav=document.querySelector('.sidebar-container')
const navBtn=document.querySelector('.nav-btn')
const closenav =nav.querySelector(".close");
const navOverlay = nav.querySelector(".overlay");



navBtn.addEventListener("click",() =>{
  nav.classList.add("show");
})
closenav.addEventListener("click",() =>{
  nav.classList.remove("show");
})
navOverlay.addEventListener("click",() =>{
  nav.classList.remove("show");
})


const months=["Jan", "Fab", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

const dayes=["mon", "tus", "wed", "thu", "fri", "sat", "sun"]
function showDate(){
  const newdate=new Date();
  
  const notif_date = document.querySelectorAll(".notif-date");
  notif_date.forEach((el) => {
    const text = el.innerHTML;
    const year = text.slice(0, text.indexOf("-"));
    const month = text.slice(text.indexOf("-")+1, text.indexOf("-")+3);
    const daye = text.slice(text.indexOf("-")+4, text.indexOf("-")+6);
    let hour = text.slice(text.indexOf( "T")+1, text.indexOf(":"));
    const menute = text.slice(text.indexOf(":")+1, text.indexOf(":")+3);
    if (newdate.getFullYear() == year) {
      if (newdate.getMonth()+1 == parseInt(month)) {
        if (newdate.getDate() == parseInt(daye)) {
          if (newdate.getHours() == parseInt(hour) ){
            last = newdate.getMinutes() - parseInt(menute);
  
            el.innerHTML= `${last} menute ago`
          } else {
            last_hour = newdate.getHours() - parseInt(hour);
            el.innerHTML= `${last_hour} hours ago`
          }
          
        }else {
          last_day=newdate.getDate() - parseInt(daye);
          if (last_day < 2) {
            el.innerHTML= `yesterday at ${hour} : ${menute}`
          }else {
            el.innerHTML= `${last_day} days ago at ${hour} : ${menute} `
          }
          
        }
      }else {
        el.innerHTML= `${months[month-1]},${daye} `
      }
    }else {
      el.innerHTML= `${months[month-1]},${daye},${year}`
    }
  });
}



console.log("hi from admin")

