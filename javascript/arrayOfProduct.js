class Solution1{
    constructor(y){
        this.arrayOfProduct = (array) => 
        {
            let product = array.map((x) => 1)

            for(let i= 0; i < product.length; i++)
            {
                let runningProduct = 1;
                for(let j= 0; j < product.length; j++){
                    if (i != j){
                        runningProduct *= array[j];
                        product[i] = runningProduct;
                    }
                }
            }
              return product;
        };

        this.w = (u) => y**2 + u;
   
    }
}

let newArray = new Solution1(2);
console.log(newArray.w(20));
console.log(newArray.arrayOfProduct([5, 1, 4, 2]));
console.log(newArray.arrayOfProduct([12, 10, 8, 6, 5, 2]));


