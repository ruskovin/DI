let calc = '';
function number(num){
    calc = calc + num
    console.log(calc)
}

function operator(operator){
   calc += operator
    console.log(calc) 
}


function equal(){
    calc = eval(calc)
    alert(calc)
    calc = '';
    return
}

function reset(){
    calc = '';
    console.log(calc)
}

console.log(calc)