import unittest
import os
import shutil

from manager.student_database import StudentDatabase


class TestStudentDatabase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.test_filename = 'test_students.txt'
        # Create a copy of the original file to use for testing
        shutil.copyfile('test_data.txt', cls.test_filename)

    def setUp(self):
        self.db = StudentDatabase(self.test_filename)

    def test_file_to_dictionary(self):
        students = self.db.file_to_dictionary()
        self.assertIsInstance(students, dict)
        self.assertIn('1001', students)

    def test_add_student(self):
        result = self.db.add_student('1020', 'New', 'Student', 'MCR3U', 85)
        self.assertTrue(result)
        self.assertIn('1020', self.db.students)

    def test_edit_student(self):
        self.db.add_student('1021', 'Edit', 'Student', 'MCR3U', 85)
        result = self.db.edit_student('1021', 'MCR3U', 90)
        self.assertTrue(result)
        self.assertEqual(self.db.students['1021'][0][3], 90)

    def test_delete_student(self):
        self.db.add_student('1022', 'Delete', 'Student', 'MCR3U', 85)
        result = self.db.delete_student('1022')
        self.assertTrue(result)
        self.assertNotIn('1022', self.db.students)

    @classmethod
    def tearDownClass(cls):
        # Delete the test file after all tests are done
        os.remove(cls.test_filename)

if __name__ == '__main__':
    unittest.main()
