import requests
import json
import os
import time

API_KEY = "Api key"
API_URL = "https://www.virustotal.com/api/v3/ip_addresses/"
HEADERS = {
    "x-apikey": API_KEY
}


if not os.path.exists("responses"):
    os.makedirs("responses")

with open("ips.txt", "r") as f:
    ips = [line.strip() for line in f if line.strip()]

with open("malicious_ips.txt", "w") as malicious_file, open("not_found_ips.txt", "w") as not_found_file:
    for ip in ips:
        url = API_URL + ip
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            data = response.json()
            malicious = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("malicious", 0)
            suspicious = data.get("data", {}).get("attributes", {}).get("last_analysis_stats", {}).get("suspicious", 0)


            with open(f"responses/{ip}.json", "w") as outfile:
                json.dump(data, outfile, indent=2)

            if malicious > 0 or suspicious > 0:
                malicious_file.write(f"{ip}\n")
        elif response.status_code == 404:
            not_found_file.write(f"{ip}\n")
        else:
            print(f"[!] {ip} için hata: {response.status_code}")

        time.sleep(16)  

print("İşlem tamamlandı.")
