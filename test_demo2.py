import pytest

@pytest.mark.login
def test_mahe():
    assert 2==1
def test_mahe1():
    assert 3==2
def test_mahe2():
    assert 5==5

@pytest.mark.login
def test_k():
    assert 'mahesh'=='mahesh'
def test_k1():
    assert 'rony'=='rony'
