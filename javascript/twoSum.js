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
			 if(currentValue + nextValue == targetSum){
				 return [currentValue, nextValue]
			 }
			 
		 }
		
	}
	return []
	
}
console.log(twoNumberSum([-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163));