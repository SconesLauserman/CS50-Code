    /////////////////////////////////////////////////////////////////////////////
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
//vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv//
//                                  VARIABLE                                       //
//vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv//
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
let InputElement = document.getElementById("UsernameInputElement");
let InputTextElement = document.getElementById("InputUsernameTextElement");
let allElementsToChangeState = document.querySelectorAll(".change_state_of_text, .change_state_of_input")
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//
//                                  VARIABLE                                       //
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
    /////////////////////////////////////////////////////////////////////////////


// When the browser/window loads run the function.
window.addEventListener("load", function() {
  
  // Making a for each loop loop thru all the elemetnts to chnage and remove all the change_state_of_text class from them.
  allElementsToChangeState.forEach(ChangeToDefaultElement => {

    ChangeToDefaultElement.classList.remove("change_state_of_text")

  })  
})

// Making a hashmap that has the login data type as key and the right regex as the value.
KeyToRegex = {
    FirstName: /^[a-zA-Z]*$/,
    LastName: /^[a-zA-Z]*$/,
    Username: "Username",
    Email: "Email",
    Password: /^[^,]*$/,
    Code: /^[0-9].+$/
}

// Making a for loop thru each element that should change in some caess.
allElementsToChangeState.forEach(ElementToChangeState => {

    // Get the text next to the input field using the built in library nectElemtentSibling.
    let ElementToChangeStateText = ElementToChangeState.nextElementSibling

    // When the user starts to write on one of the register data fields, then add the change_state_of_text class to them.
    ElementToChangeState.addEventListener("focus", function() {
        ElementToChangeStateText.classList.add("change_state_of_text")
    })

    // When the user stops writing on one of the register data fields, then do the following...
    ElementToChangeState.addEventListener("blur", function() {

        // If the element still has not value just turn it into the default settings.
        if(ElementToChangeState.value == '') {
            ElementToChangeStateText.style.color = 'rgba(0, 0, 0, 0.5)'
            ElementToChangeStateText.style.backgroundColor = 'white'
            ElementToChangeStateText.classList.remove("change_state_of_text")
        }
        // If the element has something in it do the following.
        else {

            if(KeyToRegex[ElementToChangeState.name] === "Username") { // Check if the regex value is Username then make backend call.

                fetch('/CheckUsernameValid', { // Ask backend if the username is valid.
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    
                    body: JSON.stringify(ElementToChangeState.value) // Send the username as the json data.

                })
                    .then(response => response.text())
                    .then(result => {
                        // If the username was valid make the username element green; else: red.
                        if(result == 'Valid') {
                            ElementToChangeStateText.style.backgroundColor = 'green'
                        }else {
                            ElementToChangeStateText.style.backgroundColor = 'red'

                        }
                })
            }
            else if(KeyToRegex[ElementToChangeState.name] === "Email") { // Check if the regex value is Email then make backend call. 
                fetch('/CheckEmailValid', { // Ask backend if the Email is valid.
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    
                    body: JSON.stringify(ElementToChangeState.value) // Send the Email as the json data.

                })
                    .then(response => response.text())
                    .then(result => {
                        // If the Email was valid make the username element green; else: red.
                        if(result == 'Valid' && /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/.test(ElementToChangeState.value)) {
                            ElementToChangeStateText.style.backgroundColor = 'green'
                        }else {
                            ElementToChangeStateText.style.backgroundColor = 'red'

                        }
                })
            }
            else {
                // If the regex that is set to the register data element is true then set it to green; else: red.
                if(KeyToRegex[ElementToChangeState.name].test(ElementToChangeState.value)) {
                    ElementToChangeStateText.style.backgroundColor = 'green'
                } else {
                    ElementToChangeStateText.style.backgroundColor = 'red'
                }  
            }  
        }
    })

})