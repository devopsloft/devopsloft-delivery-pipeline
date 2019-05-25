#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import NoSuchElementException

SELENIUM_HUB = 'http://localhost:4444/wd/hub'

chrome_driver = webdriver.Remote(
  command_executor=SELENIUM_HUB,
  desired_capabilities=DesiredCapabilities.CHROME,
)

firefox_driver = webdriver.Remote(
  command_executor=SELENIUM_HUB,
  desired_capabilities=DesiredCapabilities.FIREFOX,
)

try:
    for driver in [chrome_driver, firefox_driver]:
        driver.get('http://10.0.0.1:5000')
        assert driver.title == "DevOps Loft"

        driver.find_element_by_link_text('Home').click()
        assert driver.current_url == "http://10.0.0.1:5000/home"

        driver.find_element_by_link_text('Resources').click()
        assert driver.current_url == "http://10.0.0.1:5000/resources"

        driver.find_element_by_link_text('Documents').click()
        assert driver.current_url == "http://10.0.0.1:5000/docslist"

        driver.find_element_by_link_text('Contact Us').click()
        assert driver.current_url == "http://10.0.0.1:5000/contact"

        driver.find_element_by_link_text('Sign Up').click()
        assert driver.current_url == "http://10.0.0.1:5000/signup"
    print("Tests Passed Successfully")
except NoSuchElementException as exception:
    print("Element not found and test failed")
finally:
    for driver in [chrome_driver, firefox_driver]:
        driver.quit()
