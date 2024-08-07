from datetime import date

from menu import director_menu,teacher_menu,student_menu
# main.py

from datetime import date
from src.director import Director
from src.teacher import Teacher
from src.student import Student
from src.course import Course
from src.address import Address
from src.note import Note


def main():
    # Création des objets étudiants
    student1 = Student(
        first_name="Alice", last_name="Dupont", age=19, id=1,
        address=Address(75000, "Paris", "10 rue des Écoles"),
        courses=[], notes=[]
    )

    student2 = Student(
        first_name="Bob", last_name="Martin", age=20, id=2,
        address=Address(75011, "Paris", "15 avenue de la République"),
        courses=[], notes=[]
    )

    # Création des objets enseignants
    teacher1 = Teacher(
        first_name="Jean", last_name="Rousseau", age=40,
        address=Address(75000, "Paris", "20 rue des Fleurs"),
        entry_date=date(2010, 3, 15), courses=[]
    )

    teacher2 = Teacher(
        first_name="Marie", last_name="Leclerc", age=35,
        address=Address(75011, "Paris", "25 avenue des Champs"),
        entry_date=date(2015, 6, 1), courses=[]
    )

    # Création des cours
    course1 = Course(name="Mathématiques", begin_date=date(2024, 9, 1), end_date=date(2025, 6, 30), students=[student1])
    course2 = Course(name="Sciences", begin_date=date(2024, 9, 1), end_date=date(2025, 6, 30), students=[student2])

    # Assignation des cours aux enseignants
    teacher1.courses.append(course1)
    teacher2.courses.append(course2)

    # Création de l'objet directeur
    director = Director(
        first_name="Pierre", last_name="Durand", age=50,
        address=Address(75000, "Paris", "5 boulevard Saint-Germain"),
        students=[student1, student2],
        teachers=[teacher1, teacher2],
        courses=[course1, course2]
    )

    # Ajout des notes
    student1.notes.append(Note(student=student1, course=course1, note=16.5))
    student2.notes.append(Note(student=student2, course=course2, note=14.0))

    course1.add_student(student1)
    course2.add_student(student2)

    while True:
        print("\nChoisissez un type d'utilisateur pour tester :")
        print("1. Étudiant")
        print("2. Enseignant")
        print("3. Directeur")
        print("4. Quitter")

        user_type = input("Votre choix: ").strip()

        if user_type == "4":
            print("Au revoir!")
            break

        first_name = input("Entrez votre prénom: ").strip()
        last_name = input("Entrez votre nom: ").strip()

        if user_type == "1":
            # Rechercher un étudiant par prénom et nom
            student = next((s for s in [student1, student2] if s.first_name == first_name and s.last_name == last_name),
                           None)
            if student:
                print(f"\nBienvenue {student.first_name} {student.last_name}")
                student_menu(student)
            else:
                print("Étudiant non trouvé.")

        elif user_type == "2":
            # Rechercher un enseignant par prénom et nom
            teacher = next((t for t in [teacher1, teacher2] if t.first_name == first_name and t.last_name == last_name),
                           None)
            if teacher:
                print(f"\nBienvenue {teacher.first_name} {teacher.last_name}")
                teacher_menu(teacher)
            else:
                print("Enseignant non trouvé.")

        elif user_type == "3":
            # Rechercher un directeur par prénom et nom
            if first_name == director.first_name and last_name == director.last_name:
                print(f"\nBienvenue {director.first_name} {director.last_name}")
                director_menu(director)
            else:
                print("Directeur non trouvé.")

        else:
            print("Option non reconnue. Veuillez réessayer.")


if __name__ == "__main__":
    main()
