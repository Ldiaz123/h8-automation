# H8 Automation - Excel Data Extraction

This project automates the process of pulling data from H8 sources and exporting it to Excel spreadsheets.

## Overview

This automation tool fetches data from H8 systems and generates organized Excel reports with minimal manual intervention.

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Ldiaz123/h8-automation.git
   cd h8-automation
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a .env file** (if needed for H8 credentials)
   ```bash
   cp .env.example .env
   ```
   Update `.env` with your H8 connection details.

## Dependencies

| Package | Version | Purpose |
|---------|---------|----------|
| `openpyxl` | 3.10.10 | Read/write Excel files (.xlsx) |
| `pandas` | 2.0.3 | Data manipulation and analysis |
| `requests` | 2.31.0 | HTTP requests to H8 API/endpoints |
| `python-dotenv` | 1.0.0 | Environment variable management |

## Project Structure

```
h8-automation/
├── requirements.txt      # Python dependencies
├── README.md            # This file
├── .env.example         # Example environment variables
├── main.py              # Main entry point
├── src/
│   ├── __init__.py
│   ├── h8_client.py    # H8 data fetching logic
│   └── excel_export.py # Excel generation logic
└── output/
    └── reports/        # Generated Excel files
```

## Usage

```python
from src.h8_client import H8Client
from src.excel_export import ExcelExporter

# Fetch H8 data
client = H8Client()
client.authenticate()
data = client.fetch_data()

# Export to Excel
exporter = ExcelExporter()
exporter.export(data, 'h8_data_report.xlsx')
```

## Running the Automation

```bash
python main.py
```

## Configuration

Set environment variables in `.env`:
```
H8_API_URL=<your_h8_endpoint>
H8_USERNAME=<your_username>
H8_PASSWORD=<your_password>
OUTPUT_DIR=output/reports
FILE_TIMESTAMP=true
```

## Features

- [x] Basic project structure
- [x] Dependency management
- [ ] Fetch data from H8 system
- [ ] Data validation and cleaning
- [ ] Excel file generation with formatting
- [ ] Scheduled automation (cron jobs)
- [ ] Error logging and notifications

## Support

For issues or questions, please create a GitHub issue in this repository.
