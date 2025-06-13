function solution(array) {
    let answer = [];
    let M = 0;
    for(let i = 0; i < array.length ; i++){
        if(array[M] <= array[i]){
            M = i;
        }
    }
    let result = [array[M],M];
    return result;
}