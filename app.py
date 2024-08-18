import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def openPage(netuser, netpass):
    chrome = webdriver.Chrome()
    chrome.get("https://my.sa.ucsb.edu/gold/")


    og_login = WebDriverWait(chrome, 10).until(
                EC.element_to_be_clickable((By.NAME, "ctl00$pageContent$loginButtonCurrentStudent"))
            )

    og_login.click()

    username = WebDriverWait(chrome, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )

    username.send_keys(netuser)

    password = WebDriverWait(chrome, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )

    password.send_keys(netpass)

    submit_login = WebDriverWait(chrome, 10).until(
                EC.element_to_be_clickable((By.NAME, "submit"))
            )

    submit_login.click()



    WebDriverWait(chrome, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='duo_iframe']")))
    WebDriverWait(chrome, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send Me a Push']"))).click()

    chrome.switch_to.default_content()

    continue_button = WebDriverWait(chrome, 10).until(
                EC.element_to_be_clickable((By.NAME, "ctl00$pageContent$continueButton"))
            )

    continue_button.click()


    expand_classes = WebDriverWait(chrome, 10).until(
                EC.element_to_be_clickable((By.ID, "expandCollapseRegcart"))
            )

    expand_classes.click()



def get_add_button(usern, passw, name, ecode):
    chrome = webdriver.Chrome()
    chrome.get("https://my.sa.ucsb.edu/gold/")


    og_login = WebDriverWait(chrome, 10).until(
                EC.element_to_be_clickable((By.NAME, "ctl00$pageContent$loginButtonCurrentStudent"))
            )

    og_login.click()

    username = WebDriverWait(chrome, 10).until(
                EC.presence_of_element_located((By.ID, "username"))
            )

    username.send_keys(usern)

    password = WebDriverWait(chrome, 10).until(
                EC.presence_of_element_located((By.ID, "password"))
            )

    password.send_keys(passw)

    submit_login = WebDriverWait(chrome, 10).until(
                EC.element_to_be_clickable((By.NAME, "submit"))
            )

    submit_login.click()



    WebDriverWait(chrome, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@id='duo_iframe']")))
    WebDriverWait(chrome, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Send Me a Push']"))).click()

    chrome.switch_to.default_content()

    continue_button = WebDriverWait(chrome, 10).until(
                EC.element_to_be_clickable((By.NAME, "ctl00$pageContent$continueButton"))
            )

    continue_button.click()


    expand_classes = WebDriverWait(chrome, 10).until(
                EC.element_to_be_clickable((By.ID, "expandCollapseRegcart"))
            )

    expand_classes.click()





    example_class = WebDriverWait(chrome, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(),'{name}')]"))
            )

    example_class_parent1 = example_class.find_element(By.XPATH, "..")
    example_class_parent2 = example_class_parent1.find_element(By.XPATH, "..")
    example_class_parent3 = example_class_parent2.find_element(By.XPATH, "..")
    example_class_parent4 = example_class_parent3.find_element(By.XPATH, "..")



    enroll_code_upper = example_class_parent4.find_elements(By.CSS_SELECTOR, "#bottom-row-regcart > "
                                                                             "div.col-lg-1.col-sm-1.col-xs-4.col-sm-pull-8")
    section_element = None

    for e in enroll_code_upper:
        if e.text == ecode:
            section_element = e


    section_element1 = section_element.find_element(By.XPATH, "..")
    section_element2 = section_element1.find_element(By.XPATH, "..")
    section_element3 = section_element2.find_element(By.XPATH, "..")
    section_element4 = section_element3.find_element(By.XPATH, "..")

    section_add_button = WebDriverWait(section_element4, 10).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(),'Add')]"))
            )

    chrome.quit()

    class_dict = {
        "name": name,
        "enrollment code": ecode,
        "button": section_add_button
    }
    return class_dict


