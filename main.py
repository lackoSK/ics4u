from manager.student_registry_system import StudentRegistrySystem


def main():
    srs = StudentRegistrySystem('files/student_data.txt')
    srs.menu()


if __name__ == "__main__":
    main()
