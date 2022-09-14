//Math operators

// // Addition
// let sumResult = 20 + 23.1;
// console.log(`The sumResult is: ${sumResult}`)

// // Subtraction
// let difference = 20 - 10;
// console.log(`The difference is: ${difference}`)

// // Multiplication
// let multiplicationResult = 20 * 10;
// console.log(`The multiplicationResult is: ${multiplicationResult}`)

// // Division
// let divisionResult = 20 / 2;
// console.log(`The divisionResult is: ${divisionResult}`)

// // Modulus
// let remainderResult = 20 % 10;
// console.log(`The remainderResult is: ${remainderResult}`)

// Exponent
// let exponentResult = 2 ** 2;
// console.log(`The exponentResult is: ${exponentResult}`)


// //Comparison Operators

// // Greater than
// console.log(2 > 1) // true
// console.log(`Greater than (2 > 1): ${2 > 1}`)

// // Less than
// console.log(10 < 3) // false
// console.log(`Less than (10 < 3): ${10 < 3}`)

// // Greater than or equal to
// console.log(2 >= 2) // true
// console.log(`Greater than or equal to (2 >= 2): ${(2 >= 2)}`)

// // Less than or equal to
// console.log(2 <= 1) // false
// console.log(`Less than or equal to (2 <= 1): ${2 <= 1}`)

// // Equality
// console.log(2 == 1) // false
// console.log(`Equality (2 == 1): ${2 == 1}`)

// // Inequality
// console.log(2 != 1) // true
// console.log(`Inequality (2 != 1): ${2 != 1}`)


// // Assignment operator
// let size = 20
// console.log(`the size is: ${size}`)

// // Increment operator
// size++ // Increases the value of size by one
// console.log(`the size++ increased size by 1 is: ${size}`)

// // Decrement operator
// size-- // Decreases the value of size by one
// console.log(`the size-- decreased size by 1 is: ${size}`)


// // Boolean operators

// // Logical OR (||)
// console.log(true || true) // true
// console.log(`for Logical OR, (true || true) returns: ${(true || true)}`)

// console.log(false || true) // true
// console.log(`for Logical OR, (false || true) returns: ${(false || true)}`)

// console.log(false || false) // true
// console.log(`for Logical OR, (false || false) returns: ${(false || false)}`)

// // Logical AND (&&)
// console.log(true && true) // true
// console.log(`for Logical AND, (true && true) returns: ${(true && true)}`)

// console.log(false && true) // false
// console.log(`for Logical AND, (false && true) returns: ${(false && true)}`)

// console.log(false && false) // false
// console.log(`for Logical AND, (false && false) returns: ${(false && false)}`)


// // Logical NOT (!)
// console.log(!true) // false
// console.log(`for Logical NOT, (!true)  returns: ${(!true)}`)

// console.log(!false) // true
// console.log(`for Logical NOT, (!false)  returns: ${(!false)}`)


// // Precedence
// let principal = 1000
// let rate = 0.05
// let years = 10

// let simpleInterest = (principal * rate * years) / 100
// console.log(`the simpleInterest is: ${simpleInterest}`)

// Precedence Table
// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_Precedence


function echo(name, num) {
    console.log("Evaluating the " + name + " side");
    return num;
}
// Notice the parentheses around the left and middle exponentiation
console.log((echo("left", 2) ** echo("middle", 3)) ** echo("right", 2));
