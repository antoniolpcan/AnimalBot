from tkinter import *
from tkinter import messagebox
from .TKChat import TKChat

class TKMain():

    def __init__(self):  

        self.window = Tk()
        
        self.bg_color = "white"
        self.button_color = "#7EBFB0"
        self.button_cancel = "#EC9F8F"
        self.text_color = "black"

        #Configurações de Tela
        self.window.title('Robô de Animais') 
        self.window.geometry("500x500")
        self.window.configure(bg=self.bg_color)
        self.window.minsize(800, 500) 
        self.window.maxsize(800, 500) 

        # Background
        div_top = Frame(self.window, width=800, height=50, bg=self.button_color)
        div_top.pack(side="top")

        div_bottom = Frame(self.window, padx=800, width=800, height=50, bg=self.button_color)
        div_bottom.pack(side="bottom")

        # Titulo
        self.label_file_explorer = Label(self.window, font = ('Arial',30), text = "Robô de Animais", width = 100, bg=self.bg_color, fg=self.text_color)
        
        #Input
        self.message_label = Label(self.window ,text = "Digite seu Nome:", fg=self.text_color, bg=self.bg_color)
        self.message_value = Entry(self.window)

        # Selecionar Opção
        self.animal = Label(self.window ,text = "Tipo de Animal:", fg=self.text_color, bg=self.bg_color)
        self.animal_types = StringVar(self.window)
        self.animal_types.set("Selecione...")
        animal_types_options = ['Animais Carnívoros', 'Animais Herbívoros', 'Animais Onívoros']
        self.animal_option = OptionMenu(self.window, self.animal_types, *animal_types_options)

        #Botões
        self.button_exit = Button(self.window, text = "Sair", command = exit, bg=self.button_cancel, fg=self.text_color, width=15) 
        self.button_conv = Button(self.window, text = "Iniciar", command = self.start_conversion, bg=self.button_color, fg=self.text_color, width=15) 
        self.loading = Label(self.window, font = ('Arial',10), text = f"selecionando...", width = 100, fg=self.text_color, bg=self.bg_color)

    def place_start_window(self):  
        self.label_file_explorer.place(relx=0.5, rely=0.2, anchor=CENTER)
        self.message_label.place(relx=0.38, rely=0.40, anchor=CENTER)
        self.message_value.place(width=150, relx=0.6, rely=0.40, anchor=CENTER)
        self.animal.place(relx=0.38, rely=0.50, anchor=CENTER)
        self.animal_option.place(width=150,relx=0.6, rely=0.50, anchor=CENTER)
        self.button_conv.place(relx=0.40, rely=0.70, anchor=CENTER)
        self.button_exit.place(relx=0.60, rely=0.70, anchor=CENTER)
        self.window.mainloop() 

    def treat_exception(self, exception):
        return exception

    def start_conversion(self):

        self.loading.configure(text='aguarde...')
        self.window.update_idletasks()

        try:
            name = self.message_value.get()
            animal = self.animal_types.get()
            self.window.destroy()
            self.open_chat(name, animal)
            

        except Exception as ex:
            print(ex)
            ex = self.treat_exception(ex)
            messagebox.showerror("ERROR!", ex)
            self.loading.place_forget()

    def open_chat(self, name: str, animal: str):
        fbot = TKChat()
        fbot.place_start_window(name, name)
        
    