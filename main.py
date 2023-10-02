from core.TKMain import TKMain

if __name__ == "__main__":
    try:
        fbot = TKMain()
        fbot.place_start_window()
    except:
        print("O chatbot foi encerrado.")