// CREATE an array (Using class method)
// let users = new Array();

// let items = ["John", "Mary", "Yemi", 20, 25.6, { theme: "dark" }];

// console.log(items)
// console.log(items.length)


// CREATE an array of strings called animals.
// let animals = ["Lion", "Tiger", "Pig"]
// index ==>  [ 0,        1       2  ]

// GET values from the array
// alert(animals[1]) //Lions
// alert(animals[2]) //Tiger

// UPDATE a value in the array
// animals[2] = { name: "Goat", type: "herbivores" } // ["Lions", "Tiger", "Goat"]
// console.log(animals)


// GET the LENGTH of the array
// console.log(animals.length) // 3 


// ARRAY METHODS

// .PUSH: ADD a value to the end of the array
// animals.push("Cow")
// console.log(animals) // ["Lions", "Tiger", "Goat", "Cow"]

// .POP: REMOVE a value from the end of the array
// animals.pop()
// console.log(animals) // ["Lions", "Tiger"]


// .SHIFT: REMOVE a value from the beginning of the array
// animals.shift()
// console.log(animals) // ["Tiger",  "Pig"]

// .UNSHIFT: ADD a value to the beginning of the array
// animals.unshift("Cheetah")
// console.log(animals) // ["Cheetah", "Lions", "Tiger", "Pig"]


// .INDEXOF: GET the INDEX of a value
// console.log(animals.indexOf("Tiger")) // 1
// console.log(animals.indexOf("Elephant")) // -1


// GET a SLICE of the array
// let animals = ["Lions", "Tiger", "Pig", "Cheetah", "Jaguar"]

// console.log(animals.slice(0,2)) // start-index: 0 and end-index: 2 (-1) ['Lions', 'Tiger']
// console.log(animals.slice(2)) // ['Pig', 'Cheetah', 'Jaguar']


// GET a COPY of the array
// let copyOfanimals = animals.slice()


// .REVERSE the array
// animals.reverse()
// console.log(animals) 


// .SORT the array
// animals.sort()
// console.log(animals) //  ['Lion', 'Pig', 'Tiger']



// ITERATE OVER THE ARRAY

// let animals = ["Lion", "Tiger", "Pig"]


// FOR...OF LOOP
// ITERATE over the array with "for...of" Loop. 
// NB: Here, you get the value

// for (let animal of animals) {
//     console.log(`This animal is: ${animal}`)
// }


// FOR...IN LOOP
// ITERATE over the array with "for...in" Loop. 
// NB: Here, you get the index.

// for (let index in animals) {
// console.log(`The index is ${index} and the value is ${animals[index]}`)
// }


// FOREACH LOOP
// ITERATE over the array with ".forEach" Loop. 
// NB: this takes in a call-back function to loop.

// function displayEachAnimal(animal) {
//     console.log(`This animal is: ${animal}`)
// }
// animals.forEach(displayEachAnimal)

// Instead, we can also use an ARROW function with the ".forEach" Loop. 
// NB: this can take in a call-back function. this is cleaner and smarter.

// animals.forEach((animal) => {
//     console.log(`This animal is: ${animal}`)
// })

//  ...or...
// animals.forEach((animal) => console.log(`This animal is: ${animal}`))

// ...or...
// animals.forEach(function(animal) {
//     console.log(`This animal is: ${animal}`)
// })


// .MAP FUNCTION
// ITERATE over the array with ".MAP" function. 
// NB: this also take in a call-back function. Useful for applying transformation to an array.

let usernames = ["john", "azeez", "ade", "akintude"]

// These methods returns the result in an array...
let usernameInUpperCase = usernames.map((username) => {
    const transformedUsername = username.toUpperCase() // transforms and stores it in the variable: transformedUsername.
    return transformedUsername;
})

console.log(usernameInUpperCase) // returns elements in an array


// ...or even more simplified (without the return keyword)...
// let usernameInUpperCase2 = usernames.map((username) => username.toUpperCase()) // transforms and stores it in the variable: usernameInUpperCase.

// console.log(usernameInUpperCase2) // returns elements in an array


// ...or can also be used like this (with the return keyword)...
// let usernameInUpperCase3 = usernames.map((username) => {
//     return username.toUpperCase()
// })

// console.log(usernameInUpperCase3) // returns elements in an array


// ...or ordinarily (without the transformation)...
// let usernameMapList1 = usernames.map((username) => username)
// // or like this...
// let usernameMapList2 = usernames.map((username) => {
//     return username
// })

// Note: when using the curly brackets after the arrow symbols, the return keyword should end the function. Else, no need.

// console.log(usernameMapList1) // returns elements in an array
// console.log(usernameMapList2) // returns elements in an array


// But logging the result within the function...
// let usernameInUpperCase4 = usernames.map((username) => console.log(username.toUpperCase())) // transforms and returns elements but not in an array form

// console.log(usernameInUpperCase4) // then calling the function returns an array with undefined data type.


// FILTER FUNCTION
// ITERATE over the array with "FILTER" function. 
// NB: this also take in a call-back function.

// let populations = [200, 100, 30, 4, 5, 60]

// console.log(`Default population: ${populations}`)

// let populationGreaterThan30ButLessThan200 = populations.filter((population) => {
//     if (population > 30 && population < 200){
//         return population
//     }
// })
// console.log(populationGreaterThan30ButLessThan200)


// ...even more simplified (without if and return keyword)...
// let populationGreaterThan30ButLessThan200_2 = populations.filter((population) => (population > 30 && population < 200));

// console.log(populationGreaterThan30ButLessThan200_2)


// 2D Arrays
// let matrix = [
//     [1, 2, 3], // 0 
//     [4, 5, 6], // 1
//     [7, 8, 9]  // 2
// ];// 0  1  2

// console.log(matrix[0][1]) // 2
// console.log(matrix[1][2]) // 6
// console.log(matrix[2][0]) // 7

