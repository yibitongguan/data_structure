# encoding:utf-8
"""
@author = Dcm
@create_time = 2018/8/22 20:40
"""
import datetime

# 定义异常类
class PersonTypeError(TypeError):
    pass
class PersonValueError(ValueError):
    pass

"""
父类
"""
class Person:
    _num = 0

    # 计数
    @classmethod
    def num(cls):
        return cls._num

    def __init__(self, name, sex, birthday, ident):
        if not (isinstance(name, str) and sex in ('男', '女')):
            raise PersonValueError(name, sex)
        try:
            birth = datetime.date(*birthday)
        except:
            raise PersonValueError("Wrong date:", birthday)
        self._name = name
        self._sex = sex
        self._birthday = birth
        self._id = ident
        Person._num += 1  # 计数

    def id(self):
        return self._id

    def name(self):
        return self._name

    def sex(self):
        return self._sex

    def birthday(self):
        return self._birthday

    def age(self):
        return datetime.date.today().year - self._birthday.year

    def set_name(self, name):
        if not isinstance(name, str):
            raise PersonValueError("set_name", name)
        self._name = name

    # 小于
    def __lt__(self, another):
        if not isinstance(another, Person):
            raise PersonTypeError(another)
        return self._id < another.id()

    def __str__(self):
        return " ".join((self._id, self._name, self._sex, str(self._birthday)))

    def details(self):
        return ", ".join(("编号：" + self._id,
                          "姓名：" + self._name,
                          "性别：" + self._sex,
                          "出生日期：" + str(self._birthday)))

"""
学生类
"""
class Student(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls):  # 学号生成规则
        cls._id_num += 1
        year = datetime.date.today().year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, department):
        super().__init__(name, sex, birthday, Student._id_gen())
        self._department = department
        self._enroll_date = datetime.date.today()  # 入学时间
        self._courses = {}  # 记录课程、成绩的字典

    def department(self):
        return self._department

    def enroll_date(self):
        return self._enroll_date

    def course(self):
        return self._courses

    # 设置课程
    def set_course(self, course_name):
        self._courses[course_name] = None

    # 设置成绩
    def set_score(self, course_name, score):
        if course_name not in self._courses:
            raise PersonValueError("No this course selected:", course_name)
        self._courses[course_name] = score

    def scores(self):
        return [(cname, self._courses[cname]) for cname in self._courses]

    def details(self):
        return ", ".join((super().details(),
                          "入学日期：" + str(self._enroll_date),
                          "院系：" + self._department,
                          "课程记录：" + str(self.scores())))

"""
教职工类
"""
class Staff(Person):
    _id_num = 0

    @classmethod
    def _id_gen(cls, birthday):  # 职工号生成规则
        cls._id_num += 1
        year = datetime.date(*birthday).year
        return "1{:04}{:05}".format(year, cls._id_num)

    def __init__(self, name, sex, birthday, entry_date=None):
        super().__init__(name, sex, birthday, Staff._id_gen(birthday))
        if entry_date:
            try:
                self._entry_date = datetime.date(*entry_date)
            except:
                raise PersonValueError("Wrong date:", entry_date)
        else:
            self._entry_date = datetime.date.today()
        self._salary = 2000  # 设置默认值
        self._department = "未定"
        self._position = "未定"

    def set_salary(self, amount):
        if not type(amount) is int:
            raise TypeError
        self._salary = amount

    def set_department(self, department):
        self._department = department

    def set_position(self, position):
        self._position = position

    def details(self):
        return ", ".join((super().details(),
                          "入职日期：" + str(self._entry_date),
                          "院系：" + self._department,
                          "职位：" + self._position,
                          "工资：" + str(self._salary)))

# 测试
if __name__ == '__main__':
    p1 = Student("张三", "男", (1995, 3, 2), "计算机科学与技术")
    p1.set_course("数据结构")
    p1.set_score("数据结构", 100)
    print(p1.details())
