function solution(n, k) {
    let a = n*12000;
    let b = k*2000;
    for(let i = 0;n>=10;i++){
        b -= 2000;
        n -= 10;
    }
    return a+b;
}