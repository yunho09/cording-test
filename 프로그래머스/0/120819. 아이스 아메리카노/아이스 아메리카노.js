function solution(money) {
    let a = Math.floor(money / 5500);
    let b = money % 5500;
    return [a, b];
}