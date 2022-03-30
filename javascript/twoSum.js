function twoNumberSum(array, targetSum) {
  // Write your code here.
	// targetSum = current + x(anynumber)
	// x = targetSum - current  
    // time complexity: O(n^2)
    // space complexity: O(1)
	let i
	let j
	for (i = 0; i < array.length; i++) {
        let currentValue = array[i]
		 for(j = i+1; j < array.length; j++) {
			let nextValue = array[j]
			 if (currentValue == nextValue){
				 continue;
			 } 
         
			 else if(currentValue + nextValue == targetSum){
				 console.log([currentValue, nextValue]) 
			 }
			 
		 }
		
	}
	return [] 
	
}
twoNumberSum([-21, 301, 12, 4, 80, 83, 65, 56, 210, 356, 9, -47], 163);
twoNumberSum([1, -1, 2, 4, -2, 8, 3, -3, -8], 0);
twoNumberSum([1, -1, 2, 4, -2, 9, 4, 3, 5, -8], 8);