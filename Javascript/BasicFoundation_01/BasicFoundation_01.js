//1- Get 1-255:
function getArr(){
    var arr = [];
    for (var i = 0; i < 255; i++){
        arr[i] = i+1;
    }
    return arr;
}

//2-Get even 1000:
function getEven(){
    var sum = 0;
    for (var i = 1; i <= 1000; i++){
        if(i % 2 == 0){
            sum += i;
        }
    }
    console.log(sum);
}

//3- Sum odd 5000:
function sumOdd(){
    var sum = 0;
    for(var i = 1; i < 5000; i++){
        if (i % 2 != 0){
            sum += i;
        }
    }
    return sum;
}

//4. Iterate an array:
function sumElements(arr){
    var sum = 0;
    for(var i = 0; i < arr.length; i++){
        sum += arr[i];
    }
    return sum;
}

//5. Find Max:
function getMax(arr){
    var max = arr[0];
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > max){
            max = arr[i];
        }
    }
    return max;
}

//6. Find Average:
function average(arr){
    var sum = 0;
    var average;
    for(var i = 0; i < arr.length; i++){
        sum += arr[i];
    }
    average = sum / arr.length;
    return average;
    
}

//7. Array odd:
function oddArray(){
    var arr = [];
    for(var i = 1; i <= 50; i++){
        if(i % 2 == 1){
            arr.push(i);
        }
    }
    return arr;
}

//8. Greater than Y:
function greaterY(arr){
    var count = 0;
    var y = 3;
    for(var i = 0; i < arr.length; i++){
        if (arr[i] > y){
            count++;
        }
    }
    return count;
}

//9.Squares:
function Squares(arr){
    for(var i = 0; i < arr.length; i++){
        arr[i] = arr[i] * arr[i];
    }
    return arr;
}

//10.Negative:
function negatives(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] < 0){
            arr[i] = 0;
        }
    }
    return arr;
}
//11.Max/Min/Avg:
function newArr(arr){
    var max = arr[0];
    var min = arr[0];
    var sum = 0
    var average;
    var newArr = [];

    for(var i = 0; i < arr.length; i++){
        sum += arr[i];
        if (arr[i] > max){
            max = arr[i];
        }
        else if(arr[i] < min){
            min = arr[i];
        }
        
    }
    average = sum / arr.length;
    newArr = [max , min, average];
    return newArr;
}

//12. Swap Values:

function swapArr(arr){
    var temp;
    temp = arr[0];
    arr[0] = arr[arr.length-1];
    arr[arr.length-1] = temp;
    return arr;
}

//13.Number to String:
function numToString(arr){

for(var i = 0; i < arr.length; i++){
    if(arr[i] < 0){
    arr[i] = 'Dojo';
        }
    }
    return arr;

}

