function makeATuple(input){
    let output = [];
    for(  let i of input){
        for(let j of input){
            output.push([i,j]);
        }
    }
    return output;
}

console.log(makeATuple([1,2,5,4,2]))

