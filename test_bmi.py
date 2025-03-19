import unittest
from bmi import calculate_bmi, bmi_category

class TestBMI(unittest.TestCase):
  def test_calculate_bmi(self):
    self.assertEqual(calculate_bmi(5, 6, 150), 24.8) # Test normal case
    self.assertEqual(calculate_bmi(5, 6, 100), 16.5) # Test underweight case
    self.assertEqual(calculate_bmi(5, 6, 170), 28.1) # Test overweight case
    self.assertEqual(calculate_bmi(5, 6, 200), 33.1) # Test obese case

  def test_bmi_category(self):
    self.assertEqual(bmi_category(18.4), "Underweight")
    self.assertEqual(bmi_category(18.5), "Normal weight")
    self.assertEqual(bmi_category(24.9), "Normal weight")    
    self.assertEqual(bmi_category(25.0), "Overweight")
    self.assertEqual(bmi_category(29.9), "Overweight")
    self.assertEqual(bmi_category(30.0), "Obese")

if __name__ == '__main__':
  unittest.main()
