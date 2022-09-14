// CREATING A NEW ELEMENT

// CREATE element node
const newElem = document.createElement("span") // Can't see it yet because we haven't inserted it to the DOM

// ADD content and style to the new element
// newElem.innerText = "This is a Span element"
// newElem.style.color = "red"

// INSERT the new element to the END of body element
// document.body.append(newElem)

// INSERT the new element to the BEGINNING of body element
// document.body.prepend(newElem)

// INSERT the new element after the first table element using insertBefore
// document.body.insertBefore(newElem, document.querySelector("table"))

// INSERT element in specific position using insertAdjacentHTML
// const secondTable = document.querySelectorAll("table")[1]
// secondTable.insertAdjacentHTML("afterbegin", "<h1>Hello New Section</h1>")
// Other variants are "beforebegin", "afterbegin", "beforeend", "afterend"


// REMOVING an element
// select the element to remove
// const elemToRemove = document.querySelector("h1")
// elemToRemove.remove()


// CLONING an element
// const elemToClone = document.querySelector("h1")
// const clonedElem = elemToClone.cloneNode(true)
// document.body.append(clonedElem)
