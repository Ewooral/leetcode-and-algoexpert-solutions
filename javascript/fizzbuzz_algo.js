// Challenge: fizzbuzz
// Create a function fizzbuzz that takes one number, n. fizzbuzz should loop through
//  the numbers 1 through n and push each number into the results array using the following rules:
// 1. Push the string "fizz" in place of numbers divisible by 3.
// 2. Push the string "buzz" in place of numbers divisible by 5.
// 3. Push the string "fizzbuzz" in place of numbers divisible by both 3 and 5.

// Run the test console.log to check your work.

// Hint: Check out the remainder/modulo operator: %.
const results = [];

const fizzbuzz = (n) => {
  // ADD CODE HERE...
  for (let i=1; i<n; i++){
    if(i%3===0 && i%5 === 0){
      results.push("fizzbuzz")
    }
     else if(i%3===0){
      results.push("fizz")
    }
    else if(i%5===0){
      results.push("buzz")
    }
    
    else{results.push(i)}
  }
  return results.push(n)
};

fizzbuzz(16);
console.log(results);
// should log: [1, 2, 'fizz', 4, 'buzz', 'fizz', 7, 8, 'fizz', 'buzz', 11, 'fizz', 13, 14, 'fizzbuzz', 16]


// console.log(global.process.env.path.length)


(function isEvening(){
  console.log("Good Evening")
}())
