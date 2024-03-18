#-----------------------------
#
#ID:your ID
#Name:your name
#
#-----------------------------


#-----------------------------
#function of the class
#-----------------------------
class Student(object):

    #-----------------------------
    # define constructor method HERE
    # comment HERE
    #-----------------------------
    def __init__(self, student_name, student_id, gender, major):
        self.__name=student_name
        self.__id=student_id
        self.__gender=gender
        self.__major=major
        self.__number_courses=0
        self.__courses_list=[]
    
    #-----------------------------
    # define getters HERE
    #-----------------------------

    def get_name(self):
        name = self.__name
        return name

    def get_id(self):
        return self.__id

    def get_gender(self):
        return self.__gender

    def get_major(self):
        return self.__major


    def get_number_courses(self):
        return self.__number_courses

    def get_courses(self):
        return self.__courses_list

    #-----------------------------
    # define setters HERE
    #-----------------------------


    def set_name(self,student_name):
        self.__name = student_name


    def set_id(self,student_id):
        self.__id = student_id


    def set_gender(self,gender):
        self.__gender = gender

    def set_major(self,major):
        self.__major = major

    def set_number_courses(self,number_courses):
        self.__number_courses = number_courses


    def set_courses_list(self,courses_list):
        self.__courses_list = courses_list




    


if __name__=="__main__":
    pass

