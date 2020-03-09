from unittest import TestCase
from unittest.mock import patch

# mock sum fonction

from unittest import TestCase
from unittest.mock import patch

class TestCalculator(TestCase):
    @patch('calculator.Calculator.sum', return_value=9)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3), 9)