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
import random


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

    # 1 - 2, 4 - 5
    # change the number in range () to modify the quantity
    try:
        for _ in range(5):
            ShoppingCartBtn = NewFindID('xxxx').click()
            break
    except NoSuchElementException:
        print('Retry to click again.')
        time.sleep(1)

    # 3
    # Randomly Click multiple items

    # Logic about capturing all items
    TotalList = []

    # Assign a Item Amount that you want to click
    ItemAmount = 999


    Items = NewFindIDs('XXXX')
    for element in Items:
        TotalList.append(element.text)

    # Logic about randomly pick some items
    randomList = random.sample(TotalList, int(ItemAmount))
    def ClickRandomItem(randomList):
        AllItems = NewFindIDs('XXXX')
        print('Start to Click into each items.')
        for element in AllItems:
            if element.text in randomList:
                element.click()
                # Scrolldown()
                time.sleep(2)
                # aosbs.driver.back()
                print('product being clicked' + str(element.text))
                randomList.remove(element.text)
                print('Finished one random item clicking')

def RandomProductCheckOut():
    """

    Picking a random product in random category and conduct the checkout flow
    Random logics is heavily used to write the related code of picking a random product in random category and finally conduct the checkout flow.
    It should be the most common use cases that users will encounter so it must be tested.

    """
    TotalProducts = []

    # Assign a Product Amount that you want to click
    ProductAmount = 999

    Products = NewFindIDs('XXXX')

    for element in Products:
        TotalProducts.append(element.text)

    randomProducts = random.sample(TotalProducts, int(ProductAmount))

    def ClickRandomProducts(randomProducts):
        AllItems = NewFindIDs('XXXX')
        print('Start to Click into each items.')
        for element in AllItems:
            if element.text in randomList:
                element.click()
                # Scrolldown()
                time.sleep(2)
                # aosbs.driver.back()
                print('product being clicked' + str(element.text))
                randomList.remove(element.text)
                print('Finished one random item clicking')

    # Randomly click products for enough ProductAmount randomly
    if len(TotalProducts) > int(ProductAmount) or len(TotalProducts) == int(ProductAmount):
        finalyrandomproducts = random.sample(TotalProducts, int(ProductAmount))
        for element in finalyrandomproducts:
            print('Random Product are Name is: ' + str(element))

        print('Random Clicking According to the assigned No. Begin')


        # Expect the itesm are all not shown in a page, so a scrolling logic should be applied
        while True:
            searchRmdMatchSinglePage(randomProducts)
            time.sleep(2)
            # Scroll Logic
            time.sleep(2)
            print('Scroll to find the remaining products for picking')
            if len(randomedProducts) == 0:
                break
                print('finished random products clicking, break the while loop.')

    # Otherwise, click all products (applied to small products)
    elif len(TotalProducts) < int(ProductAmount):
        print('Current amount does not support random checking, conduct full checking now.')
        pass

    def CheckOutFlow():

        # strategies what would be used

        NewFindID('XX').click()
        # This is alternative of the above Click XY:
        # NewFindID('XXXX').click()

        ClickXY('xx', 'xx')

def CheckingOrderHistory():

    """

    Customer concerns if their orders is failed or not. Therefore, the code development on checking order history is essential.

    Illustrative code
    """

    def checkingFlow(recordBtn):
        recordBtn.click()
        time.sleep(1)

        # most of the situations that can apply to this LinearLayout
        recordBtn = FindClasses('android.widget.LinearLayout')
        recordBtn[0].click()
        # Back to last page
        aosbs.driver.back()
        time.sleep(2)
        recordBtn[1].click()
        print('Turned to next order')
        time.sleep(2)
        print('Finished Info Checking and Odd Checking')
        time.sleep(1)

        # until reocrdBtn[Max.]

def ExceptionHandling():
    """

    During the development, two exceptions are often occurs, which are “No such element exception” and “Session not found exception”.
    The former refers to the element cannot be located while
    the later refers to the lose of connection with the mobile application that tester are testing.

    """

    # Try Catch Framework

    for _ in range(5):
        try:
            Elemntthatyouwant = NewFindID('XXXXXX')
            break
        except NoSuchElementException:
            print('Retry to find the element.')
            time.sleep(1)

    # Session Suspended
