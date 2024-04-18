class Trip:
    destinys=[]

    def __init__(self, *destinys):
        for dest in destinys:
          self.destinys.append(dest)

    def get_trip(self,i):
        return self.destinys[i]
    
    def get_list_trips(self):
        return self.destinys    
    
    def get_quantity_trips(self):
        return len(self.destinys)
    
    def get_show_list (self):
        i=0
        for dest in self.destinys:
            print(f"{i} - {dest}")
            i+=1

trips = Trip("Lençóis Maranhenses","BRAZIL")

print("E aí viajante. Temos algumas ofertas para você!")
traveler = input("Digite seu nome para começarmos: ")
print(f"{traveler} temos {trips.get_quantity_trips()} destinos que combinam com você:")

trips.get_show_list()

choice = int(input("Selecione o destino da viagem desejada: "))   


for option in trips.get_list_trips():
    if choice >= trips.get_quantity_trips(): 
        print("Esta opção não está incluída em nossos destinos.")
        break
    if choice>0 and choice<=trips.get_quantity_trips():   
        print(f"{traveler} sua viagem para {trips.get_trip(choice)} está marcada.") 
        print("Volte sempre!")
        break