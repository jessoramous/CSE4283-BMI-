# Main application logic

def calculate_bmi(height_ft, height_in, weight):
  # Calculate BMI using weight (in pounds) and height (in feet and inches).
  # 1. Multiply the weight in pounds by 0.45 (the metric conversion factor)
  #   new weight = (weight) X 0.45 = ___ kg
  # 2. Multiply the height in inches by 0.025 (the metric conversion factor)
  #   new height = (total height in inches) X 0.025 = ___ m
  # 3. Square the answer from step 2
  #   height squared = (___ m)^2 
  # 4.Divide the answer from step 1 by the answer from step 3
  #  new weight / height squared = BMI
  
  total_height = (height_ft * 12) + height_in 
  weight_kg = weight * 0.45
  height_m = total_height * 0.025
  height_squared = height_m * height_m
  bmi = weight_kg / height_squared
  return round(bmi, 1)

def bmi_category(bmi):
  # Return the BMI category based on the BMI value.

  if bmi < 18.5:
    return "Underweight"
  elif 18.5 <= bmi < 25:
    return "Normal weight"
  elif 25 <= bmi < 30:
    return "Overweight"
  else:
    return "Obese"
