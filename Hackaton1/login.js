let emailInput = document.getElementById('mail')
let passwordInput = document.getElementById('pwd')
let loginButton = document.getElementById('login-btn')
let rememberMe = document.getElementById('remember')

console.log(emailInput, passwordInput)
let loginEvent = loginButton.addEventListener('click', ()=>{
    console.log(emailInput.value)
    console.log(passwordInput.value)
    console.log('Remember = '+ rememberMe.checked)
})

