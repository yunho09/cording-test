function solution(my_string) {
    let arr = my_string.split("").filter((v) => !'aeiou'.includes(v)).join("");
    return arr;
}