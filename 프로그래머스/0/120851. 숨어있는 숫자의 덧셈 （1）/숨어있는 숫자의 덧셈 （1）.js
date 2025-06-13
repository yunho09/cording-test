function solution(my_string) {
    return my_string.split('').filter((e) => isNaN(e) == false).map((e) => Number(e)).reduce((a,b) => a+b);
}