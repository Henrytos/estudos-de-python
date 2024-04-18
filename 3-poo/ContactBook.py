class ContactBook:
  __contacts = []

  @classmethod
  def add_contact(self,contact):
    print("ADICIONANDO CONTATO")
    self.__contacts.append(contact.get_data())

  @classmethod
  def show_contacts(self):
    print("LISTANDO CONTATOS")
    for contact in self.__contacts:
      print(self.show_contact(contact))

  @classmethod
  def show_contact(self,contact):
    return f"{contact['name']} - {contact['phone']} - {contact['email']}"
  
  @classmethod
  def seacrh_contact(self,name):
    print("BUSCANDO CONTATO")
    for contact in self.__contacts:
      if contact['name'].lower() == name.lower():
        print(self.show_contact(contact))
        return contact
    print("Contato não encontrado")

  @classmethod 
  def remove_contact(self,name):
    print("REMOVENDO CONTATO")
    for contact in self.__contacts:
      if contact['name'].lower() == name.lower():
        self.__contacts.remove(contact)
        return
    print("Contato não encontrado")