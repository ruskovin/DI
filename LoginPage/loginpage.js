let emailInput = document.getElementById('mail')
let passwordInput = document.getElementById('pwd')
let loginButton = document.getElementById('login-btn')

console.log(emailInput, passwordInput)
let loginEvent = loginButton.addEventListener('click', ()=>{
    console.log(emailInput.value)
    console.log(passwordInput.value)
})

