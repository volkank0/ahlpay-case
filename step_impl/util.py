import datetime
import time
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from step_impl.paths import paths
from step_impl.settings import *
import json
from selenium.webdriver.common.keys import Keys

def nowTime():
    return str(datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S"))


def path_finder(driver, path):
    try:
        get_url = driver.current_url
        return paths[get_url][path]
    except KeyError:
        default_url = "https://www.volkanpay.com/"
        return paths[default_url][path]


def screen_shot(driver):
    driver.save_screenshot(file_path + str(nowTime()) + ".png")

def find_element(driver, element):
    selector_types = [ By.XPATH, By.ID, By.CLASS_NAME, By.NAME, By.LINK_TEXT]

    for selector_type in selector_types:
        try:
            element_type = str(selector_type).split(".")[-1].lower()
            element = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((selector_type, element))
            )
            #print(f"Element {element_type} seçici ile bulundu.")
            return element
        except:
            continue
    return None

def url_checker(driver, step, url):
    time.sleep(2)
    current_url = driver.current_url
    if current_url == url:
        print(f"Yönlendirme Doğru: {current_url}")
        screen_shot(driver)
    else:
        print(f"Hatalı Yönlendirme: {current_url}")

def button_clicker(path, step, driver):
    try:
        pathfile = path_finder(driver, path)
        element = find_element(driver, pathfile)
        if element:
            element.click()
            print(f"{step} başarılı.")
            screen_shot(driver)
        else:
            print(f"Buton tıklama için {path} elementi bulunamadı.")
    except Exception as e:
        print(f"{step} hata: {str(e)}")

def text_checker(path, step, text, driver):
    try:
        pathfile = path_finder(driver, path)
        element = find_element(driver, pathfile)
        if element:
            if element.text == text:
                print(f"{step} başarılı")
                screen_shot(driver)
            else:
                print(f"{step} metin eşleşmiyor")
        else:
            print(f"{step} elementi bulunamadı")
    except Exception as e:
        print(f"{step} hata: {str(e)}")


def enter_text(path, step, text, driver):
    try:
        pathfile = path_finder(driver, path)
        element = find_element(driver, pathfile)
        if element:
            element.clear()
            element.send_keys(text)
            print(f"{step} başarılı")
            screen_shot(driver)
        else:
            print(f"{step} elementi bulunamadı")
    except Exception as e:
        print(f"{step} hata: {str(e)}")
