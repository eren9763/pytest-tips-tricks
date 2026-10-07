from hello import hello_world , bye_function 

def test_hello(): 
    assert "Hello World!" == hello_world() 

def test_bye(): 
    assert "Bye!" == bye_function() 

