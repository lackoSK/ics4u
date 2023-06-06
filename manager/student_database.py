from typing import Dict, List, Union
from collections import defaultdict


class StudentDatabase:
    def __init__(self, filename: str):
        """Initializes the StudentDatabase class with the filename provided.

        Args:
            filename (str): Name of the file that contains the students' data.
        """
        self.filename = filename
        self.students = self.file_to_dictionary()

    def file_to_dictionary(self) -> Dict[str, List[List[Union[str, int]]]]:
        """Loads student data from a file and returns a dictionary.

        The keys of the dictionary are student IDs, and the values are lists
        containing information about each course the student has taken.

        Returns:
            Dict[str, List[List[Union[str, int]]]]: The dictionary of students data.
        """
        students = {}
        with open(self.filename, 'r') as file:
            next(file)  # Skip the header
            for line in file:
                data = line.strip().split(',')
                _id = data[0]
                first_name = data[1]
                last_name = data[2]
                course_code = data[3]
                mark = int(data[4])
                if _id not in students:
                    students[_id] = []
                students[_id].append([first_name, last_name, course_code, mark])
        return students

    def dictionary_to_file(self) -> None:
        """Writes the student data from the dictionary to a file.

        Each line in the file represents a student's course and mark.
        """
        with open(self.filename, 'w') as file:
            file.write("Student_id,student_first_name,student_last_name,course_code,mark\n")
            for id, courses in self.students.items():
                for course in courses:
                    file.write(f"{id},{course[0]},{course[1]},{course[2]},{course[3]}\n")

    def add_student_interface(self) -> bool:
        """
        User interface for adding a new student.

        :return: True if the student is added successfully, False otherwise.
        """
        _id = input("Enter the student's ID: ")
        if _id in self.students:
            print("A student with this ID already exists.")
            return False
        first_name = input("Enter the student's first name: ")
        last_name = input("Enter the student's last name: ")
        course_code = input("Enter the course code: ")
        try:
            mark = int(input("Enter the student's mark: "))

            if mark < 0 or mark > 100:
                raise ValueError
        except ValueError:
            print("Invalid input for mark. Mark should be an integer within 0-100.")
            return False
        if self.add_student(_id, first_name, last_name, course_code, mark):
            print("Student has been added.")
            return True
        else:
            print("Failed to add student.")
            return False

    def edit_student_interface(self) -> bool:
        """
        User interface for editing a student's mark.

        :return: True if the student's mark is edited successfully, False otherwise.
        """
        _id = input("Enter the student's ID to be edited: ")
        if _id not in self.students:
            print("Student does not exist.")
            return False
        self.print_student(_id)
        edit = input("Do you want to edit ? (Y/N): ")
        if edit.lower() == 'y':
            course_code = input("Enter the course you want to edit: ")
            try:
                new_mark = int(input("Enter the new mark: "))

                if new_mark < 0 or new_mark > 100:
                    raise ValueError
            except ValueError:
                print("Invalid input for mark. Mark should be an integer within 0-100.")
                return False
            if self.edit_student(_id, course_code, new_mark):
                print("Student's mark has been updated.")
                return True
            else:
                print("Failed to update student's mark.")
                return False
        else:
            return False

    def delete_student_interface(self) -> bool:
        """
        User interface for deleting a student.

        :return: True if the student is deleted successfully, False otherwise.
        """
        _id = input("Enter the student's ID to be deleted: ")
        if _id not in self.students:
            print("Student does not exist.")
            return False
        self.print_student(_id)
        delete = input("Do you want to delete ? (Y/N): ")
        if delete.lower() == 'y':
            if self.delete_student(_id):
                print("Student has been deleted.")
                return True
            else:
                print("Failed to delete student.")
                return False
        else:
            return False

    def print_student(self, _id: str) -> None:
        """Prints the information of a student.

        :param _id: The student's ID.
        :return: None
        """
        if _id not in self.students:
            print("Student does not exist.")
            return

        print("###################################################")
        print("| STUDENT ID | Full name            | Course name | Mark")

        for course in self.students[_id]:
            full_name = f"{course[0]} {course[1]}"
            course_code = course[2]
            mark = str(course[3])
            # fill spaces on right until it reaches a width of X characters
            print(f"| {_id.ljust(10)} | {full_name.ljust(20)} | {course_code.ljust(11)} | {mark}")

        print("###################################################")

    def delete_student(self, _id: str) -> bool:
        """Deletes a student from the database.

        :param _id: The ID of the student.
        :return: True if the student was successfully deleted, False otherwise.
        """
        if _id in self.students:
            del self.students[_id]
            self.dictionary_to_file()  # Update the file after deleting the student
            return True
        else:
            return False

    def add_student(self, _id: str, first_name: str, last_name: str, course_code: str, mark: int) -> bool:
        """Adds a new student to the students' dictionary.

        :param _id: The ID of the student.
        :param first_name: The first name of the student.
        :param last_name: The last name of the student.
        :param course_code: The code of the course.
        :param mark: The mark of the student.
        :return: True if the student was added successfully, False otherwise.
        """
        if _id in self.students:
            print("A student with this ID already exists.")
            return False

        self.students[_id] = [[first_name, last_name, course_code, mark]]
        self.dictionary_to_file()
        return True

    def edit_student(self, _id: str, course_code: str, new_mark: int) -> bool:
        """Edits a student's mark for a specific course.

        If the course does not exist for the student, a new line of information for that student is created with that new course and mark.

        :param _id: The ID of the student.
        :param course_code: The code of the course to edit.
        :param new_mark: The new mark.
        :return: True if the mark was successfully edited, False otherwise.
        """
        if isinstance(new_mark, int) and _id and course_code:
            for course in self.students[_id]:
                if course[2] == course_code:
                    course[3] = new_mark
                    self.dictionary_to_file()  # Update the file after editing the mark
                    return True
            # If the course does not exist for the student
            first_name = self.students[_id][0][0]
            last_name = self.students[_id][0][1]
            self.students[_id].append([first_name, last_name, course_code, new_mark])
            self.dictionary_to_file()  # Update the file after adding a new course for the student
            return True
        else:
            return False

    def report_all(self) -> None:
        """
        Prints the report of all students.

        :return: None
        """
        print("###################################################")
        print("| STUDENT ID | Full name            | Course name | Mark")

        # Sort by full name (first name + last name)
        for _id, courses in sorted(self.students.items(), key=lambda x: f"{x[1][0][0]} {x[1][0][1]}"):
            for course in courses:
                full_name = f"{course[0]} {course[1]}"
                course_code = course[2]
                mark = str(course[3])
                print(f"| {_id.ljust(10)} | {full_name.ljust(20)} | {course_code.ljust(11)} | {mark}")

        print("###################################################")

    def report_by_course(self, course_name: str) -> None:
        """Prints the report of students who are enrolled in a specific course.

        :param course_name: The name of the course.
        :return: None
        """
        print("###################################################")
        print("| STUDENT ID | Full name            | Course name | Mark")

        # Filter by course name and sort by mark
        for _id, courses in sorted(self.students.items(), key=lambda x:
        next((course for course in x[1] if course[2] == course_name), [None, None, None, 0])[3], reverse=True):
            for course in courses:
                if course[2] != course_name:
                    continue

                full_name = f"{course[0]} {course[1]}"
                mark = str(course[3])
                print(f"| {_id.ljust(10)} | {full_name.ljust(20)} | {course_name.ljust(11)} | {mark}")

        print("###################################################")

    def individual_report(self, _id: str) -> None:
        """Prints the report of a specific student.

        :param _id: The ID of the student.
        :return: None
        """
        if _id not in self.students:
            print("No such student.")
            return

        full_name = f"{self.students[_id][0][0]} {self.students[_id][0][1]}"
        average_mark = sum([course[3] for course in self.students[_id]]) / len(self.students[_id])

        print("###################################################")
        print(f"| STUDENT ID: {_id}")
        print(f"| Full name: {full_name}")
        print(f"| Average: {average_mark}")
        print("| Course name | Mark")

        for course in self.students[_id]:
            course_code = course[2]
            mark = str(course[3])
            print(f"| {course_code.ljust(11)} | {mark}")

        print("###################################################")

    def report_failed_courses(self) -> None:
        """Prints the report of students who failed one or more courses."""
        print("Student ID | Full name       | Failed courses | Mark")
        for _id, courses in self.students.items():
            failed_courses = [(course[2], course[3]) for course in courses if course[3] < 50]
            if failed_courses:
                full_name = f"{courses[0][0]} {courses[0][1]}"
                print(f"{_id.ljust(10)} | {full_name.ljust(15)} |", end=" ")
                for i, (course_code, mark) in enumerate(failed_courses):  # returns a tuple (index, element)
                    if i != 0:
                        print(f"{' '.ljust(29)}| {course_code.ljust(14)} | {mark}")
                    else:
                        print(f"{course_code.ljust(14)} | {mark}")

    def report_highest_average(self) -> None:
        """Prints the report of student(s) whose average is the highest in the school."""
        averages = {_id: sum([course[3] for course in courses]) / len(courses) for _id, courses in
                    self.students.items()}
        max_average = max(averages.values())
        max_average_students = [_id for _id, average in averages.items() if average == max_average]

        print("Student ID | Full name       | Average")
        for _id in max_average_students:
            full_name = f"{self.students[_id][0][0]} {self.students[_id][0][1]}"
            print(f"{_id.ljust(10)} | {full_name.ljust(15)} | {max_average}")

    def report_lowest_average(self) -> None:
        """Prints the report of student(s) whose average is the lowest in the school."""
        averages = {_id: sum([course[3] for course in courses]) / len(courses) for _id, courses in
                    self.students.items()}
        min_average = min(averages.values())
        min_average_students = [_id for _id, average in averages.items() if average == min_average]

        print("Student ID | Full name       | Average")
        for _id in min_average_students:
            full_name = f"{self.students[_id][0][0]} {self.students[_id][0][1]}"
            print(f"{_id.ljust(10)} | {full_name.ljust(15)} | {min_average}")

    def report_top_mark_in_each_course(self) -> None:
        """Prints the report of students who got the top mark in each course."""
        courses = defaultdict(list)
        for _id, data in self.students.items():
            for course in data:
                courses[course[2]].append((_id, f"{course[0]} {course[1]}", course[3]))

        print("Student ID | Full name       | Course  | Mark")
        for course_name, students in courses.items():
            top_student = max(students, key=lambda x: x[2])
            print(
                f"{top_student[0].ljust(10)} | {top_student[1].ljust(15)} | {course_name.ljust(7)} | {top_student[2]}")
