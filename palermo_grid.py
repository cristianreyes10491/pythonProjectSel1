import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestStep1():
    def setup_method(self, method):
        self.driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                                       desired_capabilities=DesiredCapabilities.CHROME)
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_step1(self):
        self.driver.get("https://wwws.palermo.edu/cgi-bin/inscripcion/form.pl")
        self.driver.set_window_size(1382, 736)
        self.driver.find_element(By.ID, "nombre").click()
        self.driver.find_element(By.ID, "nombre").send_keys("Cristian Camilo")
        self.driver.find_element(By.ID, "apellido").click()
        self.driver.find_element(By.ID, "apellido").send_keys("Reyes Rodri")
        self.driver.find_element(By.ID, "mail").send_keys("cris@gmail.com")
        self.driver.find_element(By.ID, "doc_pais").click()
        dropdown = self.driver.find_element(By.ID, "doc_pais")
        dropdown.find_element(By.XPATH, "//option[. = 'Colombia']").click()
        self.driver.find_element(By.ID, "doc_tipo").click()
        dropdown = self.driver.find_element(By.ID, "doc_tipo")
        dropdown.find_element(By.XPATH, "//option[. = 'Cédula de Ciudadania']").click()
        self.driver.find_element(By.ID, "doc_numero").click()
        self.driver.find_element(By.ID, "doc_numero").send_keys("1049604126")
        self.driver.find_element(By.ID, "nacionalidad").click()
        dropdown = self.driver.find_element(By.ID, "nacionalidad")
        dropdown.find_element(By.XPATH, "//option[. = 'Colombiana']").click()
        self.driver.find_element(By.ID, "telefono_tipo").click()
        self.driver.find_element(By.ID, "telefono_prefix").click()
        dropdown = self.driver.find_element(By.ID, "telefono_prefix")
        dropdown.find_element(By.XPATH, "//option[. = 'Colombia']").click()
        self.driver.find_element(By.ID, "telefono_area").click()
        self.driver.find_element(By.ID, "telefono_numero").send_keys("3203018680")
        self.driver.find_element(By.ID, "acad_group").click()
        dropdown = self.driver.find_element(By.ID, "acad_group")
        dropdown.find_element(By.XPATH, "//option[. = 'Ingeniería']").click()
        self.driver.find_element(By.ID, "grado_academico").click()
        dropdown = self.driver.find_element(By.ID, "grado_academico")
        dropdown.find_element(By.XPATH, "//option[. = 'Carreras y Programas de Posgrado']").click()
        self.driver.find_element(By.ID, "periodo_lectivo").click()
        self.driver.find_element(By.ID, "periodo_lectivo").click()
        self.driver.find_element(By.ID, "periodo_lectivo").send_keys(Keys.ENTER)
        self.driver.execute_script("window.scrollTo(0,785)")
        self.driver.find_element(By.CSS_SELECTOR, "button").click()
        self.driver.find_element(By.CSS_SELECTOR, ".top-1").click()
        self.driver.find_element(By.CSS_SELECTOR, ".top-1").click()
        assert self.driver.find_element(By.ID, "1").text == "Por favor, verificá los campos marcados en rojo."

