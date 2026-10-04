
import encryptletter

def test_encryptletter_A():
    assert encryptletter.encryptletter('A', 3) == 'D'

def test_encryptletter_Z():
    assert encryptletter.encryptletter('Z', 3) == 'C'

def test_encryptletter_lowercase():
    assert encryptletter.encryptletter('a', 4) == 'd'
