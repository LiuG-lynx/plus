
# 处理高层业务逻辑

class Education(object):
    def __init__(self, name):
        self.name = name

    def show_info(self):
        pass

    def __str__(self):
        return '实例名为: %s' % (self.name)

class School(Education, object):
    """学校"""
    def __init__(self, name, address):
        super(School, self).__init__(name)
        self.address = address
        self.teachers = []
        self.students = []
        self.courses = []
        self.grades = []
        print("school: %s create successful" % name)  # 创建新的学校成功

    def enroll(self,student):# 学员注册
        self.students.append(student)
        print("%s enroll in %s "% (student.name, self.name))

    def leave_school(self,student): # 退学
        self.students.remove(student)
        print("%s leave school from %s " % (student.name, self.name))

    def create_course(self, name, cycle, price):
        """ 通过学校创建课程 """
        course = Course(name,cycle, price)
        self.courses.append(course)
        print("course: %s create successful" % name)
        return course

    def create_grade(self, name, teacher, course):
        """ 通过学校创建班级  班级关联课程,老师"""
        grade = Grade(name, teacher, course)  # 实例化  班级类
        self.grades.append(grade)  # 实例化的版积累 关联到学校
        print("grade: %s create successful" % grade.name)
        return grade  # 为什么要返回  存疑  通过 学校类 调用这个方法 创建 班级

    def create_teacher(self, name): # 将老师关联到学校学校
        teacher = Teacher(name, self)  # 实例化一个老师类
        self.teachers.append(teacher) # 将实例的老师类关联到学校
        print("teacher: %s create successful" %name)  # 显示是否成功
        return teacher



    def hire_teacher(self, teacher):  # 将 老师名字添加到实例学校类
        self.teachers.append(teacher)
        print("teacher: %s hire successful" % teacher.name)
    def fire_teacher(self, teacher):
        self.teachers.remove(teacher)
        print("teacher: %s fire successful" % teacher.name)




class Grade(Education, object):
    """ 班级"""

    def __init__(self, name, teacher, course):
        super(Grade, self).__init__(name)
        self.teacher = teacher
        self.course = course
        self.students = []


    def enroll(self, student):  # 学生注册
        self.students.append(student)
        print("%s enroll in %s " % (student.name, self.name))

    def leave_grade(self, student):
        self.students.remove(student)
        print("%s leave grade from  %s " % (student.name, self.name))


    def show_info(self):  #课程详情  (班级名,老师,课程名,学生列表)
        print("grade:name: %s\t teacher:%s\t course:%s\t students:%s" %
              (self.name, self.teacher, self.course, self.students))


class Student(Education, object):
    """ 创建学生类 关联学校 关联班级"""

    def __init__(self,name,school,grade,score = 0):
        super(Student, self).__init__(name)
        """ 下面为  实例化的 学生类的默认值"""
        self.score = score
        self.school = None
        self.grade = None
        self.tuition = 0  # 学费
        self.choose_school(school)  #选择学校时 的视图
        self.choose_grade(grade)


    #  学员视图用的功能 用来选择 学校 班级  缴费
    def choose_school(self, school):
        if self.school != None:
            self.school.leave_school(self)
        school.enroll(self)
        self.school = school

    def choose_grade(self,grade):
        if self.grade !=None:
            self.grade.leave_grade(self)
        grade.enroll(self)
        self.grade = grade

    def pay_tuition(self, money):
        self.tuition += money


    # 显示学生的基本信息
    def show_info(self):
        print("student:name: %s\t school:%s\t grade:%s\t score:%s\t tuition:%s"%
              (self.name, self.school, self.grade, self.score, self.tuition))


class Teacher(Education, object):
    """老师
    5. 创建讲师角色时要关联学校，
    """
    def __init__(self, name, school):
        super(Teacher, self).__init__(name)
        self.school = None
        self.choose_school(school)
        self.grade = None

    # 6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级，
    # 查看班级学员列表 ， 修改所管理的学员的成绩
    def choose_school(self, school):
        if self.school != None:
            self.school.fire_teacher(self)
        school.hire_teacher(self)
        self.school = school

    def choose_grade(self, grade):
        self.grade = grade

    def show_students(self):
        if self.grade != None:
            for student in self.grade.students:
                student.show_info()
        else:
            print("请选择班级")

    def modify_score(self, student, score):   # 给学生打分
        student.score = score

    def show_info(self):
        print("teacher:name: %s\t school:%s\t grade:%s"%
              (self.name, self.school, self.grade))


class Course(Education, object):
    """ 课程  参数: 周期 价格"""
    def __init__(self, name, cycle, price):
        super(Course, self).__init__(name)
        self.cycle = cycle
        self.price = price




if __name__ == "__main__":
    school1 = School("上海大学","上海")
    school2 = School("北京大学","北京")
    """ 实例化  teacher  course  grade"""
    teacher= school1.create_teacher("王老师")
    course = school1.create_course("数学", "1年", 2000)
    grade = school1.create_grade("高三", teacher,course)
    student = Student("Tom", school1, grade)
    student.show_info()
    teacher.modify_score(student, 70)
    teacher.show_info()
    student.show_info()