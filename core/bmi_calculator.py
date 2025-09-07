"""BMI Calculator"""


def calculate_bmi(weight_kg, height_cm):
    """A standard bmi calculator based on user inputs."""
    height_sqr = (height_cm/100)**2
    bmi = round(weight_kg/height_sqr, 2)
    return bmi
