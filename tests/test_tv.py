from pytest import mark


# @mark.parametrize('tv_brand', [
#     ('LG'),
#     ('Samsung'),
#     ('Sony')
# ])
# iterables: use a list
# inside a list: tuples (for multiple pieces of information???)
def test_tv_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")
    pass


def test_browser_can_navigate_to_training_ground(many_browsers):
    many_browsers.get('http://techstepacademy.com/training-ground')

