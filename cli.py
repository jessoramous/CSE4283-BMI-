import argparse
from bmi import calculate_bmi, bmi_category

def main():
  parser = argparse.ArgumentParser(description="BMI Calculator")
  parser.add_argument("height_ft", type=int, help="Height in feet")
  parser.add_argument("height_in", type=int, help="Height in inches")
  parser.add_argument("weight", type=int, help="Weight in pounds")

  args = parser.parse_args()

  bmi = calculate_bmi(args.height_ft, args.height_in, args.weight)
  category = bmi_category(bmi)

  print(f"BMI: {bmi}, Category: {category}")

if __name__ == "__main__":
  main()
