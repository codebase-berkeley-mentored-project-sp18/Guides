# JavaScript: Crash Course Part 1

## Introduction

JavaScript is the _lingua franca_ of the web - it's used universally by every website out there and has grown from a simple scripting language to a mature programming language with an enormous ecosystem. Today we'll learn basic JavaScript syntax, data types, and functions.

## Getting Started

Getting started with JavaScript is easy - all you need is a web browser. We will be using some particular features that aren't supported by older browsers, so we recommend using the [latest version of Google Chrome](https://www.google.com/chrome/).

Every modern web browser (e.g. Chrome, Firefox, Edge, and Safari) includes something called a **Web Console** which you can use to interactively execute JavaScript in the context of the current page. To open up the Web Console, **right-click** anywhere on the current page and select **Inspect** from the menu (you can also type `Control`+`Shift`+`I` on Windows or `Cmd`+`Option`+`K` on Mac). Then select the **Console** tab in the window that pops up.

You can type any valid JavaScript in this window and press enter to execute it - what's more, you can view variables and objects in the context of the current page. This can be very useful if the current page is running a script that you want to debug!

## 1. Primitives, Expressions

Let's get started and see what primitive data types and operations with them are available in JS. You should be familar with most if not all of these from Python.

### 1.1 Expressions

Basic math is straightforward in JavaScript. The addition (`+`), subtraction (`-`), multiplication (`*`) and division (`/`) operators work as in Python:

```javascript
> 1 + 1 - 1; // semicolons are optional but we will be using them throughout.
1
> 1/2*5+3;
5.5
```

Additionally, we have more advanced operators such as:
* the arithmetic modulus operator (`%`)
* boolean operations like AND (`&&`) and OR (`||`)
* the boolean NOT operator (`!`)

```javascript
> true && false;
false
> true || false;
true
> !true
false
> 17 % 4;
1
```

### 1.2 Variables

We can assign the results of expressions to variables like in Python. The main difference here is that in JavaScript, you must prefix variable declarations with a **`var`** keyword:
```javascript
> var a = 1+1;
> a;
2
> a = 3; // don't need the `var` keyword since `a` has already been declared
> 3
> var b = a = 7; // we can chain assignments and declarations too!
> b;
7
> a;
7
```

Note that you can technically omit the `var` keyword and variable declarations will still work - but this is a bad idea, because it creates the variable in the global rather than local scope! More on that later.

### 1.3 Dynamic Typing and JavaScript Primitives

#### 1.3.1 Primitive Data Types

JavaScript defines six primitive data types. Here are the four most important ones:
* **Boolean** - `true` or `false` (lowercase, not uppercase!)
* **Null** - `null` only. This is similar to `None` in Python.
* **Number** - Like (decimal) numbers in Python. Note that JS has no specific integer type! There are also special Number values like **`NaN`** and **`Infinity`** reserved for values like 1/0.
* **String** - Just like strings in Python, these are immutable. They also support useful operations like slicing, reversing, etc. More on this later.

#### 1.3.2 Dynamic Typing

Like Python, JavaScript is a **loosely typed** or a **dynamic** language. Variables in JavaScript are not directly associated with any particular value type, and any variable can be assigned (and re-assigned) values of all types:

```javascript
> var iAmANumber = 4; // iAmANumber is a Number.
> iAmANumber = true; // iAmANumber now refers to a boolean!
> iAmANumber = "I am not a number"; // iAmANumber is now a string!
```

##### Determining types with `typeof`

You can determine the type of a value in your code using the `typeof` operator, which returns a string corresponding to the type of its argument. [Read the documentation for more.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/typeof)

#### 1.3.3 Equality Comparisons

Here's where JavaScript and Python (and other languages!) really start to differ: equality comparisons in JavaScript are different in that some values that are different types can still be interpreted as "equal". For example:

```javascript
> 5 == '5';
true
> 5 != '5';
false
```

