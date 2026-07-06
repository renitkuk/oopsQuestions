from abc import ABC, abstractmethod
class Person(ABC):

    @abstractmethod
    def display(self):
        pass

class Student(Person):
    def display(self):
        self.n = int(input("Enter the number of Students: "))
        self.list_of_Students = []
        self.list_of_marks = []
        for i in range(self.n):
            name = input("Enter student name: ")
            marks = int(input("Enter marks: "))
            self.list_of_Students.append(name)
            self.list_of_marks.append(marks)

    def Total(self):
        totalmarks = 0
        for i in self.list_of_marks:
            totalmarks += i
        print("\nTotal marks are:", totalmarks)

    def Average(self):
        totalmarks = 0
        for i in self.list_of_marks:
            totalmarks += i
        averagemarks = totalmarks / self.n
        print("Average marks are:", averagemarks)

    def Topper(self):
        highest = self.list_of_marks[0]
        for i in self.list_of_marks:
            if i > highest:
                highest = i
        topper_index = self.list_of_marks.index(highest)
        topper_name = self.list_of_Students[topper_index]
        print("Class Topper is:", topper_name)
        print("Topper Marks:", highest)

    def Grade(self):
        print("\nGrades:")
        for i in range(self.n):
            marks = self.list_of_marks[i]
            if marks >= 90:
                grade = "A+"
            elif marks >= 75:
                grade = "A"
            elif marks >= 60:
                grade = "B"
            elif marks >= 40:
                grade = "C"
            else:
                grade = "Fail"
            print(self.list_of_Students[i], ":", grade)

s1 = Student()
s1.display()
s1.Total()
s1.Average()
s1.Topper()
s1.Grade()
