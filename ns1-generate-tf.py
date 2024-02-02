import json
import logging
import os
from ns1 import NS1

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def initialize_api_client():
    """Initialize and return the NS1 API client."""
    api_key = os.getenv('NS1_API_KEY')
    if not api_key:
        logging.error("NS1 API key is not set. Please set the NS1_API_KEY environment variable.")
        exit(1)
    return NS1(apiKey=api_key)

def fetch_zones(api):
    """Fetch all DNS zones."""
    try:
        zones_list = api.zones().list()
        return [zone['zone'] for zone in zones_list]
    except Exception as e:
        logging.error(f"Failed to fetch zones: {e}")
        exit(1)

def fetch_records_for_zone(api, zone_name):
    """Fetch all records for a given zone, corrected to properly access records."""
    try:
        zone = api.loadZone(zone_name)
        # Assuming the correct method to fetch records is to directly access a property or method
        # Adjusted to a generic approach; replace with the correct method as per NS1 SDK documentation
        records = zone.data.get('records', [])  # Assuming 'data' contains a 'records' field
        return [{
            "domain": record['domain'],
            "type": record['type'],
            "answers": [answer for answer in record.get('answers', [])]  # Assuming 'answers' is directly accessible
        } for record in records]
    except Exception as e:
        logging.error(f"Failed to fetch records for zone {zone_name}: {e}")
        return []

def generate_terraform_file(zone_name, records):
    """Generate Terraform file for the given zone and its records in a specific sub-directory."""
    output_dir = "terraform_files"
    os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists
    filename = os.path.join(output_dir, f"{zone_name}.tf")
    
    try:
        with open(filename, 'w') as file:
            file.write(f'resource "ns1_zone" "{zone_name}" {{\n')
            file.write(f'  zone = "{zone_name}"\n')
            file.write('}\n\n')

            for record in records:
                record_data = json.dumps([answer for answer in record['answers']], indent=2)
                file.write(f'resource "ns1_record" "{record["domain"]}" {{\n')
                file.write(f'  zone = "{zone_name}"\n')
                file.write(f'  domain = "{record["domain"]}"\n')
                file.write(f'  type = "{record["type"]}"\n')
                file.write(f'  answers = {record_data}\n')
                file.write('}\n\n')
        logging.info(f"Terraform file generated: {filename}")
    except IOError as e:
        logging.error(f"Failed to write Terraform file {filename}: {e}")

def main():
    api = initialize_api_client()
    zones = fetch_zones(api)
    for zone_name in zones:
        records = fetch_records_for_zone(api, zone_name)
        generate_terraform_file(zone_name, records)

if __name__ == "__main__":
    main()

