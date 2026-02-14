import asyncio
from playwright.async_api import async_playwright

async def run_scraper():
    # YOUR PROXY INFO FROM TEXT FILE
    PROXY_SERVER = "http://45.196.152.88:63056" # Use the IP:Port from your list
    PROXY_USER = "your_username"
    PROXY_PASS = "your_password"

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
    asyncio.run(run_scraper())