function solution(my_string) {
    return my_string.split('').filter((e) => isNaN(e) == false).sort().map((e) => Number(e));
}