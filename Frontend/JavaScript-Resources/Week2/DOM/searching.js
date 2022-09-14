// Get element by ID
// const h1 = document.getElementById("h1_text")
// console.log(h1)

// Get properties from the selected element
// console.log(h1.id) // returns "h1_text"
// console.log(h1.innerText) // returns "Hello World"
// console.log(h1.innerHTML) // returns "<h1>Hello World</h1>"
// console.log(h1.style.color) // returns "rgb(0, 0, 0)"
// console.log(h1.style.fontSize) // returns "20px"
// console.log(h1.style.backgroundColor) // returns "rgb(255, 255, 255)"

// Change properties of the selected element
// h1.id = "new_id"
// h1.innerText = "New Text"
// h1.innerHTML = "<h1>New HTML</h1>"
// h1.style.color = "red"
// h1.style.fontSize = "30px"
// h1.style.backgroundColor = "yellow"


// Get elements by CLASS NAME
// const h1_class = document.getElementsByClassName("h1_class")
// console.log(h1_class)


// Get elements by TAG NAME
// const h1_tag = document.getElementsByTagName("table")
// console.log(h1_tag)


// Get elements by QUERY SELECTORS

// querySelector() returns the first element that matches the specified CSS selector(s) in the document

// const tr = document.querySelector("tr") 
// console.log(tr)

// After selecting, you work with the element
// tr.innerText = "New Table Row"

// TAG Query Selector
// const h1 = document.querySelector("h1")
// console.log(h1)

// CLASS Query Selector (uses . before classs name)
// const tableElem = document.querySelector(".my_table")
// console.log(tableElem)

// ID Query Selector (uses # before id name)
// const tableElem2 = document.querySelector("#h1_text")
// console.log(tableElem2)


// Get elements by QUERY SELECTOR ALL

// querySelectorAll() returns a static NodeList containing all elements that match the specified CSS selector(s) in the document
const trs = document.querySelectorAll("tr") // returns a NodeList of all <tr> elements
console.log(trs)

// After selecting, you work with the NodeList
// trs[1].innerHTML = "<td>New Table Column</td><td>New Table Number</td>"


// loop through NodeList, and change the color of each <td> element
// for (let i = 0; i < trs.length; i++) {
//     trs[i].style.color = getRandomColor()
// }

// function getRandomColor() {
//     const randomColors = ["red", "green", "blue", "yellow", "orange", "purple"]
//     return randomColors[Math.floor(Math.random() * randomColors.length)]
// }


// Advanced searching: See https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors


// Get elements by COMBINATORS

// CHILD combinator
// const secondTr = document.querySelector("table > tbody > tr > td.r_table_data")
// console.log(secondTr)

// DESCENDANT combinator
// const h1_elem = document.querySelector("body h1")
// console.log(h1_elem)

// const tableHeader_elem = document.querySelectorAll("body table tbody tr th")
// console.log(tableHeader_elem)

// const tableDetail_elem = document.querySelectorAll("body table tbody tr td")
// console.log(tableDetail_elem)

// ADJACENT SIBLING combinator
// const h1_next = document.querySelector("body h1 + h2")
// console.log(h1_next)

