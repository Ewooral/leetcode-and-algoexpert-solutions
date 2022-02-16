class Player{
    constructor(name, type) {
        this.name = name;
        this.type = type;
    }
}

class Wizard extends Player{
    constructor(name, type) {
        super(name, type); // super is used to call the constructor of the parent class
    }
}