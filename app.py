import os
import json
from enum import Enum

contacts=[]
filename="myContats.json"

class Selection(Enum):
    ADD = 1
    DELETE = 2
    SHOW = 3
    EXIT=4
    CLEAR=5
    EDIT=6
    SEARCH=7

def menu():
    for i in Selection:
        print(f'{i.value} - {i.name}')
    return Selection(int(input("your selection:")))

def search(action):
    contactToSearch=input(f"contact To {action}:")
    for i,contact in enumerate(contacts):
        if contact["fName"]==contactToSearch:
            print(f'{contact} in {i} place')
            return i
        print('not found')
        return -1
    
def del_contact():
    search = search("delete")
    if search>-1 :del contacts[search]

def save_contacts(filename='myContacts.json'):
    with open(filename, 'w') as file:  # שימוש במשתנה 'file' במקום 'filename'
        json.dump(contacts, file, indent=4)  # שמירת רשימת הקונטקטים לקובץ
    print(f'Contacts saved to {filename}.')  # הדפסת הודעה לאחר השמירה

def exit_app():
    save_contacts()  # שמירת הקונטקטים לפני היציאה
    exit()  # יציאה מהתוכנית
    
def load_contacts_from_file(filename='myContacts.json'):
    try:
        with open(filename, 'r') as file:  # פתיחת הקובץ לקריאה
            contacts = json.load(file)  # טעינת תוכן הקובץ לתוך המשתנה 'contacts'
            print(f'Contacts loaded from {filename}.')
    except FileNotFoundError:
        print(f'No saved contacts found in {filename}. Starting with an empty list.')
        contacts = []  # יצירת רשימה ריקה אם הקובץ לא נמצא
    return contacts  # החזרת רשימת אנשי הקשר

def edit_contact():
    index = search("edit")
    if index > -1:
        print(f"Editing contact: {contacts[index]}")
        new_name = input("Enter new name (leave blank to keep current): ")
        new_age = input("Enter new age (leave blank to keep current): ")
        
        if new_name:
            contacts[index]['fName'] = new_name
        if new_age:
            contacts[index]['age'] = new_age
        
        print("Contact updated successfully.")

if __name__=='__main__':
    contacts=load_contacts_from_file(filename)
    while True:
        userselection= menu()
        if userselection== Selection.EXIT:exit_app()
        if userselection== Selection.SHOW:print(contacts)
        if userselection== Selection.CLEAR:os.system('clear')
        if userselection== Selection.ADD:contacts.append({'fName':input("your name:"),'age':input('your age:')})
        if userselection==Selection.SEARCH:search("search")
        if userselection==Selection.DELETE:del_contact()
        if userselection==Selection.EDIT:edit_contact()