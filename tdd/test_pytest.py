import pytest
# from pytest import mark

# @mark.parametrize("input_data, output", [
#     (True, True),
#     (False, False)
# ])
# def test_basic(input_data, output):
#     assert input_data == output
#
# from SDA_TDD.functions_pytest import is_odd
#
#
# @mark.parametrize("input_data, output", [
#     (1, True),
#     (2, False),
#     (3, False),
#     (4, True),
# ])
# def test_b(input_data, output):
#     assert is_odd(input_data) == output

# @pytest.fixture()
# def my_fixture():
#     return "TEST"
#
#
# def test_basic1(my_fixture):
#     assert my_fixture == "TEST"

# from SDA_TDD.functions_pytest import Dog, Cat, is_correct_website
#
#
# @pytest.fixture()
# def dog_fixture():
#     return Dog()
#
# @pytest.fixture()
# def dogs_fixture():
#     return [
#         Dog("Rex"),
#         Dog("Lucky"),
#         Dog("Pimpek"),
#     ]
#
#
# @pytest.fixture()
# def cat_fixture():
#     return Cat()
#
# def test_dogs_sound(dogs_fixture):
#     assert len(dogs_fixture) == 3
#     for dog in dogs_fixture:
#         assert dog.speak() == "Hau!"
#
# def test_cat_sound(cat_fixture):
#     assert cat_fixture.speak() == "Miau!"
from pytest import mark

from SDA_TDD.functions_pytest import is_correct_website

from unittest import mock

@mark.parametrize("input_data", [
    "https://google.com",
    "https://wp.pl",
    "https://onet.pl"
])

@mock.patch("SDA_TDD.functions_pytest.requests.get")
def test_is_correct_website_with_200_status_code(mock_get, input_data):
   # Given
    mock_get.return_value.status_code = 200

    # When
    output = is_correct_website(input_data)

    # Then
    assert output == True
