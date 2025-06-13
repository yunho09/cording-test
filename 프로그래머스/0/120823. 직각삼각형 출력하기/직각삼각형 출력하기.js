const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = line.split(' ');
}).on('close', function () {
    let star = "";
    for(let i = 0; i < input ; i++){
        for(let j = 0 ; j < i+1 ; j++){
            star += '*';
        }
        star += '\n'
    }
    console.log(star);
    
});