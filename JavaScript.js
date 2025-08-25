console.log("Hello!");

// VARIABLES IN JS

var name = "Apurva";  //initial declaration
console.log(name);
var name = "Kulkarni";  //redeclaration is allowed
console.log(name);
name = "ASK";  //updation is allowed 
console.log(name);  //output = ASK

let city = "Nagpur"; //initial declaration
console.log(city);
city = "Shegaon";  //updation is allowed
console.log(city);

const pi = 3.14159;
console.log(pi);

// DATA TYPES IN JS

let job = "Data Scientist";  //string
let age = "21";  //number
let isStudent = true;  //boolean
let car;  //undefined
let empty = null;  //null
let bigNum = 12345678912345678900;  //bigInt

console.log(job);
console.log(age);
console.log(isStudent);
console.log(car);
console.log(empty);
console.log(bigNum);

let student = {
    name: "Apurva",
    branch: "IT",
};  //object
let languages = ["English","Hindi","Marathi"]; //array
function greet2() {
    return "Hello, from function";
}  //function

console.log(student);
console.log(languages);
greet2();

//checking data types
console.log(typeof "Data Scientist");   
console.log(typeof 21);         
console.log(typeof true);       
console.log(typeof undefined);  
console.log(typeof null); 
console.log(typeof 12345678912345678900);     
console.log(typeof {});         
console.log(typeof []);         

// OPERATORS IN JS

let x = 10, y = 3;

//arithmetic operators
console.log(x+y);  //addition
console.log(x-y);  //subtraction
console.log(x*y);  //multiplication
console.log(x/y);  //division
console.log(x%y);  //modulus
console.log(x**y);  //power
console.log(x++);  //increment
console.log(y--);  //decrement

//comparison operators
console.log(x==y);  //checks only value
console.log(x===y);  //checks value and type
console.log(x!=y);  //not equal to
console.log(x!==y);  //strict !=
console.log(x>y);  //greater than
console.log(x<y);  //less than
console.log(x>=y);  //greater than or equal to
console.log(x<=y);  //less than or equal to

//logical operators
console.log(x > 5 && y < 5);  //logical AND
console.log(x > 5 || y > 5);  //logical OR
console.log(!(x > 5));  //negation

//assignment operators
x+=5;  //add and assign
console.log(x);
y*=3;  //multiply and assign
console.log(y);

//CONDITIONAL STATEMENTS IN  JS

let company = "BMW";

//if statement
if (company=="BMW") {
    console.log("It is a car.");
}

//if...else statement
if (company=="BMW") {
    console.log("It is a car.");
} else {
    console.log("It is not a car.");
}

//else...if ladder
let marks = 87;
if (marks>=50) {
    console.log("Pass");
} else if (marks<50 && marks >=40) {
    console.log("Barely paased.");
} else {
    console.log("Fail");
}

//switch statement
let day = 5;
switch (day) {
  case 1:
    console.log("Monday");
    break;
  case 2:
    console.log("Tuesday");
    break;
  case 3:
    console.log("Wednesday");
    break;
  case 4:
    console.log("Thursday");
    break;
  default:
    console.log("Invalid day");
}

//LOOPS IN JS

let i = 1;

//for loop
i=0;
for (i=0; i<3; i++) {
    console.log(i);
}

//while loop
i=1;
while (i<=3) {
    console.log(i);
    i++;
}

//do...while loop
i = 1;
do {
  console.log("Do While Count:", i);
  i++;
} while (i <= 5);

//for...of loop
let fruits = ["Apple", "Banana", "Mango"];

for (let fruit of fruits) {
  console.log(fruit);
}

//for...in loop
student = { name: "Apurva", branch: "IT", year: 4 };

for (let key in student) {
  console.log(key, ":", student[key]);
}

//FUNCTIONS IN JS

function greet() {
    console.log("Hello!");
}
greet();  //simple function

function greetUser(name) {
  console.log("Hello, " + name + "!");
}
greetUser("Apurva");  //function with parameters

function add (a,b) {
    return a+b;
}
let sum = add(3,4);  //function with a return value
console.log(sum);

const multiply = function(x, y) {
  return x * y;
};

console.log(multiply(3, 4));  //function expression

const square = (n) => n * n;
console.log(square(5));  //arrow function

//ARRAYS IN JS

let names = ["Shreya", "Sakshi", "Gargi", "Kalyani", "Apurva", "Saiee", "Advait", "Krish"];  //creating an array
let numbers = new Array(1,2,3,4,5);  //using new array
console.log(names.length);  //length of the array

names.push("Anagha");  //add to end
names.unshift("Sachin");  //add to start
console.log(names);

names.pop();  //removes last
names.shift();  //removes first
console.log(names);

console.log(names.indexOf("Saiee"));  //returns index
console.log(names.includes("Sakshi"));  //checks existence in the array

let fruit = ["Apple", "Banana", "Mango", "Orange", "Grapes"];

// slice(start, end) → returns part of array (does not change original)
console.log(fruit.slice(1, 4)); // ["Banana", "Mango", "Orange"]

// splice(start, deleteCount, items...) → modifies array
fruit.splice(2, 1, "Pineapple"); // remove 1 at index 2, add "Pineapple"
console.log(fruit); // ["Apple", "Banana", "Pineapple", "Orange", "Grapes"]

//iterating over arrays
for (let x of names) {
    console.log(x); 
}
 
//OBJECTS IN JS

let book = {
    title: "Never Lie",
    author: "Freida McFadden",
    year: 2022,
    publisher: "Hollywood Upstairs Press"
};  //creating objects

//modifying objects
book.publisher = "Hollywood Upstairs Press";  //updating
book.country = "USA";  //adding
console.log(book);
delete book.country;  //deleting
console.log(book);

//iterating through objects
for (let key in book) {
    console.log(key, ":", student[key]);
}