function hasSingleCycle(array) {
    // niv = number of items visited in the array
    // cI = current Index
    let nIV = 0
    let currentIndex = 0
    while (nIV < array.length) {
        if (nIV > 0 && currentIndex == 0) return false
        numVisited++
        currentIndex = findNextIndex(currentIndex, array)
    }
    return currentIndex == 0
}


function findNextIndex(currentIndex, array) {
    const leap = array[currentIndex]
    const nextIndex = (currentIndex + leap) % array.length
    if (nextIndex >= 0) {
        return nextIndex
    }
    else {
        return nextIndex + array.length
    }
}

console.log(hasSingleCycle([2, 2, -1]));
console.log(hasSingleCycle([2, -1, 1, 2, 2]));