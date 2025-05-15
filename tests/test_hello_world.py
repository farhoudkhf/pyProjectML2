def test_hello_world():
    assert "hello" + " " + "world" == "hello world"  
    assert 1 + 1 == 2  
    assert len("hello") == 5  

[pytest]
testpaths = tests
python_files = test_*.py