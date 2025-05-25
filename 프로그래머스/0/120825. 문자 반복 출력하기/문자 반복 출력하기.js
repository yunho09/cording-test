function solution(my_string, n) {
    my_string.split("");
    let arr = [];
    for(let i = 0 ; i < my_string.length ; i++){
        for(let j = 0 ; j < n ; j++){
            arr.push(my_string[i]);
        }
    }
    return arr.join("");
}