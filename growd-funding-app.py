import re
import json
from os import path
from datetime import datetime
from tabulate import tabulate

Users=[]
# filename = './users.json'

class FileHandler:
    @staticmethod
    def createFile(filename):
        if not path.isfile(filename):
            with open(filename, 'w') as json_file:
                json.dump(Users, json_file,indent=4, separators=(',', ': '))

    @staticmethod
    def readFile(filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            print("Mohamed")
            data = []
        return data
    @staticmethod
    def updateFile(newUser,filename): 
        data = FileHandler.readFile(filename)  
        if isinstance(newUser,User) :
            if(not User.checkEmailUniqueness(newUser['email'],data)):
                raise ValueError('Email is alread exists!')
        Users.append(newUser) 
        data.append(newUser)
        with open(filename, "w") as file:
            json.dump(data, file, indent=4)
                

class ReularExpression:
    @staticmethod
    def _generalPattern(pattern,myStr):
        newPattern = re.compile(pattern)
        return re.match(newPattern,myStr)
    
    @staticmethod
    def isName(myStr):
        return ReularExpression._generalPattern(r'^[a-zA-Z]+$',myStr)

    @staticmethod
    def isEmail(myStr):
        return ReularExpression._generalPattern(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',myStr)

    @staticmethod
    def isPassword(myStr):
        return ReularExpression._generalPattern(r'(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$',myStr)

    @staticmethod
    def isPhone(myStr):
        return ReularExpression._generalPattern(r'^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$',myStr)
    
    @staticmethod
    def isNumber(myStr):
        return ReularExpression._generalPattern(r'^[0-9]+$',myStr)


class User:
    def __init__(self,fname='Default',lname='Default',email='default@gmail.com', password='Mm@251998', phone='01124720642'):
        self.fname=fname
        self.lname=lname
        self.email=email
        self.password=password
        self.phone=phone
        
    @property
    def fname(self):
        return self.__fname
    
    @fname.setter
    def fname(self,fname):
        if (ReularExpression.isName(fname)):
            self.__fname=fname
        else:
            raise ValueError("Please enter alphaptics only in your name! 🙂") 
        
    @property
    def lname(self):
        return self.__lname
    
    @lname.setter
    def lname(self,lname):
        if (ReularExpression.isName(lname)):
            self.__lname=lname
        else:
            raise ValueError("Please enter alphaptics only in your name! 🙂") 


    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self,email):
        

        if (ReularExpression.isEmail(email)):
            self.__email=email
            return True
        else :
            raise ValueError("Please enter valid email! 🙂") 

    
    @property
    def password(self):
        return self.__password
    
    @password.setter
    def password(self,password):
        if (ReularExpression.isPassword(password)):
            self.__password=password
        else:
            raise ValueError("A password contains at least eight characters, including at least one number and includes both lower and uppercase letters and special characters, for example #, ?, !")

    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self,phone):
        if (ReularExpression.isPhone(phone)):
            self.__phone=phone
        else:
            raise ValueError("Please enter valid phone! 🙂")

    def confirmPassword(self,confirmPass):
        return self.password==confirmPass
    
    
    @staticmethod
    def checkEmailUniqueness(email, users):
        for user in users:
            if user['email'] == email:         
                return False
        return True

    @staticmethod
    def loopIsNotValid(instance, attribute, message):
        isValid = False
        while not isValid:
            try:
                setattr(instance, attribute, input(message))
                isValid = True
            except ValueError as err:
                print(err)
                isValid = False
                continue

class programFunction():
    @staticmethod
    def register():
        newUser = User()
        User.loopIsNotValid(newUser,'fname',"Please Enter your first Name :")
        User.loopIsNotValid(newUser,'lname',"Please Enter your last Name :")
        User.loopIsNotValid(newUser,'password',"Please Enter your password :")
        User.loopIsNotValid(newUser,'phone',"Please Enter your phone :")
        User.loopIsNotValid(newUser,'email',"Please Enter your email :")
        print(newUser.fname)
        newUser = {
            'fname': newUser.fname,
            'lname': newUser.lname,
            'password': newUser.password,
            'phone': newUser.phone,
            'email': newUser.email
        }
        FileHandler.createFile('./users.json')
        try:
            FileHandler.updateFile(newUser,'./users.json')
        except ValueError as err:
            print(err)
    def login(email):
        password = input("Enter your password: ")
        data = FileHandler.readFile('./users.json')
        for user in data:
            if(user['email']==email and user['password']==password):
                print("Your email already exists")
                return True
        print("Your email or password is incorrect")
        return False
    
