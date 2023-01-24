let user_inp = prompt("enter words separated by commas")

// hello,world,in,a,frame

let user_inp_array = user_inp.split(',')

let gl = 0;

for(let i of user_inp_array){
        if(i.length > gl ){
                gl = i.length;
        }
    }

console.log('*'.repeat(gl + 4))

for (inp of user_inp_array){
    if (inp.length < gl ){
        console.log(`* ${inp}${' '.repeat(gl - inp.length)} *`);
    }
        else{
        console.log(`* ${inp} *`)
    }
}

console.log('*'.repeat(gl + 4))