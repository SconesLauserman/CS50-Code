    /////////////////////////////////////////////////////////////////////////////
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
//vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv//
//                                  VARIABLE                                       //
//vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv//
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
let textArea = document.getElementById("TextAreaMessage")
let SendTextButton = document.getElementById("SendTextMessageButton")
let fullTextPage = document.getElementById("NoUsersShownPage")
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//
//                                  VARIABLE                                       //
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
    /////////////////////////////////////////////////////////////////////////////


// When the send text button is clicked call function Send Messages.
SendTextButton.addEventListener("click", function() {
    SendMessages()
})

// When the send text button is clicked call function Send Messages.
textArea.addEventListener("keydown", function(key) {
    if(key.key == 'Enter') { // If the user typed 'Enter' SendMessages.

        key.preventDefault(); // Prevent default behavior (line break)

        SendMessages()
    }
})


function SendMessages() { // Function to send a new message between current user and friend user.

    // Making the data to send to the backend.
    data = {
        Message: textArea.value,
        Reciver: document.getElementById("FriendUsernameDisplayButton").textContent // The user to send the data to.
    }

    // Ask the backend to send the message to the other uesr.
    fetch('/SendMessage', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },

        body: JSON.stringify(data) // Send the data to the backend

    })
        .then(response => response.text())
        .then(result => {

            // Setting the full text page to the incremented by the new message
            fullTextPage.innerHTML += result

            textArea.value = '' // Making the text area value default
            textArea.rows = 1 // Making the text area rows default

        })
        .catch(error => {
            console.error('Error:', error);
        });
}