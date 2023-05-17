''' Modules '''
import pandas as pd
import customtkinter
from CTkMessagebox import CTkMessagebox

''' Tkinter GUI '''
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.app = customtkinter.CTk() 
        self.geometry("800x600")
        self.title('Inflation DataSet')

        self.entry = customtkinter.CTkEntry(self, placeholder_text="Enter Inflation Rate",width=200)
        self.entry.grid(row=0, column=1)

        self.button = customtkinter.CTkButton(self, text="Get Info",width=100,command=self.read_data)
        self.button.grid(row=1, column=1, pady=6)

        self.textbox = customtkinter.CTkTextbox(self, width=700, height=500)
        self.textbox.grid(row=2, column=1, pady=12, padx=50)

    ''' Functions '''
    def read_data(self):
        entry_data = self.entry.get()
        df = pd.read_csv('data.csv',encoding= 'unicode_escape')
        if(entry_data != ''):
            inflation = df.loc[df['Inflation'] >= float(entry_data)]
            self.textbox.insert( '1.0', inflation)
        else:
            CTkMessagebox(title="Invalid Value", message="Enter a valid Infaltion Rate.")

if __name__ == "__main__":
    app = App()
    app.mainloop()