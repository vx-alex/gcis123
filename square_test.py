from square import square   
def test_square():
    num = 8
    expected = 64
    actual = square(num)
    assert actual == expected
    
