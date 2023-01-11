from argparse import Namespace
import time
import os, sys, subprocess 
from copyreg import constructor
from string import printable
import maskpass
from random import choice, randint, shuffle
import sqlite3
import pandas as pd
from fpdf import FPDF

student_conn = sqlite3.connect("cl24.db") # This is to call out UTME Students data from the DB
cur = student_conn.cursor()
cur.execute("SELECT MatricNo, Names FROM UTME_STUDENTS UNION SELECT MatricNo, Names FROM DE_STUDENTS;")
all_students = cur.fetchall()
cur.execute("SELECT * FROM UTME_STUDENTS UNION SELECT * FROM DE_STUDENTS;")
studentinfo = cur.fetchall()
student_conn.close()

stu_num = [x[0] for x in all_students] 
stu_names =[x[1] for x in all_students]
dict_all_students = (({"Matric Number":stu_num,"Names":stu_names}))
list_all_students = (dict(all_students))

p = all_students
def one_grouping():
	global p
	m = input("Number of Persons per group: ")
	if not m.isdigit():
		print('-------------------------------------------------------------------------------------------------------')
		print("Invalid! Please input the number of groups you want to create")
		one_grouping()
	elif int(m) > len(p):
		print('-------------------------------------------------------------------------------------------------------')
		print("Error! The number of groups to be created is greater than number of values in DataBase")
		one_grouping()
	else:
		m = int(m)
	print('-------------------------------------------------------------------------------------------------------')
	group = []
	for i in range(int(m)):
		group.append(choice(p))
		if i in group == choice(p):
			choice(p)
	df= pd.DataFrame(group, columns=["Matric No", "Names"])
	df.index = df.index+1
	f = open("One Groupin.txt", "w")
	f.writelines(df.to_markdown())
	f.close()
	print("Group has been created \n view Grouping in 'One Grouping.txt' in source file. ")
	# print(df.to_markdown())
	print('-------------------------------------------------------------------------------------------------------')
	print('-------------------------------------------------------------------------------------------------------')


v = all_students
def multiple_random_groups():
	groups = []
	m = input("How Many Groups Do You Want To Create: ")
	if not m.isdigit():
		print('-------------------------------------------------------------------------------------------------------')
		print("Invalid! Please input the number of groups you want to create")
		multiple_random_groups()
	elif int(m) > (len(v)):
		print('-------------------------------------------------------------------------------------------------------')
		print("Error! The number of groups to be created is greater than number of values in DataBase")
		multiple_random_groups()
	else:
		m = int(m)
		shuffle(v)
		print('-------------------------------------------------------------------------------------------------------')
		for i in range(m):
			groups.append([])
		defi = len(v)// m
		for i in groups:
			for j in range(defi):
				i.append(v.pop(0))
		mod = len(v) % m
		for i in groups:
			for j in v:
				i.append(v.pop(0))	
		# pdf = FPDF()
		# pdf.add_page()
		# pdf.set_font('Arial', '', 14)
		# for i in range(m):
		# 	df = pd.DataFrame(groups[i-1], columns=["Matric No", "Names"])
		# 	df.index = df.index+1
		# 	pdf.cell(40,10,"Group" +str((i+1)), df)
		# pdf.output(str(m)+"Random Groups")
		# print(str(m)+" Random Grouping.txt has been created. go to the source folder to access it.")
		f= open(str(m)+" Random Grouping.txt", "w")	
		for i in range(m):
			df = pd.DataFrame(groups[i-1], columns=["Matric No", "Names"])
			df.index = df.index+1
			f.writelines("{} {}\n\n".format("Group" +str((i+1)), df))
			# print("Group" +str((i+1)), df)
		print(str(m)+" Random Grouping.txt has been created. go to the source folder to access it.")
		print('-------------------------------------------------------------------------------------------------------')

z = all_students
def multiple_heirachichal_groups():
	groups = []
	m = input("How Many Groups Do You Want To Create: ")
	if not m.isdigit():
		print('-------------------------------------------------------------------------------------------------------')
		print("Invalid! Please input the number of groups you want to create")
		multiple_heirachichal_groups()
	elif int(m) > len(z):
		print('-------------------------------------------------------------------------------------------------------')
		print("Error! The number of groups to be created is greater than number of values in DataBase")
		multiple_heirachichal_groups()
	else:
		m = int(m)
		print('-------------------------------------------------------------------------------------------------------')
		for i in range(m):
			groups.append([])
		defi = len(z) // m
		for i in groups:
			for j in range(defi):
				i.append(z.pop(0))
		mod = len(z) % m
		for i in groups:
			for j in z:
				i.append(z.pop(0))
		f= open(str(m)+" Orderly Grouping.txt", "w")	
		for i in range(m):
			df = pd.DataFrame(groups[i-1], columns=["Matric No", "Names"])
			df.index = df.index+1
			# print('-------------------------------------------------------------------------------------------------------')
			f.writelines("{} {}\n\n".format("Group" +str((i+1)), df))
		print(str(m)+" Orderly Grouping.txt has been created. go to the source folder to access it.")


