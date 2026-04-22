from gradebook import letter_grade 

def test_letter_grade_A():
    assert letter_grade(95) == 'A'

def test_letter_grade_F():
    assert letter_grade(45) == "F"

@pytest.mark.parametrize("score, expected", [(95, "A"), (45, "F")])
def test_letter_grade(score, expected):
    assert letter_grade(score) == expected

def test_letter-grade_invalid_type(score):
    if not isinstance()
    #with pytest.raises(TypeError):
        #letter_grade("hello")

def test_average_works():
    assert average([80,90,70]) == 80.0

def test_average_empty_list():
    with pytest.raises(ValueError):
        average([not a list])

def test_average_bad_items():
    with pytest.raises(TypeError):
        average([80, "ninety, 70"])