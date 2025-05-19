function solution(array, height) { 
    let n = 0
    array.sort((a,b)=>b-a);
    for(let i = 0;i<array.length;i++){
        if(array[i]>height) n++;
    }
    return n;
}