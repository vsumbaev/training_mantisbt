﻿from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper


class Application:
    def __init__(self, browser, baseUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" %browser)
        self.wd.implicitly_wait(3)
        self.session = SessionHelper(self)
        self.baseUrl = baseUrl
        self.project = ProjectHelper(self)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.baseUrl)

    def destroy(self):
        self.wd.quit()