This is because JavaScript has a concept called **Sameness** that applies across types using the abstract equality operator (`==`). However, we will not be going into the (often complex) rules of sameness. Instead, we will require that you use the **strict equality operator** (`===`) and its counterpart the **strict inequality operator** (`!==`) instead, which only check for equality across identical types:

```javascript
> 5 === '5';
false
> 5 !== '5';
true
> '123' === '123';
true
```

#### 1.3.4 Operations Across Types

As we go deeper into the language we'll see that the main philosophy of JavaScript is essentially to _avoid crashing at all costs_. This means that we can play fast and loose with types, and even perform operations on values of different types! However, some operations aren't defined and will lead to some wonkiness - if in doubt, look up the operation you are applying in the [Mozilla Docs](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Arithmetic_Operators).

```javascript
> 'my favorite number is ' + 7; // String + Number --> String
"my favorite number is 7"
> 'my favorite value is ' + true; // String + Boolean --> String.
"my favorite value is true"
> 'foo' * 3; // String * Number --> NaN
NaN
> 1/0; // Division by Zero --> Infinity. In Python this would throw an ERROR!
Infinity
```

#### 1.3.5 Truthiness

Like Python, many non-boolean values are interpreted as `true` or `false` for convenience. The following values are **falsy**, e.g. they are interpreted as `false`:

* `false`
* `0`
* `""`, the empty string
* `null`, the null value
* `undefined` for a variable that does not exist. [Read more](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/undefined)
* `NaN` for Number values that do not evaluate to a meaningful number. [Read More](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/NaN)

All other values are **truthy**, e.g. interpreted as `true`.

## 2. Functions

Every function in JavaScript is a [`Function`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function) object. The main point to take away here is that **functions in JavaScript are values themselves and can be manipulated just like values**. This makes JavaScript an incredibly expressive language; here's where the real power is.

### 2.1 Defining and Calling Functions

We can define a function using a _function declaration_. The following function declaration defines a function called `makeSomeNoise` that takes in a single parameter called `yourName`.

```javascript
function makeSomeNoise(yourName) {
    return "Make some noise for " + yourName + "!!";
}
// let's call it now
makeSomeNoise("Sinho Chewi"); // --> "Make some noise for Sinho Chewi!!"
```

We can also use a _function expression_, which is just like a normal expression but returns a **function value**, which can be assigned to a variable or further manipulated:

```javascript
var makeSomeNoise = function(yourName) {
    return "Make some noise for " + yourName + "!!";
}
makeSomeNoise("Anant Sahai"); // --> "Make some noise for Anant Sahai!!"
```

### 2.2 Manipulating Functions

#### 2.2.1 Functions as Values

Just like in Python, functions can be passed around as arguments, returned from other functions, or be assigned to variables.

```javascript
function makeAdder(increment) {
    return function(inputNumber) {
        return inputNumber + increment;
    }
}
var incrementByOne = makeAdder(1);
var incrementByTwo = makeAdder(2);
incrementByOne(50); // --> 51
incrementByTwo(50); // --> 52
```

#### 2.2.2 Functional Operations

Since functions are values, we can apply some special operations to them to create new, more complex functions. Here are some such operations:

* [**Function binding**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind) - Create a new function that is bound to a particular scope or is already applied to particular arguments.
* [**Function prototype calling**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/call) - Call a function within the context of a particular scope with particular arguments.

### 2.3 Control

#### 2.3.1 Conditional Statements

JavaScript's syntax for if-else statements take the following form:

```javascript
if (CONDITION) {
    // STATEMENTS
} else if {
    // ...    
} else {
    // ...
}
```

Conditional expressions are surrounded by parentheses and the statements to be executed if the condition is true should be surrounded by curly braces.

```javascript
if (currentClass === "61A") {
    console.log("ez pz lemon sqz");
} else if (currentClass === "61B") {
    console.log("okey dokey lowkey nopey");
} else if (currentClass === "70") {
    console.log("difficult difficult lemon difficult");
} else {
    console.log("???!!???!!???");
}
```

