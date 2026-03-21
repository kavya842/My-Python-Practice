class PythonCourse:
    python_students = []

    def __init__(self, name):
        self.name = name
    def add_python(self):
        PythonCourse.python_students.append(self.name)


class DataScienceCourse:
    ds_students = []

    def __init__(self, name):
        self.name = name
    def add_ds(self):
        DataScienceCourse.ds_students.append(self.name)


class WebTechCourse:
    webtech_students = []

    def __init__(self, name):
        self.name = name
    def add_webtech(self):
        WebTechCourse.webtech_students.append(self.name)


class Student(PythonCourse, DataScienceCourse, WebTechCourse):

    def __init__(self, name):
        PythonCourse.__init__(self, name)
        DataScienceCourse.__init__(self, name)
        WebTechCourse.__init__(self, name)


s1 = Student("Kavya")
s1.add_python()

s2 = Student("Ramya")
s2.add_ds()

s3 = Student("Harshini")
s3.add_webtech()

print("Python Students:", PythonCourse.python_students)
print("Datascience Students:", DataScienceCourse.ds_students)
print("Webtech Students:", WebTechCourse.webtech_students)