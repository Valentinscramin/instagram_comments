from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 
import random
import json


class instagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        # EDIT EXECUTABLE PATH FROM FIREFOX WEBDRIVER (geckodriver)
        self.driver = webdriver.Firefox(executable_path=r"C:\Users\55199\Desktop\Robo Iphone\geckodriver\geckodriver.exe")


    @staticmethod
    def digite_como_humano(sent, onde_digitar):
        for letra in sent:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def singout(self):
        driver = self.driver
        driver.find_element_by_xpath("//div[@class='Fifk5']//img[@data-testid='user-avatar']").click()
        driver.find_element_by_xpath("//div[contains(text(), 'Sair')]").click()
        return "login"

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
           
        time.sleep(3)

        #Click no input login e senha
        input_usuario = driver.find_element_by_xpath("//input[@name='username']")
        input_usuario.click()
        input_usuario.clear()
        input_usuario.send_keys(self.username)

        input_senha = driver.find_element_by_xpath("//input[@name='password']")
        input_senha.click()
        input_senha.clear()
        input_senha.send_keys(self.password)
        input_senha.send_keys(Keys.RETURN)
        time.sleep(3)
        retorno = self.onde_comentar("URL INSTAGRAM POST")

        if retorno == "singout":
            singoutreturn = self.singout()
            return singoutreturn


    def onde_comentar(self,url_perfil):
        driver = self.driver
        driver.get(url_perfil)

        try:

            tamanho = 300
            contador = 0

            while(contador <= tamanho):

                # YOU CAN USE @USERS THAN COUNTRYS OR PERSON NAMES

                comentarios = ["Afeganistão",
                            "África do Sul",
                            "Akrotiri",
                            "Albânia",
                            "Alemanha",
                            "Andorra",
                            "Angola",
                            "Anguila",
                            "Antárctida",
                            "Antígua e Barbuda",
                            "Arábia Saudita",
                            "Arctic Ocean",
                            "Argélia",
                            "Argentina",
                            "Arménia",
                            "Aruba",
                            "Ashmore and Cartier Islands",
                            "Atlantic Ocean",
                            "Austrália",
                            "Áustria",
                            "Azerbaijão",
                            "Baamas",
                            "Bangladeche",
                            "Barbados",
                            "Barém",
                            "Bélgica",
                            "Belize",
                            "Benim",
                            "Bermudas",
                            "Bielorrússia",
                            "Birmânia",
                            "Bolívia",
                            "Bósnia e Herzegovina",
                            "Botsuana",
                            "Brasil",
                            "Brunei",
                            "Bulgária",
                            "Burquina Faso",
                            "Burúndi",
                            "Butão",
                            "Cabo Verde",
                            "Camarões",
                            "Camboja",
                            "Canadá",
                            "Catar",
                            "Cazaquistão",
                            "Chade",
                            "Chile",
                            "China",
                            "Chipre",
                            "Clipperton Island",
                            "Colômbia",
                            "Comores",
                            "Congo-Brazzaville",
                            "Congo-Kinshasa",
                            "Coral Sea Islands",
                            "Coreia do Norte",
                            "Coreia do Sul",
                            "Costa do Marfim",
                            "Costa Rica",
                            "Croácia",
                            "Cuba",
                            "Curacao",
                            "Dhekelia",
                            "Dinamarca",
                            "Domínica",
                            "Egipto",
                            "Emiratos Árabes Unidos",
                            "Equador",
                            "Eritreia",
                            "Eslováquia",
                            "Eslovénia",
                            "Espanha",
                            "Estados Unidos",
                            "Estónia",
                            "Etiópia",
                            "Faroé",
                            "Fiji",
                            "Filipinas",
                            "Finlândia",
                            "França",
                            "Gabão",
                            "Gâmbia",
                            "Gana",
                            "Gaza Strip",
                            "Geórgia",
                            "Geórgia do Sul e Sandwich do Sul",
                            "Gibraltar",
                            "Granada",
                            "Grécia",
                            "Gronelândia",
                            "Guame",
                            "Guatemala",
                            "Guernsey",
                            "Guiana",
                            "Guiné",
                            "Guiné Equatorial",
                            "Guiné-Bissau",
                            "Haiti",
                            "Honduras",
                            "Hong Kong",
                            "Hungria",
                            "Iémen",
                            "Ilha Bouvet",
                            "Ilha do Natal",
                            "Ilha Norfolk",
                            "Ilhas Caimão",
                            "Ilhas Cook",
                            "Ilhas dos Cocos",
                            "Ilhas Falkland",
                            "Ilhas Heard e McDonald",
                            "Ilhas Marshall",
                            "Ilhas Salomão",
                            "Ilhas Turcas e Caicos",
                            "Ilhas Virgens Americanas",
                            "Ilhas Virgens Britânicas",
                            "Índia",
                            "Indian Ocean",
                            "Indonésia",
                            "Irão",
                            "Iraque",
                            "Irlanda",
                            "Islândia",
                            "Israel",
                            "Itália",
                            "Jamaica",
                            "Jan Mayen",
                            "Japão",
                            "Jersey",
                            "Jibuti",
                            "Jordânia",
                            "Kosovo",
                            "Kuwait",
                            "Laos",
                            "Lesoto",
                            "Letónia",
                            "Líbano",
                            "Libéria",
                            "Líbia",
                            "Listenstaine",
                            "Lituânia",
                            "Luxemburgo",
                            "Macau",
                            "Macedónia",
                            "Madagáscar",
                            "Malásia",
                            "Malávi",
                            "Maldivas",
                            "Mali",
                            "Malta",
                            "Man, Isle of",
                            "Marianas do Norte",
                            "Marrocos",
                            "Maurícia",
                            "Mauritânia",
                            "México",
                            "Micronésia",
                            "Moçambique",
                            "Moldávia",
                            "Mónaco",
                            "Mongólia",
                            "Monserrate",
                            "Montenegro",
                            "Namíbia",
                            "Nauru",
                            "Navassa Island",
                            "Nepal",
                            "Nicarágua",
                            "Níger",
                            "Nigéria",
                            "Niue",
                            "Noruega",
                            "Nova Caledónia",
                            "Nova Zelândia",
                            "Omã",
                            "Pacific Ocean",
                            "Países Baixos",
                            "Palau",
                            "Panamá",
                            "Papua-Nova Guiné",
                            "Paquistão",
                            "Paracel Islands",
                            "Paraguai",
                            "Peru",
                            "Pitcairn",
                            "Polinésia Francesa",
                            "Polónia",
                            "Porto Rico",
                            "Portugal",
                            "Quénia",
                            "Quirguizistão",
                            "Quiribáti",
                            "Reino Unido",
                            "República Centro-Africana",
                            "República Dominicana",
                            "Roménia",
                            "Ruanda",
                            "Rússia",
                            "Salvador",
                            "Samoa",
                            "Samoa Americana",
                            "Santa Helena",
                            "Santa Lúcia",
                            "São Bartolomeu",
                            "São Cristóvão e Neves",
                            "São Marinho",
                            "São Martinho",
                            "São Pedro e Miquelon",
                            "São Tomé e Príncipe",
                            "São Vicente e Granadinas",
                            "Sara Ocidental",
                            "Seicheles",
                            "Senegal",
                            "Serra Leoa",
                            "Sérvia",
                            "Singapura",
                            "Sint Maarten",
                            "Síria",
                            "Somália",
                            "Southern Ocean",
                            "Spratly Islands",
                            "Sri Lanca",
                            "Suazilândia",
                            "Sudão",
                            "Sudão do Sul",
                            "Suécia",
                            "Suíça",
                            "Suriname",
                            "Svalbard e Jan Mayen",
                            "Tailândia",
                            "Taiwan",
                            "Tajiquistão",
                            "Tanzânia",
                            "Território Britânico do Oceano Índico",
                            "Territórios Austrais Franceses",
                            "Timor Leste",
                            "Togo",
                            "Tokelau",
                            "Tonga",
                            "Trindade e Tobago",
                            "Tunísia",
                            "Turquemenistão",
                            "Turquia",
                            "Tuvalu",
                            "Ucrânia",
                            "Uganda",
                            "União Europeia",
                            "Uruguai",
                            "Usbequistão",
                            "Vanuatu",
                            "Vaticano",
                            "Venezuela",
                            "Vietname",
                            "Wake Island",
                            "Wallis e Futuna",
                            "West Bank",
                            "Zâmbia",
                            "Zimbabué"]

                driver.find_element_by_class_name("Ypffh").click()
                campo_comentario = driver.find_element_by_class_name("Ypffh")
                time.sleep(random.randint(3,5))
                self.digite_como_humano(random.choices(comentarios), campo_comentario)
                time.sleep(random.randint(40,120))
                driver.find_element_by_xpath("//button[contains(text(), 'Publicar')]").click()
                time.sleep(5)

                contador += 1

                if contador == tamanho:
                    return "singout"
                

        except Exception as e:
            print(e)
            return "singout"


# DEFINE YOURS ACCOUNTS
contas = {
    "user0": "USER NAME 01",
    "senha0": "USER PASSWORD 01",
    "user1": "USER NAME 02",
    "senha1": "USER PASSWORD 02",
    "user2": "USER NAME 02",
    "senha2": "USER PASSWORD 02"
}

json_str = json.dumps(contas)
resp = json.loads(json_str)

contador = 0
# YOU NEED SET NUMBER OF ACCOUNTS USING ARRAYS LOGICS
quantidade_contas = 2

while contador <= quantidade_contas:

    valentinBot = instagramBot( resp["user" + str( contador )], resp["senha" + str( contador ) ])
    retorno = valentinBot.login()

    if retorno == "login":
        contador += 1
        continue
    else:
        break



