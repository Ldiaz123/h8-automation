"""
Main entry point for H8 Automation
"""

from src.h8_client import H8Client
from src.excel_export import ExcelExporter


def main():
    """Main execution function"""
    
    # Initialize clients
    h8_client = H8Client()
    excel_exporter = ExcelExporter()
    
    # Authenticate with H8
    if not h8_client.authenticate():
        print("Failed to authenticate with H8 system")
        return
    
    # Fetch data from H8
    print("Fetching data from H8...")
    data = h8_client.fetch_data()
    
    if data is None:
        print("No data retrieved from H8")
        return
    
    # Export to Excel
    print("Exporting data to Excel...")
    filepath = excel_exporter.export(data)
    
    # Cleanup
    h8_client.close()
    
    print("Automation completed successfully!")


if __name__ == '__main__':
    main()
