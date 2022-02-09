function bubbleSort(nums){
    let swapped = false;
    do{
        swapped = false;
        for(let i = 0; i < nums.length; i++){
            if(nums[i] > nums[i + 1]){
                const temp = nums[i];
                nums[i] = nums[i + 1];
                nums[i + 1] = temp;
                swapped = true
            }
        }
    }
    while(swapped);
    return nums;

}


console.log(bubbleSort([10,5,3,8,2,6,4,7,9,1]));
console.log(bubbleSort([20,5,3,18,2,6,4,17,9,11]));

function after(count, funct){
    let counter = 0;
    return function(){
        counter++;
        if(counter === count){
            return funct.apply(this, arguments);
        }
    }

}let zzz = after(3, called);
const called = function() { console.log('hello') };
const afterCalled = after(3, called);
console.log(afterCalled()); // => nothing is printed
console.log(afterCalled()); // => nothing is printed
console.log(afterCalled()); // => 'hello' is printed
