# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

###Codigo adaptado

driver = webdriver.Chrome()
driver.implicitly_wait(30)
base_url = "http://t-pristina03:8080/grh"
verificationErrors = []
accept_next_alert = True
driver.get(base_url)
time.sleep(2)
driver.close()
#driver.find_element_by_css_selector("a[title=\"Servidor\"]").click()
#driver.find_element_by_id("frmSave:tabViewFormServidor:nome").clear()
#driver.find_element_by_id("frmSave:tabViewFormServidor:nome").send_keys("00000000000")
#driver.find_element_by_id("frmSave:tabViewFormServidor:cpf").clear()
#driver.find_element_by_id("frmSave:tabViewFormServidor:cpf").send_keys("00000000000")
#driver.find_element_by_xpath("//div[@id='frmSave:tabViewFormServidor:tipoDocumentoIdentificacao']/div[3]/span").click()
#driver.find_element_by_xpath("//div[@id='frmSave:tabViewFormServidor:tipoDocumentoIdentificacao_panel']/div/ul/li[2]").click()
#driver.find_element_by_id("frmSave:tabViewFormServidor:numeroDocumento").clear()
#driver.find_element_by_id("frmSave:tabViewFormServidor:numeroDocumento").send_keys("112456890")
#driver.find_element_by_id("frmSave:tabViewFormServidor:nomeCracha").clear()
#driver.find_element_by_id("frmSave:tabViewFormServidor:nomeCracha").send_keys("teste")
#driver.find_element_by_id("frmSave:btnSaveAndClean").click()
