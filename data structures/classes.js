// Defining a (pseudo) class

function Building(floors) {
    this.floors = floors;
    this.what = 'Building';
    // this.getFloors = function() {
    //     return this.floors;
    }  //  this is not best practice and should be avoided.


//creating instance of Building
var myBuilding = new Building(10);
// the NEW keyword creates an empty object
// and sets the constructor property to the function
// it was called with 

// METHOS(for all instance)
Building.prototype.getFloors = function() {
    return this.floors;
}

console.log(myBuilding.getFloors());

// if the methods are defined inside of the constructor function
// then anytime we call the function, we'd be creating a new instance
// of the methods which eats up space and ignores the relevance of the relevance
// of a function.

function GetNames(firstname, lastname, age) {
    this.firstname = firstname;
    this.lastname = lastname;
    this.age = age;
}
var myNames = new GetNames('John', 'Doe', 30);

GetNames.prototype.getLastName = function() {
    return this.lastname;
}
// when you use an arrow function in your prototype, you will
// not be able to use the this keyword. Instead, you should use
// the variable that creates the instance of the object.
GetNames.prototype.getFirstName = () => {
    return myNames.firstname;
}
// this will not work because we used the THIS keyword in an arrow function
// 
GetNames.prototype.getAge = () => {
    return this.age;
}


console.log(myNames.getLastName());
console.log(myNames.getFirstName());
console.log(myNames.getAge());


class Food {
    constructor(rice, beans, gari) {
        this.rice = rice;
        this.beans = beans;
        this.gari = gari;
    }
    getRice() {
        return this.rice;
    }

    getBeans() {
        return Food.beans;
    }
  
    getGari() {
        return this.gari;
    }
}
console.log("............................")

var favoriteFood = new Food('rice', 'beans', 'gari');
console.log(favoriteFood.getRice());