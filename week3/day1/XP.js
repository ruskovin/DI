
//   Exercise 1

// let dv = document.getElementById("container")
// console.log(dv)

// let ul1 = document.getElementsByClassName("list")[0]
// ul1.lastElementChild.innerHTML = "Richard"

// let uls = document.getElementsByClassName('list')

// for (ul of uls){
//     ul.firstElementChild.innerHTML = "Paul"
// }


// let parent = document.getElementsByClassName('list')[1]
// let child = document.getElementById('Sarah')
// parent.removeChild(child)


//   Exercise 2


// let divv = document.getElementsByTagName('div')[0]

// divv.style.backgroundColor = 'lightBlue'
// divv.style.padding = '15px'

// let ul = document.getElementsByTagName('ul')[0]
// ul.firstElementChild.style.display = 'none'
// ul.lastElementChild.style.border = '2px solid red'

// document.body.style.fontSize = " 22px"


// Exercise 3


// let dvv = document.getElementById("navBar")
// console.log(dvv)
// dvv.setAttribute('id', 'socialNetworkNavigation')
// console.log(dvv)

// let ul = document.getElementsByTagName('ul')[0]
// let newLi = document.createElement('li')
// let textNode = document.createTextNode('Log out')

// newLi.appendChild(textNode)

// ul.appendChild(newLi)

// let fstEl = ul.firstElementChild
// let lastEl = ul.lastElementChild
// console.log(fstEl.textContent, lastEl.textContent)


// Exercise 4

let allBooks =[
    {
        "title": "The prince",
        "author": "machiavel",
        "image": "www.machiavel.com",
        "alreadyRead": true
    },
    {
        "title": 'Flatland',
        "author": 'Abbot Edwin',
        "image":'www.flatland.com',
        "alreadyRead":false
    }
]

let table = document.createElement('table')
let div = document.getElementsByClassName("listBooks")[0]
div.appendChild(table)
let headers = ["title", "author", "image"]


for (let h of headers){
    let tableheaders = document.createElement('th')
    tableheaders.innerHTML = h
table.appendChild(tableheaders)
}

for (let title in allBooks){
    let row = document.createElement('tr')
    let  tabledata1 = document.createElement('td')
    let  tabledata2 = document.createElement('td')
    let  tabledata3 = document.createElement('td')
    tabledata1.innerHTML = allBooks[title].title
    tabledata2.innerHTML = allBooks[title].author
    tabledata3.innerHTML = allBooks[title].image
    row.appendChild(tabledata1)
    row.appendChild(tabledata2)
    row.appendChild(tabledata3)
    table.appendChild(row)
}