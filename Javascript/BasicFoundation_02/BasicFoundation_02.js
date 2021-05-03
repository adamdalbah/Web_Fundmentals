//1-Biggie Size:
function Biggie(arr){
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            arr[i] = "big";
        }
    }
    return arr;
}

//2.Print Low, Return High:
function printLowestAndReturnHigh(arr){
    var min = arr[0];
    var max = arr[0];

    for(var i = 0; i < arr.length; i++){
        if(min < arr[i]){
            min = arr[i];
        }
        else if(max > arr[i]){
            max = arr[i]
        }
    }
    console.log(min);
    return max;
}
//3.Print One, Return Another:
function printOneReturnAnother(arr){
    var odd = null;
    console.log(arr[arr.length-2]);
    for(var i = 0; i < arr.length; i++){
        if(arr[i] % 2 == 1 && odd == null){
            odd = arr[i];
        }
    }
    return odd;
}
//4.Double Vision:
function double(arr){
    var newArr = [];
    for(var i = 0; i < arr.length; i++){
        newArr[i] = arr[i] * arr[i];
    }
    return newArr;
}
//5.Count Positives:
function countPositives(arr){
    var count = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] > 0){
            count++
        }
    }
    arr[arr.length-1] = count;
    return arr;
}
//6.Evens and Odds:
function eventAndOdds(arr){
    arr = [1,3,5,4,6,6];
    var countOdd = 0;
    var countEven = 0;
    
    for(var i = 0; i < arr.length; i++){
    countEven++;
    countOdd++;
    if(arr[i] % 2 == 1 && countOdd % 3 == 0){
        console.log("Thats odd");
        countOdd = 0;
    }
    else if(arr[i] % 2==0 && countEven % 3 == 0){
    console.log("Even more so!")
    countEven = 0;
    }
    }
}
//7.Increment the Seconds:
function incrementSeconds(arr){
    for(var i = 0; i < arr.length; i++){
        if(i % 2 == 1){
            arr[i] += 1;
            console.log(arr[i]);
        }

    }
    return arr;
}

//8.Previous Lengths:
function previousLength(arr){
    var arr =["hello", "dojo", "awesome"];
for(var i = arr.length-1; i > 0; i--){
	arr[i] = arr[i-1].length;
}
return arr;
}
//9.Add Seven:
function addSeven(arr){
    newArr = [];
    for(var i = 0; i < arr.length; i++){
        newArr += arr[i] + 7;
    }
    return newArr;
}
//10.Reverse Array:
function reverseArray(arr){
    for(var i = 0; i < arr.length/2; i++){
        var temp = arr[i];
        arr[i] = arr[arr.length-1-i];
        arr[arr.length-1-i] = temp;
    }
    return arr;
}
//11.Outlook: Negative:
function makeNegative(arr){
    var newArr = [];
    for(var i = 0; i < arr.length; i++){
        if(arr[i] >= 0){
            newArr[i] = arr[i] * -1;
        }
        else{
            newArr[i] = arr[i];
        }
    }
    return newArr; 
}
//12.Always Hungry:
function alwaysHungry(arr){
    var count = 0;
    for(var i = 0; i < arr.length; i++){
        if(arr[i] == "food"){
            console.log("yummy");
        }
        else if(count!=1){
            console.log("I,m Hungry");
            count++;
        }
    }
}
//13.Swap Toward the Center:
function towardCenter(arr){
for(var i = 0; i < arr.length/2; i+=2){
	var temp = arr[i];
    arr[i] = arr[arr.length-1-i];
    arr[arr.length-1-i] = temp;
}
console.log(arr);
}
//14.Scale the Array:
function ScaleTheArray(arr,num){
    for(var i = 0; i < arr.length;i++){
        arr[i] *= num;
    }
}
return arr;
