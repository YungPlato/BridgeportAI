
from playwright.sync_api import sync_playwright, expect
import os

def verify_pricing():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to home
        page.goto("http://localhost:8000")

        # Go to Pricing
        page.click("button:text('Pricing')")
        page.wait_for_timeout(1000)

        # Click Studio Classes
        page.click("button:text('Studio Classes')")
        page.wait_for_timeout(500)

        # Check Studio Pricing
        if not os.path.exists("verification"):
            os.makedirs("verification")

        page.screenshot(path="verification/pricing_studio_toggle.png")

        # Target the Pricing Card Title explicitly
        studio_card_title = page.locator("h3.text-xl.font-bold", has_text="AI 101 Class")

        try:
            expect(studio_card_title).to_be_visible()
            print("Studio Pricing Visible")
        except Exception as e:
            print(f"Studio Pricing Not Visible: {e}")

        browser.close()

if __name__ == "__main__":
    verify_pricing()
