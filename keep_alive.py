import asyncio
from playwright.async_api import async_playwright
from datetime import datetime

URL = "https://portfolio-finance-romain-chalard.streamlit.app/"

async def ping_site():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Ouverture du navigateur...")
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print(f"Navigation vers {URL} ...")
        await page.goto(URL, timeout=60000)

        # Attend que Streamlit soit bien chargé
        try:
            await page.wait_for_selector("section.main", timeout=30000)
            print("✅ Page Streamlit chargée avec succès !")
        except:
            print("⚠️  Timeout sur le sélecteur, mais la page a quand même été visitée.")

        # Simule un scroll pour montrer de l'activité
        await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        await asyncio.sleep(3)
        await page.evaluate("window.scrollTo(0, 0)")
        await asyncio.sleep(2)

        print("✅ Interaction simulée avec succès !")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(ping_site())
