import Assignment1
# Code by Rania Sid and Amr Mousattat


def test_classifyNumber():
    assert Assignment1.classifyNumber(5)  == "positive"
    assert Assignment1.classifyNumber(-4) == "negative"
    assert Assignment1.classifyNumber(0)  == "zero"

def test_printStarShape():
    assert Assignment1.print_star_shape(1) == "*\n"
    assert Assignment1.print_star_shape(2) == "*\n**\n"

def test_sum_even():
    assert Assignment1.sum_even(1,10) == 30
    assert Assignment1.sum_even(4, 8) == 18

