from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.firefox.launch()
    page = browser.new_page()
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    # volume_watter_1
    page.locator(".desktop-impact-items-F7T6E > div:nth-child(4)").screenshot(path="output/1.png")
    browser.close()
