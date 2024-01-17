import customtkinter as ctk
import data_system as ds


ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Baza danych medycznych")
app.geometry("500x500")
parient_found = ctk.StringVar()

def on_button_press(name):
    got_name = []
    got_name.append(ds.fetch_name(name.get()))
    parient_found.set(got_name)
    print(parient_found)



def OpenPatientFetch():
    """opening new window with patient search feature"""
    PatientFetch= ctk.CTkToplevel()

    # ta metoda powoduje problemy i jeszcz nie wiem dlaczego ale nad tym pracuje 
   # PatientFetch.grab_set()

    PatientFetch.title("Znajdz w bazie")
    PatientFetch.geometry("500x500")

    #informacja potrzebna dla programu, nie ruszac!
    name_var = ctk.StringVar()

    # guzik od wyszukania pacjenta 
    button = ctk.CTkButton(master=PatientFetch, text="Znadz w bazie danych", command=lambda: on_button_press(name_var))
    button.place(relx=0.5, rely=0.5, anchor=ctk.S)

    # pole wyszukania pacjenta
    name_entry = ctk.CTkEntry(master=PatientFetch,textvariable = name_var, font=('calibre',10,'normal')) 
    name_entry.place(relx=0.5,rely=0.5, anchor=ctk.N)

    #pole zwrotne
    name_label = ctk.CTkLabel(master=PatientFetch, text ='', font=('calibre',10, 'bold'))
    name_label.place(relx=0.5,rely=0.5, anchor=ctk.S)
    name_label.configure(text = parient_found)


# wlaczenie wyszukiwania
button = ctk.CTkButton(master=app, text="Wyszukaj pacjenta", command=lambda: OpenPatientFetch())
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

app.mainloop()
