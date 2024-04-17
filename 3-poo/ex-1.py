class Movie:
  notes = []
  note = 0

  def __init__(self, name, yearLaunch, includedPlan,  durationMinutes):
    self.name = name
    self.yearLaunch = yearLaunch
    self.includePlan = includedPlan
    self.durationMinutes = durationMinutes

  def __str__ (self):
    return f"Filme:{self.name} - {self.yearLaunch} - {self.durationMinutes} Minutos"
  
  def add_note(self,note):
    self.notes.append(note)
    medium = sum(self.notes)/len(self.notes)
    self.note = medium
    print(f"Voce adicionou a nota {note}")
  
  def list_notes(self):
    print(f"nota medio do filme {self.note}")

  def show(self):
    print("----------------------FILME----------------------")
    print(f"Filme:{self.name} - {self.yearLaunch} - {self.durationMinutes} Minutos")
    print(f"Plano Basico: {self.includePlan}")
    print(f"Notas: {self.notes}")
    print(f"Nota: {self.note}")


movie = Movie("jujutsu kaisen",2022,True,120)
movie.show()

movie.add_note(10)
movie.add_note(9)
movie.list_notes()

movie.show()
    