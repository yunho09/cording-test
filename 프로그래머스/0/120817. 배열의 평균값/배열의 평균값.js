function solution(numbers) {
    let a = 0;
    for(let i = 0 ; i < numbers.length ; i++){
        a += numbers[i];
    }
    return Number(a/numbers.length).toFixed(1);
}