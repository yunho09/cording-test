function solution(n) {
    let a = 0;
    const m = n;
    for(let i = 1;i<=m;i++){
        if(n%2==0){
          a += n;
        }
        n -= 1;
    }
    return a;
}