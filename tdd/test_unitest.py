
# from SDA_TDD.functions_unittest import is_even
#
#
# class BasicTestCase(unittest.TestCase):
#
#     def test_basic(self):
#         self.assertTrue(False)
#         self.assertTrue(True)
#
#
# class IsEvenTestCase(unittest.TestCase):
#     def test_is_even_returning_true(self):
#
#         # Given
#         input_data = 4
#
#         # When
#         output = is_even(input_data)
#
#         # Then
#         self.assertEqual(output, True)
#
#     def test_is_even_returning_false(self):
#         # Given
#         input_data = 5
#
#         # When
#         output = is_even(input_data)
#
#         # Then
#         self.assertEqual(output, False)

# class BaseTestExample(unittest.TestCase):
#     def setUp(self) -> None:
#         super().setUp()
#         self.example = 5
#
#     def test_say_name_with_title(self):
#         self.assertEqual(self.example, 5)
# from SDA_TDD.functions_unittest import Person
#
#
# class PersonTestCase(unittest.TestCase):
#     def setUp(self) -> None:
#         super().setUp()
#         # Given
#         self.person = Person("John", "Snow", 30)
#
#     def test_say_name_with_title_mr(self):
#         # When
#         output = self.person.say_name_with_title("Mr.")
#         # Then
#         self.assertEqual(output, "Mr. John Snow")
#
#     def test_say_name_with_title_mrs(self):
#         # When
#         output = self.person.say_name_with_title("Mrs.")
#         # Then
#         self.assertEqual(output, "Mrs. John Snow")

import unittest

from unittest import mock

from SDA_TDD.functions_unittest import remove_file


class RemoveFileTestCase(unittest.TestCase):
    @mock.patch("SDA_TDD.functions_unittest.os.path.isfile")
    @mock.patch("SDA_TDD.functions_unittest.os.remove")
    def test_remove_file_should_remove_existing_file(self, mock_remove, mock_isfile):
        # Given
        mock_isfile.return_value = False

        # When
        remove_file("/home/michal/Szkolenie_SDA/SDA_TDD/text.xtx")

        # Then
        mock_isfile.assert_called_with("/home/michal/Szkolenie_SDA/SDA_TDD/text.xtx")
        mock_remove.assert_not_called()
