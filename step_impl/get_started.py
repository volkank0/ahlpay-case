import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from getgauge.python import before_suite, after_suite, step
from step_impl.util import *
from step_impl.paths import *


driver = None

@before_suite
def init():
    global driver
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--kiosk")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)



@after_suite
def close():
    if driver:
        driver.quit()
        print("Güzel dönüşlerinizi heyecanla bekliyorum.")


@step("Go to <url>")
def go_to_url(url):
    driver.get(url)


@step("Click the <button> button")
def click_button(button):
    button_clicker(button, "Click {btn} element".format(btn=button), driver)


@step("Check <link> URL")
def check_url(link):
    url_checker(driver, "Check url {}".format(link), link)


@step("Write <text> to input <input>")
def write_text_to_input(text, input):
    enter_text(input, "Write {} to input {}".format(text, input), text, driver)


@step("Input <input> writes <txt>")
def check_input_text(input, txt):
    text_checker(input, "Input {} writes {}".format(input, txt), txt, driver)



@step("Wait <second> second")
def wait_for_seconds(second):
    time.sleep(int(second))

