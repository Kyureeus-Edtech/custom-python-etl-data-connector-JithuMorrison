from datetime import datetime

def transform_data(ip, raw_data):
    """Transform raw API data into MongoDB-friendly format."""
    if not raw_data:
        raise ValueError(f"No data returned for IP {ip}.")

    return {
        "ip": ip,
        "riot": raw_data.get("riot", False),
        "result": raw_data,
        "ingested_at": datetime.utcnow()
    }