class Project:
    def __init__(self, details='Default', title='Default', total_target='25000', start_date='2024-05-02', end_date='2025-05-02'):
        self.details = details
        self.title = title
        self.total_target = total_target
        self.start_date = start_date
        self.end_date = end_date

    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, title):
        if ReularExpression.isName(title):
            self.__title = title
        else:
            raise ValueError("Please enter alphabetic characters only in your title! 🙂") 

    @property
    def details(self):
        return self.__details
    
    @details.setter
    def details(self, details):
        self.__details = details

    @property
    def total_target(self):
        return self.__total_target
    
    @total_target.setter
    def total_target(self, total_target):
        if ReularExpression.isNumber(total_target):
            self.__total_target = total_target
        else:
            raise ValueError("Please enter a number! 🙂") 

    @property
    def start_date(self):
        return self.__start_date
    
    @start_date.setter
    def start_date(self, start_date):
        try:
            self.__start_date = datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError as err:
            raise ValueError("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
        if(self.__start_date<datetime.now()):
                raise ValueError("Date must be after today")
    @property
    def end_date(self):
        return self.__end_date
    
    @end_date.setter
    def end_date(self, end_date):
        try:
            self.__end_date = datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid date format. Please enter the date in the format YYYY-MM-DD.")
        if(self.__end_date<self.__start_date):
                raise ValueError("End date must be after start date")

    @staticmethod
    def display_projects():
        projects = FileHandler.readFile('.projects.json')
        print("{:<20} {:<20} {:<15} {:<30} {:<30}".format('Title', 'Details', 'Total Target', 'Start Date', 'End Date'))
        print("-" * 1)  
        for project in projects:
            print("{:<20} {:<20} {:<15} {:<30} {:<30}".format(
                project['title'],
                project['details'],
                project['total_target'],
                project['start_date'],
                project['end_date']
            ))

    @staticmethod
    def update_projects(email):
        print("Enter the number of project you want update it")
        projects = FileHandler.readFile('.projects.json')
        i=1
        for project in projects:
            if(project['email']==email):
                print(i,project['title'])
            i=i+1
        project_number=input("Enter number of project you want update it: ")
        key_name=input("Enter key you want update it: ")
        value=input("Enter value: ")
        projects[int(project_number)-1][key_name]=value
        with open('.projects.json', "w") as file:
            json.dump(projects, file, indent=4)

    @staticmethod
    def delete_projects(email):
        print("Enter the number of project you want update it")
        projects = FileHandler.readFile('.projects.json')  
        i=1
        for project in projects:
            if(project['email']==email):
                print(i,project['title'])
            i=i+1
        project_number=input("Enter number of project you want delete it: ")
        projects.pop(int(project_number)-1)
        with open('.projects.json', "w") as file:
            json.dump(projects, file, indent=4)







    @staticmethod
    def create_project(email):
        newProject = Project()
        User.loopIsNotValid(newProject, 'title', "Please Enter your title: ")
        User.loopIsNotValid(newProject, 'details', "Please Enter your details: ")
        User.loopIsNotValid(newProject, 'total_target', "Please Enter your total target: ")
        User.loopIsNotValid(newProject, 'start_date', "Enter a start date (YYYY-MM-DD): ")
        User.loopIsNotValid(newProject, 'end_date', "Enter an end date (YYYY-MM-DD): ")
        project_data = {
            'title': newProject.title,
            'details': newProject.details,
            'total_target': newProject.total_target,
            'start_date': str(newProject.start_date),
            'end_date': str(newProject.end_date),
            "email":email
        }
        FileHandler.createFile('.projects.json')
        try:
            FileHandler.updateFile(project_data, '.projects.json')
            return project_data
        except ValueError as err:
            print(err)


#! Program will start 
print("Welcome to Crowdfunding App ❤")
state=input('''
1- register
2- login
''')
if(state == '1' ):
    programFunction.register()
if(state == '2'):
    email = input("Enter your email: ")
    programFunction.login(email)
    CRUDs=input('''
1- Create your project
2- Update your Project
3- Delete your Project
4- Display All Projects
''')
if(CRUDs == '1'):
    Project.create_project(email)
if(CRUDs == '2'):
    Project.update_projects(email)
if(CRUDs == '3'):
    Project.delete_projects(email)
if(CRUDs == '4'):
    Project.display_projects()
    




