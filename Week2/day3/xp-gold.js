// Exercise 1 : Divisible by three

// let numbers = [123, 8409, 100053, 333333333, 7]

// for (let num in numbers){
//     if(numbers[num]%3 ===0){
//         console.log('true')
//     }
//     else{
//         console.log('false')
//     }
// }


// Exercise 2 : Attendance
// let guestList = {
//     randy: "Germany",
//     karla: "France",
//     wendy: "Japan",
//     norman: "England",
//     sam: "Argentina"
//   }

// let namer = prompt("enter your name:")
// if(namer in guestList ){
//     console.log(`Hi! I'm ${namer}, and I'm from ${guestList[namer]}.`)
// }
// else{
//     console.log("Hi I am a guest")
// }


//Exercise 3 : Playing with numbers

let ages = [20,1, 114,310,43,55];



// let sumAges = 0;

// for (let age in ages){
    //     sumAges += ages[age]
    // }
    
    // for( let i=0 ; i <= (ages.length)-1; i++ ){
        //     sumAges += ages[i];
        // }
        // console.log(sumAges);



        // ALGORITHMS TO FIND THE GREATEST NUMBER OF AN ARRAY

        // ALGO I
// let greatest = ages[0];
// let gh = 0;

// for(let i of ages){
//     if(i > gh ){
    //         gh = i;
//     }
// }
// console.log(gh)

                // ALGO II

// for (let i =1; i<= (ages.length); i++){
//     if( ages[i]>greatest){
//         greatest = ages[i];
//     }
// }

    // ALGO III

// let greatest =0;                
// for (let i =0; i<= (ages.length); i++){
//     if( ages[i+1]>ages[i]){
//         if(ages[i+1]>greatest){
//             greatest = ages[i+1];
//         }
//     }
// }
console.log(greatest);