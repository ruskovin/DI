// let lang = prompt().toLowerCase();
// let greet = ""
// switch(lang){
//     case "english":
//         greet = "Hello";
//         break;
//     case "french":
//         greet = "Bonjour";
//         break;
//     case "hebrew":
//         greet = "Shalom"
//         break;
//     default:
//         greet = '01110011 01101111 01110010 01110010 01111001';
//         break;
// }

// alert(greet)

// 2

// let grade = parseInt(prompt());

// let grade_letter = "";

// if (grade>90){
//     grade_letter = "A"
// }

// else if(80< grade && grade <=90 ){
//     grade_letter = "B"
// }

// else if(70<= grade && grade <=80 ){
//     grade_letter = "C"
// }

// else if(grade<70 ){
//     grade_letter = "D"
// }

// alert(grade_letter)


// 3

let verb = prompt("Enter a verb")

if( verb.length >=3 &&  verb.endsWith("ing")===false){
    alert(verb + "ing")
}
else if( verb.length >=3 && verb.endsWith("ing")){
    alert(verb + "ly")
}
else{
    alert(verb)
}



