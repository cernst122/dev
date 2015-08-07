var katzDeli=[];
function takeANumber(name){
  katzDeli.push(name);
  console.log(katzDeli.length);
  katzDeli[katzDeli.length-1]=name;
  //noreturn katzDeli.length;
}

function nowServing(){
  if (katzDeli.length>0){
    console.log("Now serving "+katzDeli[0]);
    katzDeli.splice(0, 1);
  }
  else{
    console.log("There is nobody in line");
  }
}
function line(name){
  //print index of name +1
}

//while loops
/*var temperature=80;
var idealTemperature=60;

while(temperature > idealTemperature){
  temperature=temperature-1;
  console.log(temperature);
}

console.log("AC off, it is freezing in here!");*/

/* for loops
var instructors=[
  "monsur",
  "nicki",
  "riccardo",
  "justin"
];

for (var i = 0; i < instructors.length; i=i+1 ){
console.log(i+ ": " + instructors[i]);
}*/

/*var myArr=[];
myArr[0]="Hello";
myArr[2]=54;
myArr[3]=true;
myArr[1]="Stuff";
var fruits=["Apples", "Oranges", "Pears", "Bananas"];
myArr=fruits;
console.log(myArr.length);
console.log(myArr.length-1);*/


/* var student = ["Jewel",
"Bex",
"Jackie",
"Yulissa"]; //multiple items can go in brackets.
function printName(name) {
  console.log(name);
}
student[1]="Liam";
student[4]="Shaun";
student.push("Shaun");//adds item to an array
student.pop();//takes last item out of array
student.pop();
printName(student);




//lab
function nervous(words){
  console.log(words+"...I think");
}
nervous();

function today(whatILearned){
  console.log("Today I learned "+whatILearned);
}
today();

function checkout(firstValue){
  console.log(firstValue*1.095);
  return firstValue*1.095;
}

checkout();

//conditionals example
var temperature=65;

if (temperature>=80){
  console.log("wear shorts");
}
else if (temperature>60){
  console.log("wear a light jacket");
}
else {
  console.log("wear a coat");
}

function skeeBall(score){
  if (score<150)
  {
    window.alert("That's rough");
  }
  else if (score>149&&score<250)
  {
    window.alert("not bad, kid");
  }
  else if (score>249&&score<350)
  {
    window.alert("Good job!");
  }
  else if (score>349&&score<450)
  {
    window.alert("Great work!!");
  }
  else
  {
    window.alert("Excellent job!");
  }

}
skeeBall(275); */
