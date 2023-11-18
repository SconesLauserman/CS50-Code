    /////////////////////////////////////////////////////////////////////////////
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
//vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv//
//                                  VARIABLE                                       //
//vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv//
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
let FullUserListUI = document.getElementById("FullUserList")
let UserSearchInput = document.getElementById("SearchUserInput")
let UsernameInClassOnclickDocument
let FullChatTextPitDocument = document.getElementById("NoUsersShownPage")
let groupAddButtonOnclick = document.getElementById("FullGroupAddContainerOnclick")
let friendAddButtonOnclick = document.getElementById("FullUserAddContainerOnclick")
let UsernameSearchInput = document.getElementById("SearchUserInput")
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//
//                                  VARIABLE                                       //
//^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^//
//::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::://
    /////////////////////////////////////////////////////////////////////////////


function SearchUsernames(username) { 
    fetch('/SearchUsernames', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        
        body: JSON.stringify(username) 
    
    })
        .then(response => response.text())
        .then(result => {

            FullUserListUI.innerHTML = result // Set the UL of usernames to the return response.
        
        })
        .catch(error => {
            console.error('Error:', error);
        });
}


// When the button 'Add Friend' is clicked run the function.
friendAddButtonOnclick.addEventListener("click", function() {

    // Add a search bar where the user can type the new friend username.
    FullUserListUI.innerHTML += "<li><input placeholder='Friend Username' type='text' id='NewFriendInputBar'></li>"

    // Getting the just defined HTML element fore gettings the new friend username.
    let NewUserFriendInputBar = document.getElementById("NewFriendInputBar")

    // When the user presses a key run the function.
    NewUserFriendInputBar.addEventListener('keydown', function(key) {

        // If the pressed down key was 'Enter' then ask backend to add the new user to the friends list.
        if(key.key === 'Enter') {
        
            fetch('/AddUserToList', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
        
                body: JSON.stringify(NewUserFriendInputBar.value) // Send the friends username as the json data.
        
            })
                .then(response => response.text())
                .then(result => {
                    
                    FullUserListUI.innerHTML = result // Settings the full user list to the old userlist with the new friend included
        
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    })
})


// Function to set event listener fore when the current user clicks one of his friends usernames.
function setEventListeners() {

    // Get all the elements with the 'username_in_list_onclick' class(all the li usernames).
    UsernameInClassOnclickDocument = document.querySelectorAll(".username_in_list_onclick")

    // Making a for each loop thu each of the HTML elements with the class tag 'username_in_list_onclick'.
    UsernameInClassOnclickDocument.forEach(UsernameDocument => {

        // Add a event listener fore when any of the username HTML elements is clicked.
        UsernameDocument.addEventListener("click", function() {

            // Simply saying all the older clicked username tags should have a background of default.
            document.querySelectorAll(".username_in_list_onclick").forEach(ListUsernameDocument => {
                ListUsernameDocument.style.backgroundColor = '#C97D60'
            })

            // Gettings the element that shows who the current user is talking to.
            let usernameDisplayButton = document.getElementById("FriendUsernameDisplayButton")
            usernameDisplayButton.innerText = UsernameDocument.textContent
            usernameDisplayButton.style.width = usernameDisplayButton.offsetWidth

            // Settting new clicked username element to outstand, from the rest.
            UsernameDocument.style.backgroundColor = '#e60023'

            
            // Ask the backend to return us the two users chat messages with each other.
            fetch('/DisplayUserChatHistory', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },

                body: JSON.stringify(UsernameDocument.textContent) // Giving the () of the value of the just now clicked username document.
            
            })
                .then(response => response.text())
                .then(result => {
            
                    FullChatTextPitDocument.innerHTML = result // Setting the pit of Chat Data to be the chat data between current user and friend user.
            
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        })
      });   
}


// When the browser/window loads run the function.
window.addEventListener("load", function () {

    // Set the ul element of usernames to be filled with all current friend users.
    SearchUsernames("")
    
    setTimeout(() => {
    setEventListeners() // Run the function setEventListeners after 5 miliseconds due to speed of backend response
    }, 50);


    // Make a constant code runner to load new chat data.
    setInterval(() => {

        // Get the friend the user is talking to.
        let FriendUser = document.getElementById("FriendUsernameDisplayButton")

        if(FriendUser.textContent != '') { // If the user is talking to someone do the following

            // Ask the backend to Display the users chat history.
            fetch('/DisplayUserChatHistory', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },

                body: JSON.stringify(FriendUser.textContent) // Send the user the current user is talking with, to the backend
            
            })
                .then(response => response.text())
                .then(result => {
                
                    FullChatTextPitDocument.innerHTML = result // Set the Chat Pit of data to be the backends response.
                
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
    }, 5000);
})