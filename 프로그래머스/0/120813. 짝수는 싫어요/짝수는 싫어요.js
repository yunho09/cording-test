function solution(n) {
    let arr = [];
    let arry = [];
    for(let i = 1 ; i <= n;i++){
        arr.push(i);
    }
    for(let i of arr){
        if(i%2 != 0) arry.push(i);
    }
    return arry;
}