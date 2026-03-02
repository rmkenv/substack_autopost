import os
import requests
from datetime import datetime

def broadcast_via_quantagri(text: str):
    api_url = "https://ais-dev-so2tl22e75o3xvox6fhwgj-47634440091.us-east1.run.app/api/broadcast/substack"
    response = requests.post(api_url, json={"text": text})
    return response

def get_commodity_note(commodity: str) -> str:
    """Generate formatted note with timestamp & hashtags."""
    timestamp = datetime.now().strftime("%I:%M %p EST")
    base_text = f"🔥 QuantAgri {commodity.upper()} Update [{timestamp}] 🔥\n\n"
    content = (
        f"• Latest market signals & geospatial insights\n"
        f"• Key Reddit/Broadcast Hub highlights\n\n"
        f"#QuantAgri #{commodity.capitalize()} #Commodities #AgMarkets #Futures #Trading"
    )
    return base_text + content

if __name__ == "__main__":
    import sys
    commodity = sys.argv[1] if len(sys.argv) > 1 else "soy"
    commodities = ['soy', 'cotton', 'corn', 'wheat', 'sugar']
    if commodity not in commodities:
        print(f"❌ Error: Use one of {', '.join(commodities)}")
        exit(1)
    
    text = get_commodity_note(commodity)
    res = broadcast_via_quantagri(text)
    print(f"📤 [{commodity.upper()}] Status: {res.status_code}")
    print(f"📄 Sent: {text[:100]}...")
    print(f"🔍 Response: {res.text[:300]}")