Observe that the above code only really cares about the value of a single expression - the value of the variable `currentClass`. We can make decisions based on different cases for a single expression using the **switch** statement as well, which is essentially syntactic sugar for this special if-else situation. The expression inside `switch (EXPR)` gets evaluated and the result is matched sequentially against each `case VALUE:`. If `EXPR == VALUE` then the code inside that case block is executed. If the `default:` block is reached, then that code will be executed regardless of the expression's value.

```javascript
switch (currentClass) {
    case "61A": {
        console.log("ez pz lemon sqz");
        break;
    }
    case "61B": {
        console.log("okey dokey lowkey nopey");
        break;
    }
    case "70": {
        console.log("difficult difficult lemon difficult");
        break;
    }
    default: {
        console.log("???!!???!!???");
        break;
    }
}
```

Notice the `break` statements at the end of each case block. If `break` is omitted then the program continues matching the expression with cases even after a case block has been executed. Sometimes this is useful but often this will result in the default block always being executed. [Read the documentation on `switch` for more.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/switch)

So far our conditional controls have taken the form of _statements_ that are _executed_ rather than _evaluated_. But we can also express conditions in the form of _expressions_ that are evaluated to a value using the **conditional (ternary) operator**:

```javascript
var difficulty = (currentClass === "61A") ? "ez pz lemon sqz" : "super difficult";

// the above is equivalent to the following if-else statements::
if (currentClass === "61A") {
    difficulty = "ez pz lemon sqz";
} else {
    difficulty = "super difficult";
}
```

#### 2.3.2 Loops

**While loops** execute the body of the loop as long as a given condition is true:

```javascript
var i = 0;
while (i < 10) {
    console.log("Currently at the " + i + "th iteration of the loop");
    i++;
}
```

Notice in the above code that our loop executes 10 times, and to do this, we needed to do the following:

1. Declare and initialize a "counter variable" **before** our loop begins.
2. Check a **condition** at the start of **each iteration** of the loop.
3. Increment our counter variable at the **end** of each iteration.

We can put all of this code into its own block because all we really care about is the content of the loop. Let's do this using a **for loop**:

```javascript
for (var i = 0; i < 10; i++) {
    console.log("Currently at the " + i + "th iteration of the loop");
}
```

Sometimes when we're in the middle of an iteration of a loop, something happens that makes us want to break out of the loop. We can do this using a **break** statement:

```javascript
for (var i = 0; i < 10; i++) {
    console.log("Currently at the " + i + "th iteration of the loop");
    if (i === 7) {
        break; // this stops the loop at the end of the 7th iteration instead of the 10th
    }
}
```

## 3. Arrays

An _array_ in JavaScript is similar to a Python list: an ordered collection of values of any type that we can add to, delete from, and access by index. They are even created like Python lists:

```javascript
var badProfessors = []; // empty array
var goodProfessors = ["DeNero", "Hug", "Hilfinger"]; // non-empty array
// we can put anything inside arrays, even other arrays!
var dopeStuff = ["Berkeley", 1, ["public", "university"]];
```

We can access and assign to individual indices using square brackets:

```javascript
> var dopeStuff = ["Berkeley", 1, ["public", "university"]];
> dopeStuff[0];
"Berkeley"
> dopeStuff[0] = "UCLA";
> dopeStuff[0];
"UCLA"
```

Unfortunately (unlike Python), we can't use negative indices. To access the last element of an array, we need to use the **length** property of an array:

```javascript
> var dopeStuff = ["Andrew", "is", "GOAT"];
> dopeStuff.length;
3
> dopeStuff[dopeStuff.length - 1];
"GOAT"
```

### 3.1 Array Functions

All arrays are technically instances of the special [`Array`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array) object. This object has some very useful built-in functions.

#### 3.1.1 [`Array.map`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map)

The map function creates a new array with the results of calling a provided function on every element in the calling array. This is a lot like Python list comprehensions, except we are required to provide a function:

