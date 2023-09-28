from tkinter import *
from tkinter import messagebox, scrolledtext

class TKChat():

    def __init__(self):  

        self.window = Tk()
        self.bg_color = "white"
        self.button_color = "#7EBFB0"
        self.button_cancel = "#EC9F8F"
        self.text_color = "black"
        self.div_color = "#D9D9D9"
        self.div_user = "#ACE3C9" 
        self.div_bot = "#EC9F8F"
        
        self.list_messages = []

        #Configurações de Tela
        self.window.title('Robô de Animais') 
        self.window.geometry("500x500")
        self.window.configure(bg=self.bg_color)
        self.window.minsize(800, 500) 
        self.window.maxsize(800, 500) 

        # Background
        div_top = Frame(self.window, width=800, height=50, bg=self.div_color)
        div_top.pack(side="top")

        div_bottom = Frame(self.window, padx=800, width=800, height=100, bg=self.div_color)
        div_bottom.pack(side="bottom")

        #Input
        self.chat = scrolledtext.ScrolledText(self.window, width=800, height=400)
        self.chat.config(state=DISABLED)
        self.chat.pack()
        self.message_value = Entry(self.window)

        #Messages
        self.user_message = Label(self.window, text = f"selecionando...", bg=self.div_user)
        self.bot_message = Label(self.window, text = f"teste...", bg=self.div_bot)

        #Botões
        self.button_exit = Button(self.window, text = "Fechar", command = exit, bg=self.button_cancel, fg=self.text_color, width=15) 
        self.button_send = Button(self.window, font = ('Arial',10), text = "Enviar", command = self.send_message, bg=self.button_color, fg=self.text_color, width=15) 
        self.loading = Label(self.window,  text = f"selecionando...", width = 100, fg=self.text_color, bg=self.bg_color)

    def place_start_window(self, nome, animal):  
        self.message_value.place(width=600, height=50, relx=0.40, rely=0.90, anchor=CENTER)
        width_box = (len(nome) * 5) + 80
        
        #Label(self.window, font = ('Arial',8), text = f"Olá {nome}!", bg=self.div_bot).place(width=width_box, height=50, relx=0.05, rely=0.20)
        self.button_send.place(height=50, relx=0.90, rely=0.90, anchor=CENTER)
        self.button_exit.place(width=80,relx=0.05, rely=0.02)
        self.window.mainloop() 

    def treat_exception(self, exception):
        return exception
    

    def send_message(self):
        mensagem = self.message_value.get()
        if mensagem:
            message = "Você: " + mensagem + "\n"
            mensagem_label = Label(self.chat, text=message, bg="lightblue")
            mensagem_label.pack(side="right")
            self.message_value.delete(0, END)

    def start_conversion(self):

        self.loading.configure(text='aguarde...')
        self.window.update_idletasks()

        try:
            print(self.message_value.get())

        except Exception as ex:
            print(ex)
            ex = self.treat_exception(ex)
            messagebox.showerror("ERROR!", ex)
            self.loading.place_forget()

    def open_chat(self, name: str, animal: str):
        self.chat_window = Tk()

