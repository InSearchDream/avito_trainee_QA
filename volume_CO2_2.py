from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    page = browser.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    #volume_CO2_2
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(2)").screenshot(path="output/2.png")
    browser.close()
