from answer import answer, fileToSpeak, randomNumb
from AI_process.listen import dateTimeNow, read_process, read_content
from time import sleep

# Executar e retornar a busca
def main():
    info = read_content(fileToSpeak)
    phrase = dateTimeNow()
    rand = randomNumb(info["Speak"]["userName"])
    read_process(phrase+info["Speak"]["userName"][rand])
    rand = randomNumb(info["Speak"]["phrases"])
    read_process(info["Speak"]["phrases"][rand])
    while True:
        text = input(info["Speak"]["quest"])
        search = False
        if(text == "boost"):
            print('boost')
            text = input(info["Speak"]["search"])
            search = True
        response = answer(text, search)
        
        if response is not None:
            read_process(response)
        elif text is not None:
            if text.lower() == 'n':
                print('indo aqui')
                rand = randomNumb(info["Speak"]["break"])
                read_process(info["Speak"]["break"][rand])
                sleep(3)
                break         
        else:
            rand = randomNumb(info["Speak"]["notFound"])
            if(rand):
                print('speak oii')
                print(info["Speak"]["notFound"][rand])
            else:
                print(info["Speak"]["notFound"][0])



if __name__ == "__main__":
    main()