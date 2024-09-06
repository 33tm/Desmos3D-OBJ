#!/usr/bin/env python

from sys import argv
from selenium import webdriver

if len(argv) < 2:
    print(f"Usage: {argv[0]} <input>")
    exit(1)

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

browser = webdriver.Chrome(options=options)
browser.get("https://desmos.com/3d")

def get(selector):
    return browser.find_element("css selector", selector)

def folder():
    try:
        get("button[aria-label='Add Item']").click()
        get("div[aria-label='Add folder']").click()
        get("textarea[aria-label='Folder']").send_keys(argv[1])
        get(f"div[aria-label='Collapse {argv[1]} folder']").click()
    except:
        folder()

def graph(equation):
    get("div.dcg-new-math-div").click()
    get("textarea.dcg-focus-visible").send_keys(equation)
    # move to folder

folder()

with open(argv[1]) as obj:
    for line in obj:
        if not line.strip():
            continue

        command, *args = line.split()

        match command:
            case "#":
                continue
            case "v":
                x, y, z = args
                graph(f"({x}, {y}, {z})")
            case _:
                x
                print(f'Unexpected "{command}"')
