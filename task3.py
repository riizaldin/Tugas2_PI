class BMI_Calculator:
    def __init__(self, weight, height):
        self._weight = weight
        self._height = height

    @property
    def weight(self):
        return self._weight

    @property
    def height(self):
        return self._height

    def BMI_Value(self):
        bmi = self._weight / (self._height ** 2)
        return bmi

# Example usage:
if __name__ == "__main__":
    person = BMI_Calculator(weight=70, height=1.75)  # Weight in kilograms, height in meters
    print("Weight:", person.weight, "kg")
    print("Height:", person.height, "m")
    print("BMI:", person.BMI_Value())
