// DIFFERENCE BETWEEN A MAP AND AN OBJECT DATA STRUCTURE
// A Map DS can take different kind of keys WHILE Object DS cannot.
// In Objects DS, the keys are converted to string. BUT in Map DS, most data type can be used as keys

// CREATING a Map with the new keyword
// let map = new Map()

// ADD VALUES to the map
// map.set(1, "An integer key")
// map.set(true, "A boolean key")

// let mary = {name : "Mary", age: 20} // this is an object. defining an object
// map.set(mary, "An object key") // using the defined object as a key

// console.log(map)

// Creating same Array with Object DS
// let userMap = {
//     1: "An integer key",
//     true: "A boolean key",
//     mary: "An object key",
// }
// console.log(userMap)

// Display the KEYS
// console.log(map.keys())

// Display the VALUE
// console.log(map.values())

// Display the ENTRIES
// console.log(map.entries())

// Display the size
// console.log(map.size)

// Check if a key exists
// console.log(map.has(1))

// Remove a key
// map.delete(1)
// console.log(map)

// Iterate over the map using "for...of" Loop
// for (let entry of map) {
//     console.log(entry) // gives you a key-value pair
//     console.log(`the key is: ${JSON.stringify(entry[0])} and the value is: ${JSON.stringify(entry[1])}`)
// }

// CONVERT the map to an array
// let mapArray = Array.from(map)
// console.log(mapArray)

// CONVERT the map to an object
// let mapObject = Object.fromEntries(map)
// console.log(mapObject)

