from main import jajal
from dotenv import load_dotenv
import os
import json

load_dotenv(dotenv_path=".env.test")

def test_jajal_success():
    result = jajal()
    assert result == "oke"

def test_jajal_failed():
    result = jajal()
    print(os.getenv("WADIDAW"), "<<<<<<<<< env")
    print(os.getenv("WATITSUYA"), "<<<<<<<<< eWWW")
    assert result != None

def test_read_json():
    j_file = os.getenv("FIREBASE_ADMIN_SDK_FILENAME_TEST")
    print(os.getenv("FIREBASE_ADMIN_SDK_FILENAME_TEST"), "<<<<<<<<< FIREBASE_ADMIN_SDK_FILENAME_TEST")
    with open(j_file) as f:
        data = json.load(f)

    print(data, "<<<<<<<<< data FIREBASE_ADMIN_SDK_FILENAME_TEST")
