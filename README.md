# VirusTotal IP Reputation Checker (Python)

Bu script, bir dosya içindeki IP adreslerini alarak her biri için VirusTotal Public API üzerinden sorgu yapar ve zararlı/şüpheli olanları tespit eder.

## Özellikler

- `ips.txt` dosyasındaki IP'leri sırayla okur
- Her IP için VirusTotal’dan veri çeker
- `malicious` veya `suspicious` ≥ 1 ise `malicious_ips.txt`'ye yazar
- Bulunamayan IP'ler `not_found_ips.txt`'ye yazılır
- Tüm JSON yanıtları `responses/` klasörüne kaydedilir

## Gereksinimler

- Python 3
- requests modülü

```bash
pip install requests
