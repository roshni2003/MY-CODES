// var num=22;
// if (num%10==0){
//     console.log("last digit number")
// }
// else{
//     console.log("not a last digit number")
// }



// var a=2;
// var b=4;
// if (a>b) {
//     console.log("a is large");
//   } else if (a<b) {
//     console.log("b is large");
//   } else {
//     console.log("small");
//   } 212

// var a=require('readline-sync'). questionInt("enter")
// if (a%3==0 && a%5==0){
// console.log("fizz-buzz")
// }else if (a%3==0){
//     console.log("fizz")
// }else if(a%5==0){
//     console.log("buzz")
// }

// a=5
// b=10        
// c=15
// c=a
// a=b
// b=c

// console.log(a,b,c)



// people=["Roshni", "kajal", "monika","ruchi"]
// for (let name in people){
//     console.log(name)
// }


// console.log("*****For of*****")

// people=["Roshni", "kajal", "monika","ruchi"]
// for (let name of people){
//     console.log(name)
// }



// var cars = ["Maruti", "Mercedes", "BMW"];
// for (let car in cars){
//    console.log(cars[car])
// }


// const n=require("readline-sync");
// var name=n.question("enter name: ")
// const store=name;
// var string=""
// for (let i=name.length-1;i>=0;i--) {
//    string=string+name[i]
// }
// if (store===string) {
//    console.log("its palindrome string")
// }
// else {
//    console.log("it's not a palindrome string")
// }


N=require('readline-sync').questionInt("enter");
sum=0
for (var i=0; i<=N; i++) {
   sum+=i
}
console.log(sum)

