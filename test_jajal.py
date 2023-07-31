from main import jajal
from dotenv import load_dotenv
import os
load_dotenv(dotenv_path=".env.test")

def test_jajal_success():
    result = jajal()
    assert result == "oke"

def test_jajal_failed():
    result = jajal()
    print(os.getenv("WADIDAW"), "<<<<<<<<< env")
    assert result != None