```javascript
> var someNumbers = [1, 4, 5, 9];
> var squaredNumbers = someNumbers.map(function(x) { return x*x; });
> squaredNumbers;
[1, 16, 25, 81]
> someNumbers; // original array is not changed
[1, 4, 5, 9]
```

#### 3.1.2 [`Array.forEach`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/forEach)

The forEach function is a lot like the map function, but does **not** create a new array, and does not return anything.

```javascript
> var someNumbers = [1, 4, 5, 9];
> someNumbers.map(function(x) { console.log(x*x); });
1
16
25
81
> someNumbers; // original array is not changed
[1, 4, 5, 9]
```

#### 3.1.3 [`Array.push`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/push)

The push function adds one or more elements to the **end** of an array (like the list.append function in Python) and returns the new length of the array.

```javascript
> var someNumbers = [1, 4, 5, 9];
> someNumbers.push(20);
5
> someNumbers;
[1, 4, 5, 9, 20]
```

#### 3.1.4 [`Array.pop`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/pop)

The pop function removes the **last** element from an array and returns that element. This method changes the length of the array. Together with the push function, this is enough to use an array as a stack.

```javascript
> var someNumbers = [1, 4, 5, 9];
> someNumbers.pop();
9
> someNumbers;
[1, 4, 5]
```

#### 3.1.5 [`Array.slice`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/slice)

The slice function returns a shallow copy of a portion of an array into a new array object selected from begin to end (end not included). The original array will not be modified. This is similar to Python's list slices.

```javascript
> var professors = ["DeNero", "Hilfinger", "Hug", "Sahai"];
> var goodProfessors = professors.slice(0, 3);
> goodProfessors;
["DeNero", "Hilfinger", "Hug"]
```

## 4. Objects

**Objects** in JavaScript are simply collections of properties, where each property has a string **name** (or _key_) and a **value**, which can also be a function or any other value. You can think of these objects as equivalent to Python dictionaries.

>Note: You may be used to using classes to define objects in Python or Java.
>JavaScript has no direct analog for classes, though a "class" declaration was introduced in the latest version of JavaScript (ES2015), it works rather differently than Python or Java classes. We will  not be covering ES2015 classes here, but you can read more about them [here](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes) if you are interested.

### 4.1 Defining Objects

Objects in JS are defined just like dictionaries in Python, using curly braces and pairs of keys and values:

```javascript
var mustang = {
    make: "Ford",
    model: "Mustang",
    year: 2009,
    isUsed: true,
    makeNoise: function() {
        return "vroom vroom";
    },
};
```

We can further abstract this away by defining a function to create objects for us (a "constructor"):

```javascript
function createCar(make, model, year) {
  return {
    make: make,
    model: model,
    isUsed: year !== 2018,
    makeNoise: function() {
      return "vroom vroom";
    },
  };
}

// call it to make a mustang
var mustang = createCar("Ford", "Mustang", 2009);
```

This is not the only way to create objects in JavaScript, and indeed there is a whole object-oriented paradigm involving something called **Object Prototypes** that attempts to mimic things like classes and inheritance - things you might be used to if you are coming to JavaScript from a Java/Python/C++ background. We will not cover prototypes, but you can [read the MDN documentation on them if you are interested.](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Inheritance_and_the_prototype_chain)

### 4.2 Object Properties

#### 4.2.1 Accessing and Assigning Properties

We can then access object properties in a couple ways:

```javascript
> mustang.year; // dot notation
2009
> mustang["year"]; // like a dictionary - bracket notation
2009
> var key = "year";
> mustang[key]; // bracket notation again
2009
```

We can assign object properties in the same ways:

```javascript
> mustang["topSpeed"]
undefined // uh oh - the object does not have this property!
> mustang["topSpeed"] = 80;
> mustang.topSpeed;
80 // now it does have the property we want.
```

We can even delete properties from objects using the `delete` operator:

```javascript
> delete mustang.topSpeed;
true // property was successfully deleted.
> mustang.topSpeed;
undefined
```

#### 4.2.2 Iterating Over Properties

