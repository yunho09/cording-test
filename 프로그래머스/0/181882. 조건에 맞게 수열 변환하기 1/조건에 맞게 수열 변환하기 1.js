function solution(arr) {
    return arr.map((e) => e<50 ? e%2!=0 ? e*2 : e : e%2==0 ? e/2 : e);
}