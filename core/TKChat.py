from tkinter import *
from tkinter import messagebox, scrolledtext
from core.service import Chat
from tkinter import PhotoImage
from PIL import Image, ImageTk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class TKChat():

    def __init__(self, name: str, type: str):  
        self.chat_service = Chat(name, type)
        self.name = name
        self.type = type
        self.bg_color = "white"
        self.button_color = "#7EBFB0"
        self.button_cancel = "#EC9F8F"
        self.text_color = "black"
        self.div_color = "#D9D9D9"
        self.div_user = "#ACE3C9" 
        self.div_bot = "#EC9F8F"
        
        self.list_messages = []

        #Configurações de Tela
        self.window = Tk()
        self.window.title('Chatbot de Animais') 
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
        self.chat = scrolledtext.ScrolledText(self.window, wrap=WORD, width=800, height=400, state=DISABLED)
        self.chat.pack(padx=10, pady=10)
        self.message_value = Entry(self.window)

        #Messages
        self.user_message = Label(self.window, text = f"selecionando...", bg=self.div_user)
        self.bot_message = Label(self.window, text = f"teste...", bg=self.div_bot)

        #Botões
        self.button_exit = Button(self.window, text = "Fechar", command = exit, bg=self.button_cancel, fg=self.text_color, width=15) 
        self.button_cloud = Button(self.window, text = "Ver núvem de palavras", command = self.show_wordcloud, bg=self.button_color, fg=self.text_color, width=15) 
        self.button_send = Button(self.window, font = ('Arial',10), text = "Enviar", command = self.send_message, bg=self.button_color, fg=self.text_color, width=15) 
        self.loading = Label(self.window,  text = f"selecionando...", width = 100, fg=self.text_color, bg=self.bg_color)

        self.message_value.place(width=600, height=50, relx=0.40, rely=0.90, anchor=CENTER)
        self.button_send.place(height=50, relx=0.90, rely=0.90, anchor=CENTER)
        self.button_exit.place(width=80,relx=0.05, rely=0.02)
        self.button_cloud.place(width=150,relx=0.17, rely=0.02)
        self.window.mainloop() 
        
    def treat_exception(self, exception):
        return exception    

    def show_wordcloud(self):
        wordcloud_window = Toplevel()
        wordcloud_window.title(f"Nuvem de Palavras - {self.type}")
        wordcloud_window.geometry("800x400")
        try:
            text = self.chat_service.get_cleaned_text()
            wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
            
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.imshow(wordcloud, interpolation='bilinear')
            ax.axis('off')

            canvas = FigureCanvasTkAgg(fig, master=wordcloud_window)
            canvas_widget = canvas.get_tk_widget()
            canvas_widget.pack(fill=BOTH, expand=True)
            button_exit = Button(wordcloud_window, text = "Fechar", command = wordcloud_window.destroy, bg=self.button_cancel, fg=self.text_color, width=15) 
            button_exit.place(width=80,relx=0.05, rely=0.02)
        except:
            wordcloud_window.destroy()

    def insert_message(self, message, person_type):
        if person_type == "user":
            self.chat.config(state=NORMAL)
            self.chat.insert(END, f"{self.name}: " + message + "\n")
            self.chat.config(state=DISABLED)
            self.message_value.delete(0, END)
        else:
            self.chat.config(state=NORMAL)
            self.chat.insert(END, "Bot: " + message + "\n")
            self.chat.config(state=DISABLED)
            self.message_value.delete(0, END)

    def send_message(self):
        mensagem = self.message_value.get()
        print(mensagem)
        response_welcome = self.chat_service.welcome_message(mensagem)
        if response_welcome:
            self.insert_message(mensagem, "user")
            self.insert_message(response_welcome, "bot")
        else:
            if mensagem:
                self.insert_message(mensagem, "user")
                message_bot = self.chat_service.answer(mensagem)
                self.insert_message(message_bot, "bot")
                

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