def menu_optionA():
		user_data= input("Input an Option: ").upper()
		print('-------------------------------------------------------------------------------------------------------')
		if user_data == "A":
			one_grouping()
		elif user_data == "B":
			multiple_random_groups()
		elif user_data == "C":
			multiple_heirachichal_groups()
		elif user_data == "D":
			mainmenu()
		else: 
			print("Please input valid given options only!")
			menu_optionA()		
				    					    	

def menu_optionB():
	user_data = input("Input an Option: ").upper()
	print('-------------------------------------------------------------------------------------------------------')
	if user_data == 'A':
		print("A. Search By Matric Number \nB. Search By Student Name")
		user_enter = input("Insert An Option: ").upper()
		if user_enter == 'A':
			print('-------------------------------------------------------------------------------------------------------')
			searchStudent()
		elif user_enter == 'B':
			print('-------------------------------------------------------------------------------------------------------')
			searchNameStudent()
		else:
			print("Please input valid given options only!")
			mainmenu()
	elif user_data == 'B':
		all_students()
	elif user_data == 'C':
		mainmenu()
		print("Please input valid given options only!")
		print('-------------------------------------------------------------------------------------------------------')
		menu_optionB()
		
		
def searchStudent():
	list=[]
	m = input("Enter Student's Matric Number: ")
	if m.isnumeric():
		m = int(m)
		if m in list_all_students:
			n =(m, list_all_students[m])
			list.append(n)
			df = pd.DataFrame(list, columns=["Matric Number", "Names"])
			df.index = df.index+1
			print(df)	

		else:
			print('-------------------------------------------------------------------------------------------------------')
			print("ATTENTION: Matric Number doesn't exist in Class of 24 database.Please try a correct Matric Number")
			searchStudent()
	else:
		print('-------------------------------------------------------------------------------------------------------')
		print("Please Insert Matric Numbers Only!")
		searchStudent()

def all_students():
	filename = 'all_students.csv'
	df = pd.DataFrame(studentinfo, columns=['Matric Number', "Names", "Phone Number"])
	df.index = df.index+1
	print(df.to_csv(filename))
	print("All Students has been uploaded to Nous File")
				
def mainmenu():
	print('What would you like to do, Admin?')
	print("A. Group Students \nB. Search for Student")
	user_choice = input("Input an  option from above: ").upper()
	print('-------------------------------------------------------------------------------------------------------')
	if user_choice == "A":
		print("Pick an option most suitable for the grouping you hope to create:")
		print("A. One random group of Students\nB. Multiple random groups of Students\nC. Multiple orderly  grouping of students\nD. Back to Menu")
		print('-------------------------------------------------------------------------------------------------------')
		menu_optionA()
	elif user_choice == "B":
		print("A. Search for Student\nB. View All Students\nC. Back To Menu")
		menu_optionB()
		print('-------------------------------------------------------------------------------------------------------')		
	else:
		print("Invalid Input! Input from the listed option")
		print('-------------------------------------------------------------------------------------------------------')
		mainmenu()

def searchNameStudent():
    list=[]
    count = 0
    all_students_keys = list_all_students.keys()
    m = input("Enter Student's Name: ").upper()
    if m.isalpha():
        for key in all_students_keys:
            if m in list_all_students[key]:
                n =(key, list_all_students[key])
                list.append(n)
                count += 1
        df = pd.DataFrame(list, columns=["Matric Number", "Names"])
        df.index = df.index+1
        print('-------------------------------------------------------------------------------------------------------')
        print(df)	
                
        if count == 0:
            print('-------------------------------------------------------------------------------------------------------')
            print("ATTENTION: Name doesn't exist in Class of 24 database.Please try again!")
            searchNameStudent()
    else:
        print('-------------------------------------------------------------------------------------------------------')
        print("Please Insert Student's names Only!")
        searchNameStudent()

# searchNameStudent()

def last():
	print("Input 'Yes' to go back to Main Menu or 'No' to exit program")
	endput = input("Input: ").upper()
	if endput == 'YES':
		os.system('cls')
		subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])
		exit()
	if endput == 'NO':
		exit()
	else:
		last()

print('-------------------------------------------------------------------------------------------------------\n')
print("================================================  NOUS  ===============================================")
time.sleep(2)
print("Tailored Specifically For UNILAG PHY CLASS OF 24.")
print('-------------------------------------------------------------------------------------------------------')
time.sleep(3)
print("WELCOME ADMIN!\n\nInput the password")
password = 'mind'
time.sleep(2)
pwd = maskpass.askpass(prompt="Passcode: ", mask="*")
#pwd = input("Passcode: ")
while True:
	if pwd != password:
		print('-------------------------------------------------------------------------------------------------------')
		print("Invalid Passcode! Please insert the correct Passcode")
		pwd = maskpass.askpass(prompt="Password: ", mask="*")
		#pwd = input("Passcode: ")
	else:
		print("Access Granted...")
		break
print('-------------------------------------------------------------------------------------------------------')
time.sleep(2)
mainmenu()
print('-------------------------------------------------------------------------------------------------------')
time.sleep(2)
last()