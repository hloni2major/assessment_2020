import unittest

from src.question_one import QuestionOne


class TestQuestionOne(unittest.TestCase):
    """ It tests methods for Question One in the exercise """

    def test_sorted_letters_takes_text_with_more_than_two_alphaberts(self):
        """Test see if the provided text has a minimun of 2 characters in it"""
        instance = QuestionOne("I am a test here...")
        self.assertTrue(
            len(instance.sorted_letters()) > 2)

    def test_sorted_letters_raises_exception_on_empty_text(self):
        """Test that sorted_letters raises a ValueException on null text"""
        instance = QuestionOne("")
        with self.assertRaises(ValueError):
            instance.sorted_letters()

    def test_sorted_letters_returns_lowercase_string(self):
        """Test that the returned string is all lowercase values"""
        text = "This is a test"
        instance = QuestionOne(text)
        self.assertTrue(instance.sorted_letters().islower())

    def test_sorted_letters_returns_sorted_string_of_alphaberts(self):
        """Test if the returned value is a sorted string of alphaberts"""
        """in the original string"""
        text = "cool gang"
        instance = QuestionOne(text)
        self.assertEqual(instance.sorted_letters(), "acgglnoo")

    def test_sorted_letters_ignores_punctuation_marks(self):
        """Test if the sorted_letters method ignores punctuation marks/characters"""
        test_input = "@cool gang#$%!!"
        expected_result = "acgglnoo"
        instance = QuestionOne(text=test_input)
        self.assertEqual(instance.sorted_letters(), expected_result)


if __name__ == '__main__':
    unittest.main()
