const containsCommonItem = (array1:any[], array2:any[]):boolean => {
   let map:any = {};
   let value;
   let temp;
   for ( value of array1) { // traversing array1
     if(!map[value]){ // checking if array1 is in the map object, if not add it
           temp = value;
             map[temp] = true; // adding array1 to the map object
            
     }
      console.log( value, "=", array1.indexOf(value));
   }
  
   for ( let value2 of array2) { // traversing array2
        if (map[value2]){   //checking if array2 is in the map object, if yes return true
        return true;
        }
   }
    
    return false;
}
console.log(containsCommonItem(["a", "b", "c","x"], ["a", "b", "z"]));