There are several ways of iterating over all properties of an object. Starting with the latest version of JavaScript (which all modern browsers should support), we can use the `Object.keys(o)` function to iterate over all of the own properties of an object `o`. This function returns an array of all the keys for the own properties of the argument `o`:

```javascript
> Object.keys(mustang);
["make", "model", "year", "isUsed", "makeNoise"]
```

### 4.3 The `this` Pointer

The `this` pointer in JavaScript is a special pointer that we can use inside functions to refer to the enclosing object. For example, suppose we have a function `canDrive` for our car object that returns whether or not the car can drive at that speed:

```javascript
var car = {
    //...
    topSpeed: 130,
    canDrive: function(speed) {
        return speed > this.topSpeed;
    },
};
car.canDrive(150); // --> will return false
car.topSpeed = 200;
car.canDrive(150); // --> will return true
```

In the example, `this` allows a function defined inside the object to access properties of its enclosing object. It is intended for the same use as the `self` pointer in Python.

#### 4.3.1 The Behavior of `this`

The behavior of the `this` pointer in JavaScript is different than most other programming languages. There are 3 cases that determine what value `this` is bound to:

##### 4.3.1.1 The Global Scope

```javascript
this;
```

When using `this` in the global scope, it will refer to what's known as the _global object_, which is typically the `window` object in web browsers.

##### 4.3.1.2 Calling a Function

```javascript
someFunction();
```

The above code may be executed in any context (within another function, in the global scope, in a loop...) and `this` will still refer to the _global object_ when evaluated inside the body of `someFunction`.

##### 4.3.1.3 Calling an Object Property

```javascript
object.someFunction();
```

In this example, `this` will refer to `object` when evaluated inside the body of `object.someFunction`.

> Note: We do not cover object prototypes in this guide, but the `new` operator also changes the behavior of `this` so that
> it refers to the newly created object.

##### Common Pitfalls

The apparently strange behavior of `this` was designed to allow for more flexibility in the language. Unfortunately, it can be confusing to get and even experienced JavaScript programmers will fall into the trap of binding `this` to the wrong thing.

Consider the following code, in which we define a hero character and a function that makes it take damage:

```javascript
var hero = {
  name: "Gandalf",
  health: 500,
  takeDamage: function(dmg) {
    this.health = Math.max(this.health - dmg, 0);
  },
};

var attacks = [100, 150, 250];
attacks.forEach(hero.takeDamage); // <-- doesn't do what we want!
console.log(hero.health);
```

The above code is intended to make `hero` take a total of 100 + 150 + 250 = 500 damage. Instead, it takes no damage whatsoever after executing the code. This is because when we pass in `hero.takeDamage` as an argument to `forEach`, the function is then executed as a regular function (see 4.3.1.2) rather than as an object property (see 4.3.1.3). There are a couple ways to fix this; one way is to change what we pass into `forEach` so that we explicitly call our function as an object property:

```javascript
attacks.forEach(function(dmg) {
  hero.takeDamage(dmg);
});
```

The above works, but is a little verbose. Here's a better way: we can **[bind](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Function/bind)** `hero.takeDamage` so that whenever `this` is used inside the function body, it will _always_ refer to what we want it to refer to (the `hero` object).

```javascript
attacks.forEach(hero.takeDamage.bind(hero));
```

The above creates a new function that is identical to `hero.takeDamage`, but is **bound** to the `hero` object permanently. So when we pass it as an argument to `forEach`, even though the function gets executed as a regular function, since we've bound its `this` pointer permanently, it will execute as intended.

### 4.4 Comparing Objects

JS Objects are a reference type. This means that two distinct objects are never equal, even if they have the exact same properties. Only comparing the same object reference with itself returns true.

```javascript
// Two variables, two distinct objects with the same properties
var fruit = {name: 'apple'};
var fruitbear = {name: 'apple'};

fruit === fruitbear; // --> false
apple = fruit; // apple refers to the same object as fruit
fruit === apple; // --> true
```
