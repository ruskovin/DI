// Exercise 1

// let a = 10;
// let b = 21;

// if(a<b){
//     console.log("b is greater than a")
// }
// if(a>b){
//     console.log("a is greater than b")
// }
// if(a===b){
//     console.log("a is equal to b")
// }

// // Exercise 2

// let newDog = 'Chihuahua';

// //1
// console.log('Chihuahua has '+newDog.length + " letters");
// //2
// console.log(newDog.toUpperCase());
// //3
// console.log(newDog.toLowerCase());

// switch(newDog){
//     case 'Chihuahua':
//         console.log("I love Chihuahuas, it's my favorite dog breed");
//         break;
//     default:
//         console.log("I dont care, I prefer cats");
//     }

// // Exercise 3

// let x = parseInt(prompt("enter a variable"));

// if(x%2 === 0){
//     alert("x is an even number");
// }
// else if(x%2 !=0){
//     alert("x is not an even number");
// }

// Exercise 4

const users = ["Lea123", "Princess45"];

let usersConnectedCount = users.length ;
console.log("There are "+usersConnectedCount+ " user(s) connected")
let usersConnected = "";

if (usersConnectedCount === 0 ){
    console.log("No users connected");
}
else if (usersConnectedCount===1){
    usersConnected += (users[0] + " is online")
}

else if(usersConnectedCount===2){
    usersConnected += (`${users[0]} and ${users[1]} are connected!`)
}

else if(usersConnectedCount>2){
    usersConnected += (`${users[0]} , ${users[1]} and  ${(usersConnectedCount - 2)} more are connected `)
}
console.log(usersConnected)