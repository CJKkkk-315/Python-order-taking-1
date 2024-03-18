#-----------------------------
#
#ID:your ID
#Name:your name
#
#-----------------------------


#-----------------------------
#function of the class
#-----------------------------
class Course(object):


    #-----------------------------
    # define constructor method HERE
    # comment HERE
    #-----------------------------

    def __init__(self, course_name, course_id, credit, instructor_name, address, description):
        self.__course_name=course_name
        self.__course_id=course_id
        self.__credit=credit
        self.__instructor_name=instructor_name
        self.__address=address
        self.__description=description

    #-----------------------------
    # define getters HERE
    #-----------------------------

    def get_course_name(self):
        return self.__course_name
    def get_course_id(self):
        return self.__course_id
    def get_credit(self):
        return self.__credit
    def get_instructor_name(self):
        return self.__instructor_name
    def get_address(self):
        return self.__address
    def get_description(self):
        return self.__description

        

    #-----------------------------
    # define setters HERE
    #-----------------------------
    def set_course_name(self,course_name):
        self.__course_name = course_name
    def set_course_id(self,course_id):
        self.__course_id = course_id
    def set_credit(self,credit):
        self.__credit = credit
    def set_instructor_name(self,instructor_name):
        self.__instructor_name = instructor_name
    def set_address(self,address):
        self.__address = address
    def set_description(self,description):
        self.__description = description


        


if __name__=="__main__":
    pass

    
