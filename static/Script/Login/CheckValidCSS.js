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
            ElementToChangeStateText.classList.add("change_state_of_text")
        }
    })

})