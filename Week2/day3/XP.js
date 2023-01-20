const people = ["Greg", "Mary", "Devon", "James"];

// 1

people.splice(0,1)

console.log(people)

//2

people.splice(2,1,"Jason")
console.log(people)

//3

people.push("Paul")
console.log(people)

//4

console.log(people.indexOf('Mary'))

//5
const peopleNew = people.slice(1,-1)
console.log(peopleNew)

//6

console.log(people.indexOf('foo'))

//7
let last = peopleNew[(peopleNew.length - 1)]
console.log(last)


// Part II : loops
 
// 1
people.forEach(i => {
    console.log(i)
});

// 2
console.log("*************")
for (let x in people) {
    if (people[x]==="Jason") {
        break;
    }
    console.log(people[x])
}


//Exercice 2 : Your favorite colors

// 1

let colors = ["blue", "green","white", "yellow","black"];
let suffixes =['st', 'nd','rd','th']

// for(let color in colors){
//     console.log("My #"+color + " choice is "+colors[color] ) 
// }
// for(let color in colors){
//     console.log("My "+color + "st choice is "+colors[color] ) 
// }

// bonus

// for (let color in colors){
//     let colCount = parseInt(color)
//    if(color == 0){
//     // console.log("My "+(colCount +1) +suffixes[0]+ " choice is "+colors[color]);
//     console.log(`My ${(colCount +1)}${suffixes[0]} choice is ${colors[color]}`);
//    }
//    else if (color == 1){
//     // console.log("My "+(colCount +1) +suffixes[1]+ " choice is "+colors[color]);
//     console.log(`My ${(colCount +1)}${suffixes[1]} choice is ${colors[color]}`);
    

//    }
//    else if (color == 2){
//     // console.log("My "+(colCount +1) +suffixes[2]+ " choice is "+colors[color]);
//     console.log(`My ${(colCount +1)}${suffixes[2]} choice is ${colors[color]}`);

//      }else{
//         // console.log("My "+(colCount +1) +suffixes[3]+ " choice is "+colors[color]);
//         console.log(`My ${(colCount +1)}${suffixes[3]} choice is ${colors[color]}`);

//      }
// }



// Exercise 3
// let num;
    
// do {
//     num = parseInt(prompt("Enter a number greater than 10 please"));

// } while ( num<10);





// Exercise 4

const building = {
    numberOfFloors: 4,
    numberOfAptByFloor: {
        firstFloor: 3,
        secondFloor: 4,
        thirdFloor: 9,
        fourthFloor: 2,
    },
    nameOfTenants: ["Sarah", "Dan", "David"],
    numberOfRoomsAndRent:  {
        sarah: [3, 990],
        dan:  [4, 1000],
        david: [1, 500],
    },
}

console.log(building['numberOfFloors'])

console.log(`There are ${building['numberOfAptByFloor'].firstFloor} floors in the first appart and ${building['numberOfAptByFloor'].thirdFloor} in the third appart `)

console.log(` The name of the second tenant is ${building['nameOfTenants'][1]} and he has ${building['numberOfRoomsAndRent']['dan'][0]} rooms in his appartment`)

let sarahRent = building['numberOfRoomsAndRent']['sarah'][1]
let davidRent = building['numberOfRoomsAndRent']['david'][1]
let danRent = building['numberOfRoomsAndRent']['dan'][1]

if ((sarahRent + davidRent)> danRent){
    danRent += 200
}

console.log(danRent)