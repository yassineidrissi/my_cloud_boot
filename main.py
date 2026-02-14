import asyncio
import os
from playwright.async_api import async_playwright

async def run_scraper():
    # Use environment variables for security (recommended for Railway)
    PROXY_SERVER = os.getenv("PROXY_SERVER", "http://45.196.152.88:63056")
    PROXY_USER = os.getenv("PROXY_USER", "your_actual_username")
    PROXY_PASS = os.getenv("PROXY_PASS", "your_actual_password")

    async with async_playwright() as p:
        # Launching with your residential proxy
        browser = await p.chromium.launch(
            headless=True,
            proxy={
                "server": PROXY_SERVER,
                "username": PROXY_USER,
                "password": PROXY_PASS
            }
        )
        
        context = await browser.new_context()
        page = await context.new_page()

        # TEST: Check if the proxy is working
        await page.goto("https://httpbin.org/ip")
        ip_info = await page.content()
        print(f"Bot is running with IP: {ip_info}")

        # YOUR LOGIC: Search AppStoreSpy or Play Store here
        # Example: await page.goto("https://appstorespy.com/...")
        
        await browser.close()

if __name__ == "__main__":
    # Run continuously every 60 seconds
    while True:
        try:
            asyncio.run(run_scraper())
            print("Bot cycle completed. Waiting 60 seconds...")
            asyncio.run(asyncio.sleep(60))
        except Exception as e:
            print(f"Error occurred: {e}")
            asyncio.run(asyncio.sleep(30))  # Wait 30 seconds before retry