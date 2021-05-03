//Predict 1:
function greeting(){
        return "Hello";
        console.log("World");
    }
    var word = greeting();
    console.log(word);

/*Console.log:
"Hello"
*/

//Predict 2:
function add(num1, num2){
        console.log("Summing Numbers!");
        console.log("num1 is: " + num1);
        console.log("num2 is: " + num2);
        var sum = num1 + num2;
        return sum;
    }
    var result1 = add(3,5);
    var result2 = add(4,7);
    console.log(result1);
    console.log(result2);

/*Console.log:
"Summing Numbers!"
num1 is: 2
num2 is: 5
"Summing Numbers!"
num1 is: 4
num2 is: 7
7
11
*/

//Predict 3:
function highFive(num){
        for(var i=0; i<num; i++){
            if(i == 5){
                console.log("High Five!");
            }
            else{
                console.log(i);
            }
        }
    }

/*Console.log:
it will do nothing because function didn,t been called. and has no parameter.

but if we assume it have been called and we give it an argument (6) the output will be:
0
1
2
3
4
"High Five!"
*/

