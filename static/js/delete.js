 const delete_icon = document.getElementById("delete_icon");

 const checkBtns = document.querySelectorAll(".checkbox-btn");


 const selectAll = document.getElementById('selectAll')
 const deleteBtns= document.querySelectorAll('table td .delete_btn')
 deleteBtns.forEach((el) => { 
    el.addEventListener('click', (e) => { 
        el.parentElement.parentElement.querySelector('.checkbox-btn').checked=true
        delete_icon.click()
     })
 })
 const icon = selectAll.querySelector('i')
 let checkedBtns = [];
 selectAll.addEventListener("click", () => {
     console.log(icon.classList.contains('fa-list-check'));
     if (icon.classList.contains('fa-list-check')) {
         checkBtns.forEach((btn) => {
             btn.checked = true;
         });
         delete_icon.classList.add("show");
         icon.classList.replace('fa-list-check', 'fa-times')
     } else {
         checkBtns.forEach((btn) => {
             btn.checked = false;
         });
         delete_icon.classList.remove("show");
         icon.classList.replace('fa-times', 'fa-list-check')
     }
 });

 
 checkBtns.forEach((btn) => {
     btn.checked = false;
     btn.addEventListener("change", (e) => {
         checkedBtns = document.querySelectorAll(".checkbox-btn:checked");

         if (checkedBtns.length > 0) {
             delete_icon.classList.add("show");
         } else {
             delete_icon.classList.remove("show");
         }
         if (checkedBtns.length < checkBtns.length) {
             icon.classList.replace('fa-times', 'fa-list-alt')
         }
     });
 });
 delete_icon.addEventListener('click', () => {
    type=delete_icon.dataset.type
    checkedBtns = document.querySelectorAll(".checkbox-btn:checked");
   showdeleteBox(checkedBtns.length, type)
})
 function delete_items(path,crf, tid) {
    console.log('yes');
    console.log(path);
    const box_con=document.querySelector('.delete-box-container')
    var id = []
    $('.checkbox-btn:checked').each(function (i) {
        id[i] = $(this).val()
    })
    console.log(id)
    $.ajax({
      
        method: "POST",
        url: document.location.href  ,
   
        data: {
            id,
            csrfmiddlewaretoken: crf,
        },
        success: function (data) {
            id.forEach((i) => {
                document.querySelector(`table#${tid} tbody`).removeChild(document.getElementById('tr-' + i + ''))
            })
            id = []
            console.log(id);
            box_con.classList.remove('show')
        },
        error: function (response) {
            console.log("error", response);
        },
    });
  }




