import sys
sys.path.append('..')
sys.path.append('...')
import utilidades

class BasePage:
	def __init__(self, browser, nomeScript):
		self.browser = browser
		self.nomeScript = nomeScript

	def acessar(self,url):
		utilidades.acessar(self.browser,url)