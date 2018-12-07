#!/bin/sh
from selenium import webdriver
from selenium.webdriver.common.by import By
import time,os

fp = webdriver.FirefoxProfile()

fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/csv")

browser = webdriver.Firefox(fp)
browser.get('http://www22.receita.fazenda.gov.br/inscricaomei/private/pages/relatorios/opcoesRelatorio.jsf#')
#iframe = browser.find_element_by_id('windowZ')
#browser.switch_to_frame(iframe)
el = browser.find_element_by_link_text('CNAE/Município')
res = el.click()
el = browser.find_element_by_id('form:uf')
for option in el.find_elements_by_tag_name('option'):
   if option.text == 'PERNAMBUCO':
        option.click() # select() in earlier versions of webdriver
        break
time.sleep(1.5)
lista_municipios = el = browser.find_element_by_id('form:listaMunicipiosUF')
#print(lista_municipios)
for option in lista_municipios.find_elements_by_tag_name('option'):
   #print(option.text)
   if option.text == 'RECIFE':
        option.click() # select() in earlier versions of webdriver
        break

btn_inserir = el = browser.find_element_by_id('form:btnInserir').click()

time.sleep(1)
browser.find_element_by_id('form:botaoConsultar').click()
time.sleep(2)
browser.find_element_by_id('form:botaoExportarCsv').click()
