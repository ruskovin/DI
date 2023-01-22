let calc = '';
function number(num){
    calc += num
    console.log(calc)
}

function operator(operator){
   calc += operator
    console.log(calc)
}

function equal(){
    calc = eval(calc)
    alert(calc)
    calc = 0;
    return
}

function reset(){
    calc = '';
    console.log(calc)
}

console.log(calc)