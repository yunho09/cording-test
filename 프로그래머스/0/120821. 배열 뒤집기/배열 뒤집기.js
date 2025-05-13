function solution(num_list) {
    let leg = num_list.length-1;
    let sum = 0;
    if(num_list.length % 2 == 0){
        for(let i = 0; i < num_list.length/2 ; i++){
            sum = num_list[i];
            num_list[i] = num_list[leg];
            num_list[leg] = sum;
            leg--;
        }
    }
    else if(num_list.length == 2){
        sum = num_list[0];
        num_list[0] = num_list[1];
        num_list[1] = sum;
    }
    else{
                for(let i = 0; i < Math.floor(num_list.length/2) ; i++){
            sum = num_list[i];
            num_list[i] = num_list[leg];
            num_list[leg] = sum;
            leg--;
        }
    }
    
    return num_list;
}