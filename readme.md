# Contact Management Application

This is a simple command-line application written in Python for managing a list of contacts. The application allows you to add, delete, show, search, and edit contacts, as well as save them to a JSON file.

## Features

	•	Add Contacts: Add new contacts with a name and age.
	•	Delete Contacts: Delete existing contacts by searching for their name.
	•	Show Contacts: Display the list of all contacts.
	•	Search Contacts: Search for a contact by their name.
	•	Edit Contacts: Edit the details of existing contacts (name and/or age).
	•	Clear Screen: Clear the command-line screen.
	•	Save Contacts: Automatically save contacts to a JSON file before exiting.
	•	Load Contacts: Automatically load contacts from a JSON file when the application starts.


## How to Use

	1.	Menu Options: The application displays a menu with the following options:
	•	1 - ADD: Add a new contact.
	•	2 - DELETE: Delete an existing contact.
	•	3 - SHOW: Show all contacts.
	•	4 - EXIT: Save contacts and exit the application.
	•	5 - CLEAR: Clear the screen.
	•	6 - EDIT: Edit an existing contact (not yet implemented).
	•	7 - SEARCH: Search for a contact by name.
	
    2.	Adding a Contact:
	•	Select option 1 from the menu.
	•	Enter the contact’s name and age when prompted.
	
    3.	Deleting a Contact:
	•	Select option 2 from the menu.
	•	Enter the name of the contact you want to delete.
	
    4.	Viewing Contacts:
	•	Select option 3 to view all contacts currently saved.
	
    5.	Exiting the Application:
	•	Select option 4 to save all contacts and exit the application.
	
    6.	Searching for a Contact:
	•	Select option 7 to search for a contact by their name.

## Files

	•	main.py: The main Python file containing the application logic.
	•	myContacts.json: The JSON file where contacts are saved. This file is automatically created when you first save a contact.

## Installation

	1.	Clone the repository:
    git clone https://github.com/yourusername/your-repo-name.git
    
    2.	Navigate to the project directory:
    cd your-repo-name

    3.	Run the application:
    python main.py

    Dependencies

	•	Python 3.x

## Future Improvements

	•	Implement the Edit Contact feature.
	•	Add validation for input data.
	•	Improve the user interface for better usability.
	•	Implement unit tests for the application.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

Contributing

Feel free to fork this project and make your changes. Pull requests are welcome!
