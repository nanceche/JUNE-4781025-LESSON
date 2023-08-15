import testing_function

def test_sequence():
    assert testing_function.count([5,4,3],1) == 0

def test_sequencea():
    assert testing_function.count([5,4,3,4,4],4) == 3

