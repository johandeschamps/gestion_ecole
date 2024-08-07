import datetime
from typing import List, TypeVar

from src import inputs
from src.address import Address
from src.course import Course

from src.director import Director

from src.student import Student
from src.teacher import Teacher
from list_utils import select_element_from_list, modify_list, modify_selected_list

T = TypeVar('T', bound='Inputable')

def student_menu(student: Student):
    print(f"\nMenu pour {student.first_name} {student.last_name} !")
    while True:
        print("1. Consulter notes")
        print("2. Consulter cours")
        print("3. Consulter les cours pour une date")
        print("4. Quitter")

        choice = input("Choisissez une option: ").strip()

        match choice:
            case "1":
                course = select_element_from_list(student.courses, "Choisissez un cours pour consulter la note: ")
                if course is not None:
                    print("Note (0 = non remplie):", student.get_note(course))
            case "2":
                for course in student.courses:
                    print(course)
            case "3":
                date = inputs.date("Date : ")
                for course in student.courses:
                    print(course)
                    course.current_course(date)
                    print()
            case "4":
                break
            case _:
                print("Option non reconnue. Veuillez réessayer.")

def teacher_menu(teacher: Teacher):
    print(f"\nMenu pour {teacher.first_name} {teacher.last_name} !")
    while True:
        print("1. Voir cours")
        print("2. Consulter notes")
        print("3. Modifier notes")
        print("4. Quitter")

        choice = input("Choisissez une option: ").strip()

        match choice:
            case "1":
                for idx, course in enumerate(teacher.courses):
                    print(idx, course)
            case "2":
                course = select_element_from_list(teacher.courses, "Choisissez un cours pour consulter les notes: ")
                if course is not None:
                    for student in course.students:
                        print("Note de", student.first_name, student.last_name, student.get_note(course).note)
            case "3":
                course = select_element_from_list(teacher.courses, "Choisissez un cours pour modifier les notes: ")
                if course is not None:
                    student = select_element_from_list(course.students, "Choisissez un élève: ")
                    if student is not None:
                        note = student.get_note(course)
                        note.user_input()
            case "4":
                break
            case _:
                print("Option non reconnue.")

def director_menu(director: Director):
    print(f"\n Menu pour {director.first_name} {director.last_name} !")
    while True:
        print("1. Modifier enseignants")
        print("2. Modifier élèves")
        print("3. Éditer cours")
        print("4. Assigner élèves au cours")
        print("5. Assigner cours")
        print("6. Quitter")

        choice = input("Choisissez une option: ").strip()

        match choice:
            case "1":
                modify_list(director.teachers, "Enseignants",Teacher("","",0,Address(2,"",""),datetime.date.min))
            case "2":
                def student_callback(student_list: List[Student], student: Student):
                    student.id = max((s.id for s in student_list), default=0) + 1

                modify_list(director.students, "Élèves", Student("","",0,Address(2,"",""),77), add_function=student_callback)
            case "3":
                modify_list(director.courses, "Cours", Course("",datetime.date.min,datetime.date.min,[]))
            case "4":
                course = select_element_from_list(director.courses, "Choisissez un cours pour modifier les élèves: ")
                if course is not None:
                    def student_add(lst: List[Student], student: Student):
                        course.add_student(student)

                    def student_remove(lst: List[Student], student: Student):
                        course.remove_student(student)

                    modify_selected_list(director.students, "Élèves", course.students, add_function=student_add, remove_function=student_remove)
            case "5":
                teacher = select_element_from_list(director.teachers, "Choisissez un enseignant pour assigner des cours: ")
                if teacher is not None:
                    modify_selected_list(director.courses, "Cours", teacher.courses)
            case "6":
                break
            case _:
                print("Option non reconnue.")