//1-Sigma:
function sigma(num){
    var sum = 0;
    while(num >= 0){
        sum += num; 
        num--;
    }
    return sum;
}
//2-Factorial:
function factorial(num){
    var factorial = 1;
    while(num >= 1){
        factorial *= num;
        num--;
    }
    return factorial;
}
//3-Fibonacci:
function fib(num){
    var fib = [];
    fib[0] = 0;
    fib[1] = 1;

    for(var i = 2; i <= num; i++){
        fib[i] = fib[i-1] + fib[i-2];
    }
    return(fib[fib.length-1]);
}
//4-Array: Second-to-Last:
function returnSecondToLast(arr){
    if(arr.length <= 1){
        return null;
    }
    else{
        return arr[arr.length-2];
    }
}
//5-Array: Nth-to-Last: 
function returnSecondToLast(arr,num){
    if(arr.length <= 1){
        return null;
    }
    else if(num > 0 && num <= arr.length){
        return arr[arr.length-num];
    }
    else{
        return arr[arr.length-1];
    }
}
//6-Array: Second-Largest:
function secondLargest(arr){
var max1=arr[0];
var max2=arr[0];

if(arr.length <= 1){
return null;
}
for(var i = 0; i < arr.length;i++){
    if(arr[i] > max1){
    max2 = max1;
    max1 = arr[i];
}
}
return max2;
}
//7-Double Trouble:
function double(arr){
    var arrnew = [];

    for(var i = 0; i < arr.length; i++){
        for(var j = 0; j < 2; j++ ){
            arrnew.push(arr[i]);
        }
    }
    arr = arrnew;
    return arr;
}