// let sentence = 'This movie is not so bad !';
// let sentence =  'This dinner is bad !';
let sentence = 'This dinner is not that bad ! You cook well' ;
let wordNot = sentence.indexOf('not');
let wordBad = sentence.indexOf('bad');
console.log(wordNot, wordBad)
let str;
if ( wordNot <0){
    console.log(sentence);
} else if (wordNot < wordBad) {
    str = sentence.substring(0, wordNot) + 'good' + sentence.substring(wordBad+3);
    console.log(str);
}