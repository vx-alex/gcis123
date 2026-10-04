from calculate import add   

def test_add():
    num = 10
    expected = 11
    actual = add(num)
    assert actual == expected
