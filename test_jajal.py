from main import jajal

def test_jajal_success():
    result = jajal()
    assert result == "oke"

def test_jajal_failed():
    result = jajal()
    assert result != None
