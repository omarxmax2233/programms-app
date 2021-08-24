class Students:

    no_of_students = 0
    def __init__(self, name, age, ln):

        self.name = name
        self.age = age
        self.ln = ln
        Students.no_of_students += 1
    def describe (self):
        print(f"the name is {self.name} and the age is {self.age} i learn {self.ln} in evalution it's fun tere")



student_1 = Students("omar", "12.7" , "python" )
student_2= Students("youssef", "14", "python")
student_3 = Students("mahamed", "30", "java")
student_4 = Students("hana", "9", "c#")




choose = input("search or describe : ")



names1 = "name : " + student_1.name

ages1 = "age :" + student_1.age

laungage1 = "laungage : " + student_1.ln
#===========================================
names2 = "name : " + student_2.name

ages2 = "age :" + student_2.age

laungage2 = "laungage : " + student_2.ln
#==============================================
names3 = "name : " + student_3.name

ages3 = "age :" + student_3.age

laungage3 = "laungage : " + student_3.ln
#============================================
names4 = "name : " + student_4.name

ages4 = "age :" + student_4.age

laungage4 = "laungage : " + student_4.ln

if choose == "search" :

        select = input("wich one you need : ")

        if select == "first" :

            print(names1)
            print(ages1 )
            print(laungage1)


        if select == "second" :

            print(names2)
            print( ages2 )
            print( laungage2)


        if select == "third" :

            print(names3)
            print( ages3 )
            print( laungage3)


        if select == "forth" :

            print(names4)
            print( ages4 )
            print( laungage4)



if choose == "describe" :


    select = input("wich one you need : ")

    if select == "first" :

        student_1.describe()

    if select == "second" :

        student_2.describe()



    if select == "third" :

       student_3.describe()



    if select == "forth" :

        student_4.describe()




