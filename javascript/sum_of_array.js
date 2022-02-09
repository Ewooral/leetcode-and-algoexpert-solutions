/**
 * Given an array of integers, find the sum of its elements.

For example, if the array , , so return .

Function Description

Complete the simpleArraySum function in the editor below. It must return the sum of the array elements as an integer.

simpleArraySum has the following parameter(s):

ar: an array of integers
Input Format

The first line contains an integer, , denoting the size of the array.
The second line contains  space-separated integers representing the array's elements.

Constraints


Output Format

Print the sum of the array's elements as a single integer.

Sample Input

6
1 2 3 4 10 11
Sample Output

31
 */

/* Another way of importing the
 lodash packagae is 
 var lodash = require('lodash');
*/
import pkg from 'lodash'; const { sum: _sum } = pkg; 

var arr = [3, 6, 1, 5, 8];
var sum = _sum(arr);
console.log(sum); 

//Use the reduce() Method to Sum an Array in a JavaScript Array
/**
 * The reduce() method loops over the array and calls 
 * the reducer function to store the value of array 
 * computation by the function in an accumulator. 
 * An accumulator is a variable remembered throughout
 *  all iterations to store the accumulated results of
 *  looping through an array. We can use this to iterate
 *  through the array, add the element’s 
 * value to the accumulator and get the sum of the array.
 */
const array = [1, 2, 3, 4];
const reducer = (accumulator, curr) => accumulator + curr;
console.log(array.reduce(reducer));

// No library
function addArrays(arrays){
    var sumTotal = 0; 
    for(let value of arrays){
        sumTotal += value;
    }
    return sumTotal;
}
console.log("The sum of the array is: " + addArrays([3, 4, 6, 7]));