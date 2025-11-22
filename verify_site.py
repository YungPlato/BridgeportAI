
import os
from playwright.sync_api import sync_playwright, expect

def verify_site():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Navigate to home
        page.goto("http://localhost:8000")
        page.wait_for_selector("body")

        # Take screenshot of Home
        if not os.path.exists("verification"):
            os.makedirs("verification")

        page.screenshot(path="verification/1_home.png")
        print("Home screenshot taken")

        # Navigate to Services
        page.click("button:text('Agency Services')")
        # Wait for transition (currently simple display block)
        page.wait_for_timeout(1000)
        page.screenshot(path="verification/2_services.png")
        print("Services screenshot taken")

        # Navigate to Studio
        page.click("button:text('The Studio')")
        page.wait_for_timeout(1000)
        page.screenshot(path="verification/3_studio.png")
        print("Studio screenshot taken")

        # Navigate to Pricing
        page.click("button:text('Pricing')")
        page.wait_for_timeout(1000)
        page.screenshot(path="verification/4_pricing.png")
        print("Pricing screenshot taken")

        # Navigate to About
        page.click("button:text('Our Mission')")
        page.wait_for_timeout(1000)
        page.screenshot(path="verification/5_about.png")
        print("About screenshot taken")

        browser.close()

if __name__ == "__main__":
    verify_site()
