"""
H8 Client Module
Handles fetching data from H8 sources
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv()


class H8Client:
    """Client for interacting with H8 data sources"""
    
    def __init__(self):
        self.base_url = os.getenv('H8_API_URL')
        self.username = os.getenv('H8_USERNAME')
        self.password = os.getenv('H8_PASSWORD')
        self.session = None
    
    def authenticate(self):
        """Authenticate with H8 system"""
        try:
            self.session = requests.Session()
            # Add your H8 authentication logic here
            print("Authenticating with H8 system...")
            return True
        except Exception as e:
            print(f"Authentication failed: {e}")
            return False
    
    def fetch_data(self, endpoint='data', params=None):
        """
        Fetch data from H8 endpoint
        
        Args:
            endpoint: H8 API endpoint
            params: Query parameters
            
        Returns:
            Dictionary or list of data
        """
        if not self.session:
            self.authenticate()
        
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.get(url, params=params or {})
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error fetching data from {endpoint}: {e}")
            return None
    
    def close(self):
        """Close the session"""
        if self.session:
            self.session.close()
