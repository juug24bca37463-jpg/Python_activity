Aim

To create a class for storing student details, calculate total marks, and display the student information.

Algorithm

1. Start
2. Define a class named `Student`
3. Create a method `getData()` to take input (name, USN, and 5 subject marks)
4. Create a method `total_marks()` to calculate the sum of all marks
5. Create a method `display()` to print student details and total marks
6. Create an object of the class
7. Call `getData()` to take input
8. Call `total_marks()` to compute total
9. Call `display()` to show output
10. Stop

CODE:
class Student:
    def getData(self):
        self.name = input("Enter the name: ")
        self.usn = input("Enter the USN: ")
        self.mark1 = int(input("Enter marks 1: "))
        self.mark2 = int(input("Enter marks 2: "))
        self.mark3 = int(input("Enter marks 3: "))
        self.mark4 = int(input("Enter marks 4: "))
        self.mark5 = int(input("Enter marks 5: "))

    def total_marks(self):
        self.total = self.mark1 + self.mark2 + self.mark3 + self.mark4 + self.mark5

    def display(self):
        print("\nStudent Details")
        print("Name:", self.name)
        print("USN:", self.usn)
        print("Total Marks:", self.total)


obj = Student()

obj.getData()
obj.total_marks()
obj.display()
Output 
Enter the name: Shivani
Enter the USN: 24BCA2000
Enter marks 1: 80
Enter marks 2: 91
Enter marks 3: 88
Enter marks 4: 75
Enter marks 5: 94

Student Details
Name: Shivani
USN: 24BCA2000
Total Marks: 428
