# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from random import choice
"""Main module."""

# -*- coding: utf-8 -*-

"""Main module."""

"""
Human Friendly Name: Syllable
Import Friendly Name: syllable
Package Description: Package that send a word or words set to service and get the syllabes of each phrase sent
https://gitter.im/twoscoopspress/packaging-workshop-march10
"""

from selenium import webdriver

def sendingWords(pathfile):
    """Send some words list to sillable service"""
    driver = webdriver.Chrome()
    driver.get("http://tip.iatext.ulpgc.es/silabas/Default.aspx")

    # words = ['Competencia', 'Educacion', 'Salud', 'Solidaridad', 'Armonia']

    with open(pathfile, 'r') as input, \
            open('send_words/output.txt', 'w') as output:
        for item in input:
            element = driver.find_element_by_id("MainContent_TextBox1")
            element.send_keys(item)

            result = driver.find_element_by_css_selector("table#MainContent_Table1 > tbody > tr > td:nth-of-type(2)").text
            # output.write(result)
            output.write("My word sent is: {item}. "
                "The word divide in silabes is: {result}\n".format(item=item, result=result))

def quotes():
    """Show some random quotes"""
    quotes = ['Hola', 'Como estas', 'Contento compartiendo en el workshop']
    print(choice(quotes))
