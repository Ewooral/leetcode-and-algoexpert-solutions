import { performance } from 'perf_hooks';/*
  Insertion sort!
  
  Be sure to call your function insertionSort!
  
  The idea here is that the beginning of your list is 
  sorted and everything else is assumed to be an 
  unsorted mess.
  The outer loop goes over the whole list,
   the index of which signifies where the "sorted" 
   part of the list is. The inner
  loop goes over the sorted part of the list and 
  inserts it into the correct position in the array.
  
  Like bubble sort, there's a visualization mechanism
   available to you. Just call snapshot(myArray) at the
    beginning of
  your inner loop and it should handle the rest for you!
  
  And you put xdescribe instead of describe if you want to 
  spend running the unit tests.  
*/

function insertionSort(nums) {
  // code goes here
  let t0 = performance.now();
  let sorted;
  for (let i = 0; i < nums.length; i++) {
    if (sorted) {
      sorted = false;
      continue;
    }
    for (let j = i; j > 0; j--) {
      if (nums[j] < nums[j - 1]) {
        let temp = nums[j];
        nums[j] = nums[j - 1];
        nums[j - 1] = temp;
      } else {
        break;
      }
    }
  }
  let t2 = performance.now()
    console.log(t2 - t0);
    return nums;
}

function insertion_Sort(nums) {
    // code goes here
    let t0 = performance.now();
  for (let i = 1; i < nums.length; i++) {
    let numberToInsert = nums[i]; // the numberToInsert number we're looking to insert
    let j; // the inner counter

    // loop from the right to the left
    for (j = i - 1; nums[j] > numberToInsert && j >= 0; j--) {
      // move numbers to the right until we find where to insert
      nums[j + 1] = nums[j]; // moving nums backwards to the right
    }

    // do the insertion
    nums[j + 1] = numberToInsert;
  }
    let t2 = performance.now()
    console.log(t2 - t0);
  return nums;
}

console.log(insertionSort([10, 5, 3]));
console.log(insertion_Sort([-1,8,2.2,-12,0,14,3,5,7,9,10]));
