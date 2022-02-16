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
    this.lastname = lastname ;
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
        this.Rice = rice;
        this.Beans = beans;
        this.Gari = gari;
        console.log("My food is: ", this.getRice());
        console.log(this)
    }
    getRice() {
        return this.Rice;
    }

    getBeans() {
        return Food.Beans;
    }
  
    getGari() {
        return this.Gari;
        
    }
    
}
console.log("............................");

var favoriteFood = new Food('rice', 'beans', 'gari');
console.log("Fav 1: ", favoriteFood.getRice());
console.log("Fav 2: ", favoriteFood.getBeans());
console.log("Fav 3: ", favoriteFood.getGari());




// reference type

var obj1 = {value: 10};
var obj2 = obj1;
var obj3 = {value: 10};
obj1 = {value:35};

console.log(obj1)
console.log(obj2)
console.log(obj1 === obj2)
console.log(obj1 === obj3)
console.log(obj1)
console.log(obj3)

