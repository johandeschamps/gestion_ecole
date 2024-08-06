import copy
import datetime
import os
from typing import List, Callable, Optional, TypeVar

from src.address import Address
from src.course import Course
from src.director import Director
import subprocess, platform

from src.inputable import Inputable
from src.student import Student
from src.teacher import Teacher

T = TypeVar('T', bound='Inputable')


def asc_modify(list: List[T], header: str, other: List[T],add: Optional[Callable[[List[T], T], None]] = None,remove: Optional[Callable[[List[T], T], None]] = None):
    """

    :param list: List to choose from
    :param header: List's header
    :param other: List to modify
    """
    while True:
        print(header)
        for l, x in enumerate(list):
            print(l, "-", x)
        print("Actuels")
        for l, x in enumerate(other):
            print(l, "-", x)

        print()

        e = input("Action (aN ajouter, dN supprimer N) :").lower().strip().replace(" ", "")

        if e.startswith("a"):
            e = e[1:]
            a = list[int(e)]
            if a in other:
                print("Déjà présent")
            else:
                if add is not None:
                    add(other,a)
                else:
                    other.append(a)
        elif e.startswith("d"):
            l = int(e[1:])
            if remove is None:
                del other[l]
            else:
                remove(other,other[l])
        else:
            break


def reference(list: List[T]) -> Optional[T]:
    """
    Ask the user an element in the list
    :param list: list to choose from
    :return: element
    """
    while True:
        for ps, x in enumerate(list):
            print(ps, "-", str(x))
        print()
        e = input("Sélectionnez :").lower().strip().replace(" ", "")
        if e == "":
            return None
        return list[int(e)]


def list_manage(list: List[T], name, base: T, onAdd: Optional[Callable[[List[T], T], None]] = None):
    """
    Allow the user to add and remove element from the list
    :param list:
    :param name: unused
    :param base: dummy instance
    :param onAdd: callback when an element is added
    :return:
    """
    cn = True

    while cn:
        for ps, x in enumerate(list):
            print(ps, "-", str(x))
        print()
        e = input("Action (a ajouter, dN supprimer N, eN modifier) :").lower().strip().replace(" ", "")
        if e.startswith("a"):
            new = copy.deepcopy(base)
            new.user_input()
            if onAdd is not None:
                onAdd(list, new)
            list.append(new)
        elif e.startswith("e"):
            e = e[1:]
            list[int(e)].user_input()

        elif e.startswith("d"):
            e = e[1:]
            del list[int(e)]
        else:
            break


def student(st: Student):
    while True:
        print("1. Consulter notes")
        print("2. Consulter cours")

        n = input("")

        match n:
            case "1":
                cours = reference(st.courses)
                if cours is not None:
                    print("Note (0 = non remplit)", st.get_note(cours))
            case "2":
                for x in st.courses:
                    print(x)


def teacher(teacher: Teacher):
    while True:
        print("1. Editer cours")
        print("2. Consulter notes")
        print("3. Modifier notes")

        n = input("")
        match n:
            case "1":
                cours = reference(teacher.courses)
                if cours is not None:
                    cours.user_input()
            case "2":
                cours = reference(teacher.courses)
                if cours is not None:
                    for s in cours.students:
                        print("Note de", s.first_name, s.last_name, s.get_note(cours).note)
            case "3":
                cours = reference(teacher.courses)
                if cours is not None:
                    eleve = reference(cours.students)
                    if eleve is not None:
                        note = eleve.get_note(cours)
                        note.user_input()


def main():
    x = Director("A", "A", 29, Address(3, "X", "Z"))

    x.add_student(Student("A", "A", 29, Address(3, "X", "Z"), -1))

    x.add_teacher(Teacher("X", "A", 29, Address(3, "X", "Z"), datetime.date.today()))

    x.add_course(Course("F", datetime.date.today(), datetime.date.today(), []))

    x.teachers[0].courses.append(x.courses[0])

    x.courses[0].add_student(x.students[0])

    #student(x.students[0])

    #x.add_course(Course("A",datetime.datetime.now(datetime.UTC),datetime.datetime.now(datetime.UTC)))

    while True:

        print("1. Modifier enseignants")
        print("2. Modifier élèves")
        print("3. Editer cours")
        print("4. Assigner élèves au cours")
        print("5. Assigner cours")

        inp = input("")

        match inp:
            case "1":
                list_manage(x.teachers, "Enseignants", Teacher("", "", 0, Address(0, "", ""), datetime.datetime.min))
            case "2":
                def st_callback(list: List[Student], std: Student):
                    i = 0
                    for x in list:
                        i = max(i, x.id)
                    i += 1
                    std.id = i

                list_manage(x.students, "Eleves", Student("", "", 0, Address(0, "", ""), 0), st_callback)

            case "3":
                list_manage(x.courses, "Cours", Course("", datetime.datetime.min, datetime.datetime.min, []))
            case "4":
                print("Cours")
                cours = reference(x.courses)



                if cours is not None:
                    def st_add(lst : List[Student],student : Student):
                        cours.add_student(student)

                    def st_remove(lst : List[Student], student: Student):
                        cours.remove_student(student)

                    asc_modify(x.students, "Elèves", cours.students,st_add,st_remove)
            case "5":
                teach = reference(x.teachers)
                if teach is not None:
                    asc_modify(x.courses, "Cours", teach.courses)
            case "":
                break


main()
