class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}"
    

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def remove_contact(self, contact):
        self.contacts.remove(contact)

    def display_contacts(self):
        if not self.contacts:
            print("Lista de Contatos vazia.")
        else:
            for contact in self.contacts:
                print(contact)
                print("----------------------")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print(contact)
                return
        print("Contato não encontrado.")



contact_book = ContactBook()

while True:
    print("\n--- Opções Agenda de Contatos ---")
    print("1. Adicionar Contato")
    print("2. Remover Contato")
    print("3. Listar Contatos")
    print("4. Buscar Contato")
    print("5. Sair")

    choice = input("Escolha a opção: ")

    if choice == "1":
        name = input("Informe o nome: ")
        phone = input("Informe o telefone: ")
        email = input("Informe o e-mail: ")
        contact = Contact(name, phone, email)
        contact_book.add_contact(contact)
        print("Contato adicionado com sucesso.")
    elif choice == "2":
        name = input("Informe o nome para remover: ")
        contact = contact_book.search_contact(name)
        if contact:
            contact_book.remove_contact(contact)
            print("Contato removido com sucesso.")
    elif choice == "3":
        contact_book.display_contacts()
    elif choice == "4":
        name = input("Procure por um nome: ")
        contact_book.search_contact(name)
    elif choice == "5":
        print("Saindo do programa.")
        break
    else:
        print("Opção Inválida. Utilize uma opção de 1 a 5")