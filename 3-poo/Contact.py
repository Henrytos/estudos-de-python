class Contact:
  def __init__(self,name,phone,email):
    self.__name = name
    self.__phone = phone
    self.__email = email
  
  def get_data(self):
    return {
      "name":self.__name,
      "phone":self.__phone,
      "email":self.__email
    }
  
  def __str__(self) -> str:
    return f"{self.__name} - {self.__phone} - {self.__email}"

  def show(self) -> str:
    return f"{self.__name} - {self.__phone} - {self.__email}"



