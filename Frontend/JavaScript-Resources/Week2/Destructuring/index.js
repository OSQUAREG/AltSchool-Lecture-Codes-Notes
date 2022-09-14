// DESTRUCTURING AN ARRAY
// let names = ["Adebayor", "Olubisi", "Ogunbiyi"]

// let [firstName, middleName] = names

// console.log(firstName);
// console.log(middleName);

// Get the first name
// let [name1] = names
// console.log(name1) // Adebayor

// Get the middle name
// let [, name2] = names
// console.log(name2) // Olubisi

// Get the last name
// let [, , name3] = names // "let [,,name3] = names" works too
// console.log(name3) // Ogunbiyi

// Use the REST OPERATOR to get the rest of the names
// let [name4, ...restOfNames] = names
// console.log(name4) // Adebayor
// console.log(restOfNames) // ["Olubisi", "Ogunbiyi"]


// DESTRUCTURING AN OBJECT
// let settings = { 
//     theme: "dark", 
//     fontSize: 20, 
//     fullScreen: true }
// let { theme, fontSize, fullScreen } = settings

// console.log(theme);
// console.log(fontSize);

// Get only the theme, and ASSIGN it to a NEW VARIABLE
// let { theme: newTheme } = settings
// console.log(newTheme);

// Use the REST OPERATOR to get the rest of the settings
// let { theme: newTheme1, ...restOfSettings } = settings
// console.log(newTheme1) // dark
// console.log(restOfSettings) // { fontSize: 20, fullScreen: true }


// DESTRUCTURING IN A FUNCTION
// function getUserInfo({ name, age, sex }) {
//     console.log("My name is:", name)
//     console.log("My age is:" , age)
//     console.log(`And I'm a ${sex}`)
// }

// const user = {
//     name: "John",
//     age: 23,
//     sex: "male"
// }

// getUserInfo(user) // John 23 male




