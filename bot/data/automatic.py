from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Configurar driver modo headless
options = webdriver.ChromeOptions()
options.add_argument("--headless")


def superSearch(user_query):
    try:
        # Iniciar driver do Chrome
        driver = webdriver.Chrome(options=options)
        driver.get("https://www.google.com/")
        
        # Pesquisa
        search_box = driver.find_element("name", "q")
        search_box.send_keys(user_query)
        search_box.send_keys(Keys.RETURN)

        # Aguardar resultados
        driver.implicitly_wait(5)
        # Encontre um link
        first_link = driver.find_element("css selector", ".tF2Cxc a")
        first_link_url = first_link.get_attribute("href")

        print("URL do link:", first_link_url)
        return first_link_url

    except Exception as e:
        print(f"Ocorreu um erro: {str(e)}")

    finally:
        driver.quit()


