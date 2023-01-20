// function ageCalc(myAge){
//     let myMomAge = myAge * 2
//     let myDadAge = parseInt(myMomAge * 1.2)

//     console.log(' my mom age is '+ myMomAge + ' and my dad age is '+ myDadAge)
// }

// ageCalc(12)


// function about(myAge){
//     let myMomAge = myAge * 2
//     return myMomAge;
// }

// let alpha = about(17)
// console.log(alpha)


let person= {
    firstName : "Sarah",
    eyeColor: "blue",
    eat : function () {
        console.log("My name is " + this.firstName + " I love chocolate")
    }
}


person.eat()