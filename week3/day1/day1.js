// let access_div = document.getElementById('parent')
// // let b = c.nextElementSibling
// let div = document.getElementsByTagName('div')[0]
// let b = div.nextElementSibling
// let d = b.firstElementChild

// console.log(b)
// console.log(c)
// console.log(d)


// let btn = document.getElementById('button')

// btn.addEventListener('click', ()=>{
//     document.getElementById('john').innerHTML = prompt("enter the name you want to replace john with")
//     if ( document.getElementById('john').innerHTML ===''){
//         alert("You should enter something")
//         document.getElementById('john').innerHTML  = "John"

//     }
// })

let newDiv = document.createElement('div')  
let newTextNode = document.createTextNode('Here I am');
newDiv.appendChild(newTextNode);
document.body.appendChild(newDiv);