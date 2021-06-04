#!/usr/bin/env python
# coding: utf-8

"""
Chan Chi Fung's FYP deliverable:
Generic approach (Code, Framework and Exception Handlings) for automating functional testing on shopping apps
"""

from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import io
import sys, getopt


def StartShoppingApp():
    """
    StartShoppingApp with the correct desired capabilities.

    appPackage = Shopping App
    appActivity = The first page interact with
    noReset = Ture > No need to reset every time
    """
    caps = dict(
        platformName='android',
        deviceName='x',
        appPackage='X',
        appActivity='.MainPageActivity',
        noReset=True,
        newCommandTimeout=0,
        automationName='UiAutomator2')

    driver = webdriver.Remote('http://localhost:80/wd/hub', caps)

    return driver

# Locator Strategy that covers all
FindXpath = lambda x: aosbs.driver.find_element_by_xpath(x)
FindXpaths = lambda x: aosbs.driver.find_elements_by_xpath(x)
FindClass = lambda x: aosbs.driver.find_element_by_class_name(x)
FindClasses = lambda x: aosbs.driver.find_elements_by_class_name(x)
FindID = lambda x: aosbs.driver.find_element_by_id(x)
FindIDs = lambda x: aosbs.driver.find_elements_by_id(x)

FindText = lambda x: FindXpath('//*[@text[contains(.,"' + x + '")]]')
FindTexts = lambda x: FindXpaths('//*[@text[contains(.,"' + x + '")]]')
ClickIDbyXPath = lambda x: FindXpath('//*[@resource-id[contains(.,"' + x + '")]]').click()

# Just in case the above settings are not work
NewFindID = lambda x: aosbs.driver.find_element_by_android_uiautomator('new UiSelector().resourceId("'+ x +'")')
NewFindIDs = lambda x: aosbs.driver.find_elements_by_android_uiautomator('new UiSelector().resourceId("'+ x +'")')
NewFindText = lambda x: aosbs.driver.find_element_by_android_uiautomator('text("'+ x +'")')
NewFindTexts = lambda x: aosbs.driver.find_elements_by_android_uiautomator('text("'+ x +'")')
NewFindXpath = lambda x: aosbs.driver.find_element_by_android_uiautomator(x)
NewFindXpaths = lambda x: aosbs.driver.find_elements_by_android_uiautomator(x)

WaitElementByID = lambda timout,ID: WebDriverWait(aosbs.driver, timout).until(EC.presence_of_element_located((By.ID, ID)))
WaitElementByClass = lambda timout,className: WebDriverWait(aosbs.driver, timout).until(EC.presence_of_element_located((By.CLASS_NAME, className)))
WaitElementByXPath = lambda timout,text: WebDriverWait(aosbs.driver, timout).until(EC.presence_of_element_located((By.XPATH, text)))

aosbs = AOSBS()

def ShoppingCart():
    """
    Interacting with shopping cart

    Five basic test scenarios related to the shopping cart are selected:

    1)	Increase the quantity of the item from the cart and verify.
    2)	Add the same item multiple times and verify.
    3)	Add multiple items of different types and verify.
    4)	Remove some items from the cart and verify.
    5)	Remove all items from the cart and then verify.

    """

    # 1
    try:
        for _ in range(5):
            ShoppingCartBtn = NewFindID('xxxx').click()
            break
    except NoSuchElementException:
        print('Retry to click again.')
        time.sleep(1)

def RandomProductCheckOut():
    """

    Picking a random product in random category and conduct the checkout flow
    Random logics is heavily used to write the related code of picking a random product in random category and finally conduct the checkout flow.
    It should be the most common use cases that users will encounter so it must be tested.

    """