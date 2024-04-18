from Contact import Contact
from ContactBook import ContactBook

contato = Contact("henry","11967603378","franzhenry46@gmail.com")


ContactBook.add_contact(contato)
ContactBook.show_contacts()
ContactBook.seacrh_contact("henry")
ContactBook.remove_contact("henry")
ContactBook.show_contacts()
