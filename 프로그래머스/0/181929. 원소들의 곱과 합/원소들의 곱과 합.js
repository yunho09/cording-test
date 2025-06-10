function solution(num_list) {
    let a = 0;
    let b = 1;
    for(let i = 0; i < num_list.length ; i++){
        a += num_list[i];
        b *= num_list[i];
    }
    return b <= a*a ? 1 : 0
}