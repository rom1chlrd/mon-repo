import requests
import time
from datetime import datetime

URL = "https://portfolio-finance-romain-chalard.streamlit.app/"

def ping_site():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Pinging {URL} ...")
    try:
        response = requests.get(URL, timeout=30)
        print(f"✅ Status: {response.status_code} — Site is alive!")
    except requests.exceptions.Timeout:
        print("⚠️  Timeout — le site met du temps à répondre (probablement en train de se réveiller).")
    except requests.exceptions.RequestException as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    ping_site()
