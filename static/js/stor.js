const  closeSearchBtn = document.querySelector(".close-form"),
searchIcon= document.querySelector('.search-icon');
searchIcon.addEventListener('click', () => {
    document.querySelector('.search-container').classList.add('show')
  })
  closeSearchBtn.addEventListener('click', () => {
    document.querySelector('.search-container').classList.remove('show')
  })

