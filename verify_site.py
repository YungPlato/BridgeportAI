
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

        # Scroll to bottom to see contact form
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        page.wait_for_timeout(1000) # Wait for AOS animation

        # Focus on the contact section for better screenshot
        contact_section = page.locator("#contact")
        contact_section.screenshot(path="verification/contact_form.png")
        print("Contact form screenshot taken")

        browser.close()

if __name__ == "__main__":
    verify_site()
