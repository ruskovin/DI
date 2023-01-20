// let sentence = prompt()

// let sentenceArr = sentence.split(' ')

// console.log(sentenceArr)
// let nemoPosition = sentenceArr.indexOf("Nemo")
// console.log(nemoPosition)

// if(nemoPosition != -1){
//     console.log("I found Nemo at " + nemoPosition);
// }
// else{
//     console.log("I can't find Nemo");
// }


// 4



let n = parseInt(prompt());


if(n<2){
    alert("Boom")
}

else if( n%2 ===0 && n%5===0){
    alert("Boom!".toUpperCase())
}
else if(n % 2 === 0){
    alert("Boom!")
}
else if( n % 5 ===0){
    alert("Boom".toUpperCase())
}
else if(n>2){
    alert("B" + "o".repeat(n) + "m")
}