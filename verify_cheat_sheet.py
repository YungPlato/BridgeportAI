from playwright.sync_api import sync_playwright
import time

def verify_cheat_sheet():
    with sync_playwright() as p:
        browser = p.chromium.launch()

        # Desktop
        page_desktop = browser.new_page(viewport={"width": 1280, "height": 800})
        page_desktop.goto("http://localhost:8000")
        time.sleep(1)
        # Scroll to lead magnet form
        page_desktop.evaluate("document.querySelector('form[action*=\"formsubmit\"]').scrollIntoView({block: 'center'})")
        time.sleep(0.5)
        page_desktop.screenshot(path="verification/cheat_sheet_desktop.png")

        # Mobile
        context_mobile = browser.new_context(
            viewport={"width": 375, "height": 812},
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1"
        )
        page_mobile = context_mobile.new_page()
        page_mobile.goto("http://localhost:8000")
        time.sleep(1)
        page_mobile.evaluate("document.querySelector('form[action*=\"formsubmit\"]').scrollIntoView({block: 'center'})")
        time.sleep(0.5)
        page_mobile.screenshot(path="verification/cheat_sheet_mobile.png")

        browser.close()
        print("Cheat Sheet verification screenshots re-captured.")

if __name__ == "__main__":
    verify_cheat_sheet()
