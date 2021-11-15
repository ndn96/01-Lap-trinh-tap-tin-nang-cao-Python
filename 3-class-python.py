# A. Import all module before using:
import pickle
# Requirement 1:- Xây dựng 3 lớp Person, Student và Professor như bảng thiết kế ở trên
print('# Requirement 1:- Xây dựng 3 lớp Person, Student và Professor như bảng thiết kế ở trên')

# Define storeData into save file with Pickle
def storeData(inputData, saveFileName):
    dbfile = open(f'{saveFileName}.json', 'wb')

    # source, destination
    pickle.dump(inputData, dbfile)
    dbfile.close()

# Define loadData into load data from file with Pickle
def loadData(fileName):
    # for reading also binary mode is important
    dbfile = open(f'{fileName}.json', 'rb')
    db = pickle.load(dbfile)
    for keys in db:
        print(keys)
    dbfile.close()

# Person Class
class Person:
  def __init__(self, name, phoneNumber, emailAddress):
    self.name = name
    self.phoneNumber = phoneNumber
    self.emailAddress = emailAddress
  def showInfo(self):
    print(self.name, self.phoneNumber, self.emailAddress)

# Student Class
class Student(Person):
  def __init__(self,studentNumber,name,phoneNumber, emailAddress, averageMark):
    super().__init__(name, phoneNumber, emailAddress)
    self.studentNumber = studentNumber
    self.averageMark = averageMark
  def showInfo(self):
    print(self.name, self.phoneNumber, self.emailAddress, self.studentNumber, self.averageMark)
  def learningExercise(self):
    print(self.name,' is learning excercise!')


# Professor Class
class Professor(Person):
  def __init__(self,professorNumber, name, phoneNumber, emailAddress, salary):
    super().__init__(name, phoneNumber, emailAddress)
    self.professorNumber = professorNumber
    self.salary = salary
  def showInfo(self):
    print(self.name, self.phoneNumber, self.emailAddress, self.salary)
# Requirement 2,3,4 được tạo tự động trong chương trình thông qua vòng for
print('# Requirement 2,3,4 được tạo tự động trong chương trình thông qua vòng for')
# Main function:
def __main__():
  # S1: Make empty list with corresponding list:
  _personList = []
  _professorList = []
  _studentList = []
  for i in range(1, 11):
    # S1. Init instance from Person Class:
    person = Person(f'Person{i}', f'011111122{i}', f'Person{i}@gmail.com')
    _personList.append({
      'name': person.name,
      'phoneNumber': person.phoneNumber,
      'emailAddress': person.emailAddress})
    # S2. Init instance from Professor Class:
    professor = Professor(f'ProfessorID{i}', f'Professor {i}', f'024311122{i}', f'ProfessorE{i}@gmail.com',
                          f'{10000 - i}')
    _professorList.append({
      'id': professor.professorNumber,
      'name': professor.name,
      'phoneNumber': professor.phoneNumber,
      'emailAddress': professor.emailAddress,
      'salary': professor.salary})
    # S3. Init instance from Student Class:
    student = Student(f'StudentID{i}', f'Student {i}', f'012311122{i}', f'Student{i}@gmail.com', f'{10 - i}')
    _studentList.append({
      'id': student.studentNumber,
      'name': student.name,
      'phoneNumber': student.phoneNumber,
      'emailAddress': student.emailAddress,
      'averageMark': student.averageMark})
  # Requirement 4: In kết quả 3 danh sách trên ra màn
  print('# Requirement 4: In kết quả 3 danh sách trên ra màn')
  print(f'personList: {_personList}')
  print(f'_professorList: {_professorList}')
  print(f'_studentList: {_studentList}')

  # Requirement 5: Sắp xếp danh sách Person giảm dần theo Name; sắp xếp danh sách Student giảm dần theo
  # Average Mark; và sắp xếp danh sách Professor tăng dần theo Salary
  # Sắp xếp lại DS theo các tiêu chí:
  print('# Requirement 5: Sắp xếp danh sách Person giảm dần theo Name...')
  sortWithName = lambda value: value['name']
  sortWithAverageMark = lambda value: value['averageMark']
  sortWithSalary = lambda value: value['salary']
  _personList.sort(reverse=True, key=sortWithName)
  _studentList.sort(reverse=True, key=sortWithAverageMark)
  _professorList.sort(reverse=False, key=sortWithSalary)
  for i in range(0, len(_professorList)):
    print(_professorList[i])
  for i in range(0, len(_professorList)):
    print(_professorList[i])
  for i in range(0, len(_professorList)):
    print(_professorList[i])
  # Requirement 7:
  print('#Requirement 7: Lưu tuần tự 3 danh sách này vào 3 tập tin khác nhau (sử dụng pickle)')
  # S1. Save data with corresponding list:
  storeData(_personList, '_personList')
  storeData(_professorList, '_professorList')
  storeData(_studentList, '_studentList')
  # Requirement 8:
  print('# Requirement 8:Đọc các tập tin này và in kết quả ra màn hình.')
  # S2. Load data with corresponding list:
  loadData('_personList')
  loadData('_professorList')
  loadData('_studentList')
# D. Call Main function
__main__()