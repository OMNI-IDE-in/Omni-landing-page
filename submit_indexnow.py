import json
import urllib.request
import urllib.error

HOST = "omniide.com"
KEY = "c0379c6560934e6293901b0451cf5713"
KEY_LOCATION = f"https://{HOST}/{KEY}.txt"

URL_LIST = [
    f"https://{HOST}/",
    f"https://{HOST}/omni/",
    f"https://{HOST}/interns/",
    f"https://{HOST}/docs/",
    f"https://{HOST}/blog/",
    f"https://{HOST}/terms-of-use/",
    f"https://{HOST}/privacy-policy/",
    f"https://{HOST}/assets/images/nihan-nihu-founder-omni-ide.png",
    f"https://{HOST}/assets/images/mohammed-nihan-founder-ceo-omniide.jpeg",
    f"https://{HOST}/assets/images/nihan-nihu-founder-ceo-omni.jpg",
    f"https://{HOST}/assets/images/mohammed-nihan-nihu-founder-omniide.jpg",
    f"https://{HOST}/assets/images/logo.jpg",
    f"https://{HOST}/assets/images/og-image.png",
    f"https://{HOST}/assets/images/arogya-omni-logo.png",
    f"https://{HOST}/assets/images/syncgraph-logo.jpg",
    f"https://{HOST}/assets/images/omni_rovis_icon.png",
    f"https://{HOST}/assets/images/scanai-logo.png",
    f"https://{HOST}/assets/images/mohammed-bilal.jpg",
    f"https://{HOST}/assets/images/wokspace-images/founder_ceo.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/founder-ceo.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/founder.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/ceo_coo.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/team-omni.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/team.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/working.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/core-team.jpeg",
    f"https://{HOST}/assets/images/wokspace-images/collage_ofimage.jpeg"
]

payload = {
    "host": HOST,
    "key": KEY,
    "keyLocation": KEY_LOCATION,
    "urlList": URL_LIST
}

endpoints = [
    "https://api.indexnow.org/indexnow",
    "https://www.bing.com/indexnow"
]

data = json.dumps(payload).encode("utf-8")
headers = {
    "Content-Type": "application/json; charset=utf-8",
    "User-Agent": "OmniIDE-IndexNow-Broadcaster/1.0"
}

print(f"[*] Submitting {len(URL_LIST)} URLs (Pages + Images) to IndexNow...")

for endpoint in endpoints:
    try:
        req = urllib.request.Request(endpoint, data=data, headers=headers, method="POST")
        with urllib.request.urlopen(req, timeout=15) as resp:
            status = resp.getcode()
            print(f"[+] Endpoint: {endpoint} -> HTTP {status} (Success / Queued for Indexing)")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        print(f"[-] Endpoint: {endpoint} -> HTTP {e.code}: {body}")
    except Exception as ex:
        print(f"[!] Endpoint: {endpoint} -> Connection Error: {ex}")
