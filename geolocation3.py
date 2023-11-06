import requests

def get_location_info(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None

ip_address = input("Masukkan alamat IP yang ingin Anda cari informasinya: ")
location_info = get_location_info(ip_address)

if location_info:
    print(f"IP Address: {ip_address}")
    print(f"City: {location_info.get('city', 'N/A')}")
    print(f"Region: {location_info.get('region', 'N/A')}")
    print(f"Country: {location_info.get('country', 'N/A')}")
    print(f"Location: {location_info.get('loc', 'N/A')}")
else:
    print("Tidak dapat mendapatkan informasi lokasi.")
