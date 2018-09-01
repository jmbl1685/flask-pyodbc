'use strict'

window.addEventListener('load', () => {
  console.log('Hello World');
})

function LoadDate() {
  fetch('/user')
    .then(res => res.json())
    .then(res => { render(res) })
    .catch(err => { console.log(err) })
}

function render(res){

  let app = document.getElementById('render')
  app.style.textAlign = 'center'

  res.forEach((user,index) => {
    
    app.innerHTML += 
    ` 
      <div id="user_${index}">
        <h1>${user.FullName}</h1>
        <h3>${user.Email}</h3>
      </div>
    `
    
  })
  
}

LoadDate();