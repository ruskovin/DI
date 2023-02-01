const tasks =[];

let task = document.getElementById("task")
let Add = document.getElementById("add")
let div = document.getElementById("listTasks")

let list = document.createElement('ul')


let addList = Add.addEventListener("click", function addTask(){
    if (task.value != ''){
        tasks.push(task.value)

            let li = document.createElement('li');
            li.innerHTML = task.value
            list.appendChild(li)
            let cbox = document.createElement('input')
            cbox.setAttribute("type", "checkbox")
            list.appendChild(cbox)
        }

})




div.appendChild(list)
