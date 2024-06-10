from tkinter import *
from tkinter import messagebox, ttk
import subprocess

root = Tk()
root.title("Tkinter 1")
root.geometry("900x500+100+200")

# Funktsioon, mis käivitatakse nupule klõpsamisel
def click_button():
    keel = Languages_combobox.get()
    tase = Kategooria_combobox.get()
    # Failide sõnastik vastavalt valitud keelele ja tasemele
    failid = {
        ('Eesti keel', 'A2'): "testid/A2EestiKeel.py",
        ('Eesti keel', 'B1'): "testid/B1EestiKeel.py",
        ('Eesti keel', 'B2'): "testid/B2EestiKeel.py",
        ('Eesti keel', 'C1'): "testid/C1EestiKeel.py",
        ('Eesti keel', 'Testerimine'): "testid/TesterimineEestiKeel.py",
        ('English', 'A2'): "testid/A2English.py",
        ('English', 'B1'): "testid/B1English.py",
        ('English', 'B2'): "testid/B2English.py",
        ('English', 'C1'): "testid/C1English.py",
        ('English', 'Testerimine'): "testid/EnglishFullTest.py",
    }
    
    fail_avamine = failid.get((keel, tase))
    if fail_avamine:
        subprocess.Popen(["python", fail_avamine])
    else:
        messagebox.showerror("Viga", "Valitud keele ja taseme jaoks ei leitud faili.")

lbl = Label(root, text='Tere tulemast!', font=('Times New Roman', '25', 'bold'))
lbl.grid(row=1, column=1, padx=300, pady=0)

lbl1 = Label(root, text='Valige keele test', font=('Times New Roman', '15', 'normal'))
lbl1.grid(row=2, column=1, padx=300, pady=0)

Keeled = ('Eesti keel', 'English')
Languages_combobox = ttk.Combobox(root, values=Keeled)
Languages_combobox.current(0)
Languages_combobox.grid(row=3, column=1, padx=0, pady=0)

lbl2 = Label(root, text='Valige keeletase', font=('Times New Roman', '15', 'normal'))
lbl2.grid(row=4, column=1, padx=300, pady=0)

Tasemed = ('A2', 'B1', 'B2', 'C1','Testerimine')
Kategooria_combobox = ttk.Combobox(root, values=Tasemed)
Kategooria_combobox.current(0)
Kategooria_combobox.grid(row=5, column=1, padx=0, pady=0)

nupp = Button(root, text='Alusta',
              background='#555',
              foreground='#ccc',
              padx='5', pady='1',
              font='16',
              command=click_button)
nupp.grid(row=6, column=1, padx=0, pady=0)

root.mainloop()
