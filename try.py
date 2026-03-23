from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv
import os 

# Load environment variables from .env file
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

if not MONGO_DB_URL:
    print("Error: MONGO_DB_URL not found in .env file")
    exit(1)

print(f"Connecting to MongoDB Atlas...")

try:
    # Create a new client and connect to the server
    # Disable certificate verification for TLS issues with Python 3.14
    import ssl
    client = MongoClient(
        MONGO_DB_URL, 
        server_api=ServerApi('1'),
        tlsAllowInvalidCertificates=True
    )
    
    # Send a ping to confirm a successful connection
    client.admin.command('ping')
    print("✓ Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(f"✗ Connection failed: {e}")
