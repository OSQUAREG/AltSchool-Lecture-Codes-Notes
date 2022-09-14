alert("Welcome to my Page")
getUserData()
alert("Good bye")


// Validation Functions

function validateUsername(username) {
    if (!username) return false;
    if (username.length > 10) return false;
    return true
}

function validatePassword(password) {
    if (!password) return false;
    if (password.length < 6) return false;
    if (password.length > 10) return false;
    return true;
}


function getUserData() {
    let username = prompt("Enter your Username")
    while (!validateUsername(username)) {
        if (username === null) return username = prompt("Enter your Username. Username must be less than 10")
    }

    let password = prompt("Enter your Password")
    while (!validatePassword(password)) {
        if (password === null) return password = prompt("Enter your password. Password must be greater than 6")
    }

    let passwordAgain = prompt("Enter your Password again")
    while (passwordAgain !== password) {
        if (passwordAgain === null) return passwordAgain = prompt("Password does not match. Confirm your password.")
    }

    const userData = userStore[username]
    if (!userData) {
        alert(`User ${username} does not exist. Please register`)
        return
    }

    if (userData.password !== password) {
        alert(`Password is incorrect. Please try again`)
        return
    }

    alert('Showing details for ${username}')

}

