from execute_addition import add
def test_add():
    x = 5
    y = 4
    expected = 9
    actual = add(x, y)
    assert actual == expected