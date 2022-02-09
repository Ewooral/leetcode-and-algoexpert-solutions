function findElement(element, arrayStack) {
    for(let newArray of arrayStack) {
        if(newArray.includes(element)) {
            return true;
        }
    }
    return false;
    
}

console.log(findElement("daddy", ["ruby", "javascript", "python", "ruby"]));
