let addressNumber = 205;
let addressStreet = "somewhere";
let country = "Cameroon"

let globalAddress = "I live in " + addressStreet + ' ' + addressNumber + " ,in " + country

console.log(globalAddress)


let favoriteFood ="chicken"
let favoriteMeal = "Dinner"

console.log("I eat "+ favoriteFood + " at eery " + favoriteMeal)


const myWatchedSeries = ["black mirror", "money heist", "the big bang theory"];

let myWatchedSeriesLength= myWatchedSeries.length

let myWatchedSeriesSentence = myWatchedSeries[0]+', '+myWatchedSeries[1]+', and '+myWatchedSeries[2]


console.log(myWatchedSeriesLength)
console.log(myWatchedSeriesSentence)
console.log("I watched 3 series : " + myWatchedSeriesSentence)
console.log(myWatchedSeries.indexOf("the big bang theory"))

myWatchedSeries.splice(2,1,"friends")
myWatchedSeries.push("All American")
myWatchedSeries.unshift("Game of Thrones")

console.log(myWatchedSeries[2][2])
console.log(myWatchedSeries)


 let celsius = 12;

 function degToFahrenheit(val){
    converted_deg = (val*9/5)+32
    return converted_deg
 }

console.log(celsius+"°C is "+ degToFahrenheit(celsius)+" in °F")
