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
    for key, value in os.environ.items():
      print(f'{key}: {value}')

    print(os.getcwd(), " <<<<< os.getcwd()")
    print(os.listdir(), " <<<<< listdir")


    j_file = os.getenv("FIREBASE_ADMIN_SDK_FILENAME_TEST")
    print(os.getenv("FIREBASE_ADMIN_SDK_FILENAME_TEST"), "<<<<<<<<< FIREBASE_ADMIN_SDK_FILENAME_TEST")
    print(j_file, " <<<< j_file")
    with open(j_file, "r") as f:
        data = f.readlines()

    print(data, "<<<<<<<<< data FIREBASE_ADMIN_SDK_FILENAME_TEST")
