from faker import Faker
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
import schedule

def main():

    fake = Faker('pt_BR')
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=Options)  # seu path do driver
    driver.get('https://br.ubberbrz.store/acesso/registro.php')
    time.sleep(3)

    try:

        driver.find_element_by_name('fnameQ').send_keys(fake.first_name())
        driver.find_element_by_name('lnameQ').send_keys(fake.last_name())

        for i in range(5):
            driver.find_element_by_name('cepQ').send_keys(fake.pyint(min=0, max=9, step=1))

        driver.find_element_by_name('cepQ').send_keys('-')

        for i in range(3):
            driver.find_element_by_name('cepQ').send_keys(fake.pyint(min=0, max=9, step=1))

        driver.find_element_by_id('btnQuick').click()

        driver.find_element_by_name('cpfC').send_keys(fake.cpf())

        driver.find_element_by_name('cc').send_keys(fake.credit_card_number(card_type=None))

        driver.find_element_by_name('exp').send_keys(fake.credit_card_expire(start="now", end="+10y", date_format="%m/%y"))

        driver.find_element_by_name('cvv').send_keys(fake.credit_card_security_code(card_type=None))

        driver.find_element_by_id('btnAppl').click()
        time.sleep(2)


        for i in range(4):
            driver.find_element_by_name('senhaCC').send_keys(fake.pyint(min=0, max=9, step=1))

        driver.find_element_by_id('btnSenha').click()

        driver.close()

    except:
        print('Cannot complete the function')
        driver.close()

schedule.every().minute.at(":17").do(main)


while True:
       schedule.run_pending()
       time.sleep(1)




