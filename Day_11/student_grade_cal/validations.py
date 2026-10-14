import grades

def validation(mark):
    while True:
        try:
            return grades.grades(float(input(mark)))
        except (TypeError,ValueError) as e:
            return print(f"Invalid input : {str(e)}")

