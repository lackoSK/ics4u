from manager.student_database import StudentDatabase


class StudentRegistrySystem:
    def __init__(self, filename: str):
        """Initialize the StudentRegistrySystem class with a StudentDatabase instance.

        Args:
            filename (str): Name of the file that contains the students' data.
        """
        self.db = StudentDatabase(filename)

    def menu(self):
        """Display the menu and handle the user options."""
        while True:
            print("------Braemar College student registry system ------")
            print("A. Add student")
            print("B. Edit student")
            print("C. Delete student")
            print("D. Report")
            print("E. Special Report")
            print("Q. Quit")
            option = input("Enter one of these options (A-E or Q): ")

            if option.upper() == 'A':
                self.db.add_student_interface()
            elif option.upper() == 'B':
                self.db.edit_student_interface()
            elif option.upper() == 'C':
                self.db.delete_student_interface()
            elif option.upper() == 'D':
                print("1. All")
                print("2. By Course")
                print("3. By Student")
                report_option = input("Enter one of these options (1-3): ")

                if report_option == '1':
                    self.db.report_all()
                elif report_option == '2':
                    course_name = input("Enter the course name: ")
                    self.db.report_by_course(course_name)
                elif report_option == '3':
                    _id = input("Enter the student's ID: ")
                    self.db.individual_report(_id)
                else:
                    print("Invalid option. Please try again.")
            if option.upper() == 'E':
                print("1. Students who failed one or more courses")
                print("2. Student(s) whose Average is the highest in school")
                print("3. Student(s) whose Average is lowest in School")
                print("4. Students who got top mark in each course")
                report_option = input("Enter one of these options (1-4): ")

                if report_option == '1':
                    self.db.report_failed_courses()
                elif report_option == '2':
                    self.db.report_highest_average()
                elif report_option == '3':
                    self.db.report_lowest_average()
                elif report_option == '4':
                    self.db.report_top_mark_in_each_course()
            elif option.upper() == 'Q':
                print("Thank you for using the school registry system!")
                break
            else:
                print("Invalid option. Please try again.")

            self.db.dictionary_to_file()
