function solution(n) {
    let m = String(n);
    let a = m.length;
    let b = 0;
    for(let i = 0 ; i < a ; i++){
        b += Number(m[i]);
    }
    return b;
}