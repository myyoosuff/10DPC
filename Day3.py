mark = int(input("Enter your mark: "))
if mark < 0 or mark > 100:
        print("Invalid mark. Please enter a mark between 0 and 100.")
else:
        if mark >= 90:
            print("Grade: A")
        elif mark >= 80:
            print("Grade: B")
        elif mark >= 70:
            print("Grade: C")
        elif mark >= 60:
            print("Grade: D")
        else:
            print("Grade: F")