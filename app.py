from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep


def iniciar_driver():
    chrome_options = Options()
    arguments = ['--lang=pt-BR', '--window-size=1300,1000', '--incognito']
    for argument in arguments:
        chrome_options.add_argument(argument)

    chrome_options.add_experimental_option('prefs', {
        'download.prompt_for_download': False,
        'profile.default_content_setting_values.notifications': 2,
        'profile.default_content_setting_values.automatic_downloads': 1,

    })
    driver = webdriver.Chrome(service=ChromeService(
        ChromeDriverManager().install()), options=chrome_options)

    return driver


driver = iniciar_driver()
# ir até o facebook
driver.get('https://www.facebook.com/')
sleep(5)
# Digitar email
campo_email = driver.find_element(By.ID, 'email')
sleep(5)
campo_email.send_keys('email@gmail.com')
sleep(5)
# Digitar senha
campo_senha = driver.find_element(By.ID, 'pass')
sleep(5)
campo_senha.send_keys('senha')
sleep(5)
# clicar em login
botao_entrar = driver.find_element(By.XPATH, "//button[@name='login']")
sleep(5)
botao_entrar.click()
sleep(5)


# encontrar e clicar no campo de postagem
campo_status = driver.find_element(
    By.XPATH, "//span[text()='No que você está pensando, Diogo?']")
sleep(2)
campo_status.click()
sleep(5)
# Clicar dentro do campo de status
dentro_campo_status = driver.find_element(
    By.XPATH, "//p[@class='xdj266r x11i5rnm xat24cr x1mh8g0r x16tdsg8']")
sleep(1)
dentro_campo_status.click()
sleep(1)
# Digitar algo
dentro_campo_status.send_keys('Teste Bot->Partiu Corujao!')
sleep(3)
# Clicar em publicar
botao_publicar = driver.find_element(
    By.XPATH, "//div[@class='x1n2onr6 x1ja2u2z x78zum5 x2lah0s xl56j7k x6s0dn4 xozqiw3 x1q0g3np xi112ho x17zwfj4 x585lrc x1403ito x972fbf xcfux6l x1qhh985 xm0m39n x9f619 xn6708d x1ye3gou xtvsq51 x1r1pt67']")
sleep(2)
botao_publicar.click()

input('')
driver.close()
