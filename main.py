import asyncio
import os
import sys
from playwright.async_api import async_playwright

async def run_scraper():
    """Run the web scraper with proxy"""
    print("Starting scraper...")
    
    # Use environment variables for security (recommended for Railway)
    PROXY_SERVER = os.getenv("PROXY_SERVER", "http://45.196.152.88:63056")
    PROXY_USER = os.getenv("PROXY_USER", "your_actual_username")
    PROXY_PASS = os.getenv("PROXY_PASS", "your_actual_password")
    
    print(f"Using proxy server: {PROXY_SERVER}")
    print(f"Proxy user: {PROXY_USER}")

    try:
        async with async_playwright() as p:
            print("Launching browser...")
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
            print("Testing proxy connection...")
            await page.goto("https://httpbin.org/ip")
            ip_info = await page.content()
            print(f"Bot is running with IP: {ip_info}")

            # YOUR LOGIC: Search AppStoreSpy or Play Store here
            # Example: await page.goto("https://appstorespy.com/...")
            
            await browser.close()
            print("Browser closed successfully")
            
    except Exception as e:
        print(f"Error in scraper: {e}")
        raise

async def main():
    """Main function to run the bot continuously"""
    while True:
        try:
            await run_scraper()
            print("Bot cycle completed. Waiting 60 seconds...")
            await asyncio.sleep(60)
        except Exception as e:
            print(f"Error occurred: {e}")
            print("Retrying in 30 seconds...")
            await asyncio.sleep(30)

if __name__ == "__main__":
    print("Starting CloudBot...")
    asyncio.run(main())