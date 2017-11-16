from selenium.webdriver.common.by import By
import time, os, sys
from util import utilidades
from util.PageObjects.GRH import *
from selenium import webdriver

usuario = sys.argv[1]
senha = sys.argv[2]
driver = webdriver.Firefox()
driver.implicitly_wait(30)
base_url = "http://t-pristina:8080/grh"
nomeScript = os.path.basename(__file__)
utilidades.inicializar_diretorio_prints(nomeScript)
parametros = utilidades.get_parametros_script(nomeScript)

paginaLogin = GRHLoginPage(driver,nomeScript)
paginaPrincipal = paginaLogin.fazer_login(usuario,senha)
paginaServidor = paginaPrincipal.acessar_pagina_servidor(base_url)
paginaServidor.acessar_busca_servidor()
paginaServidor.buscar_servidor(parametros['matricula'])
paginaServidor.abrir_dados_funcionais()
paginaServidor.verificar_nomeacao_servidor(parametros['nomeacaoEsperada'])