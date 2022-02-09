var stack = function (){
    this.storage = " ";
};

stack.prototype.push = function(val){
this.storage = this.storage.concat("***", val);
return this.storage;
};
stack.prototype.pop = function(){
var str = this.storage.slice(this.storage.
    lastIndexOf("***") + 3);
    this.storage = this.storage.
    substring(0, this.storage.lastIndexOf("***"));
    return str;
};


stack.prototype.size = function(){
};

var myWeeklyMenu = new stack();
myWeeklyMenu.push("pizza");
myWeeklyMenu.push("burger");
myWeeklyMenu.pop();
console.log(myWeeklyMenu.push("Chicken"));



