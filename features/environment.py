# features/environment.py
import os, sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait

# Put project root (one level up from features/) on sys.path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from app.application import Application   # <-- NOT "features.app"

def before_scenario(context, scenario):
    service = Service(ChromeDriverManager().install())
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    context.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def after_scenario(context, scenario):
    try:
        context.driver.quit()
    except:
        pass


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()
