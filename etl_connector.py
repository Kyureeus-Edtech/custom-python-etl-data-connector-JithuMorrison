from extract import fetch_greynoise
from transform import transform_data
from load import save_result

def run_etl(ip_list):
    for ip in ip_list:
        try:
            print(f"Processing IP: {ip}")
            raw_data = fetch_greynoise(ip)
            doc = transform_data(ip, raw_data)
            save_result(doc)
            print(f"Successfully saved IP: {ip}")
        except Exception as e:
            print(f"Error processing IP {ip}: {e}")

if __name__ == "__main__":
    ips = input("Enter IP addresses (comma-separated): ").split(",")
    ips = [ip.strip() for ip in ips if ip.strip()]
    run_etl(ips)