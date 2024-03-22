def main():
    grades = []
    while True:
        grade = input("Enter a grade (-1 to end): ")
        if grade == '-1':
            break
        grades.append(int(grade))

    if not grades:
        print("No grades entered.")
        return

    average_grade = sum(grades) // len(grades)
    print(average_grade)
    for grade in grades:
        print(grade)

if __name__ == "__main__":
    main()
