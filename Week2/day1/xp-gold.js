// 1

let sentence = ["my","favorite","color","is","blue"];

let sentenceStr = sentence.join(" ")
console.log(sentenceStr)

// 2

// let str1 = "mix";
// let str2 = "pod";
let str1 = "Hello";
let str2 = "World";

let nStr1 = (str1.slice(0,2) + str2.slice(2))
let nStr2 = (str2.slice(0,2) + str1.slice(2))
console.log(nStr2, nStr1)
console.log(str1.slice(0,3))
// 3
let num1 = parseInt(prompt("enter num1"))
let num2 = parseInt(prompt("enter num2"))

alert(" The sum of these two numbers is "+( num1 + num2))