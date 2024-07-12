import hello
import prog1

def test_hello():
    assert hello.hello_world() == "Hello!"
    
def test_math():
    assert prog1.prog1_sum() == 5
    