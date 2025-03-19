import unittest
from bmi import calculate_bmi, bmi_category

class TestBMI(unittest.TestCase):
  def test_calculate_bmi(self):
    self.assertEqual(calculate_bmi(5, 6, 150), 24.2) # Test normal case
    self.assertEqual(calculate_bmi(5, 6, 100), 16.2) # Test underweight case
    self.assertEqual(calculate_bmi(5, 6, 200), 32.3) # Test obese case

  def test_bmi_category(self):
    self.assertEqual(bmi_category(16.2), "Underweight")
    self.assertEqual(bmi_category(24.2), "Normal weight")
    self.assertEqual(bmi_category(32.3), "Obese")

if __name__ == '__main__':
  unittest.main()
