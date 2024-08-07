import copy
from typing import List, Optional, Callable, TypeVar

T = TypeVar('T',bound="Inputable")


def modify_list(
        items: List[T],
        header: str,
        dummy: T,
        add_function: Optional[Callable[[List[T], T], None]] = None,
        remove_function: Optional[Callable[[List[T], T], None]] = None
):
    """
    Fonction pour ajouter ou supprimer des éléments d'une liste avec les élément d'une autre liste

    :param items: Liste d'éléments disponibles pour modification
    :param header: En-tête affiché pour la liste des éléments
    :param dummy: Element de base
    :param add_function: Fonction appelée pour ajouter un élément
    :param remove_function: Fonction appelée pour supprimer un élément
    """
    while True:
        print(header)
        for index, item in enumerate(items):
            print(f"{index} - {item}")

        action = input("Action (a ajouter, dN supprimer N, q quitter) : ").lower().strip()

        if action.startswith("a"):
            ins = copy.deepcopy(dummy)
            ins.user_input()

            if add_function:
                add_function(items, ins)
            else:
                items.append(ins)

        elif action.startswith("d"):
            index = int(action[1:])
            if index < 0 or index >= len(items):
                print("Index invalide")
                continue
            item_to_remove = items[index]
            if remove_function:
                remove_function(items, item_to_remove)
            else:
                del items[index]

        elif action == "q":
            break

        else:
            print("Action non reconnue.")


def modify_selected_list(
        items: List[T],
        header: str,
        selected_items: List[T],
        add_function: Optional[Callable[[List[T], T], None]] = None,
        remove_function: Optional[Callable[[List[T], T], None]] = None
):
    """
    Fonction pour ajouter ou supprimer des éléments d'une liste avec les éléments d'une autre liste

    :param items: Liste d'éléments disponibles pour modification
    :param header: En-tête affiché pour la liste des éléments
    :param selected_items: Liste des éléments actuellement sélectionnés
    :param add_function: Fonction appelée pour ajouter un élément
    :param remove_function: Fonction appelée pour supprimer un élément
    """
    while True:
        print(header)
        for index, item in enumerate(items):
            print(f"{index} - {item}")

        print("Éléments actuels")
        for index, item in enumerate(selected_items):
            print(f"{index} - {item}")

        action = input("Action (aN ajouter, dN supprimer N, q quitter) : ").lower().strip()

        if action.startswith("a"):
            index = int(action[1:])
            if index < 0 or index >= len(items):
                print("Index invalide")
                continue
            item_to_add = items[index]
            if item_to_add in selected_items:
                print("Déjà présent")
            else:
                if add_function:
                    add_function(selected_items, item_to_add)
                else:
                    selected_items.append(item_to_add)

        elif action.startswith("d"):
            index = int(action[1:])
            if index < 0 or index >= len(selected_items):
                print("Index invalide")
                continue
            item_to_remove = selected_items[index]
            if remove_function:
                remove_function(selected_items, item_to_remove)
            else:
                del selected_items[index]

        elif action == "q":
            break

        else:
            print("Action non reconnue.")


def select_element_from_list(
        items: List[T],
        prompt: Optional[str] = None
) -> Optional[T]:
    """
    Demande à l'utilisateur de sélectionner un élément dans une liste.

    :param items: Liste d'éléments disponibles pour sélection
    :param prompt: Message d'invite pour la sélection
    :return: Élément sélectionné ou None si l'entrée est vide
    """
    while True:
        for index, item in enumerate(items):
            print(f"{index} - {item}")
        print()
        choice = input(prompt if prompt else "Sélectionnez un élément : ").strip()
        if not choice:
            return None
        try:
            index = int(choice)
            if 0 <= index < len(items):
                return items[index]
            else:
                print("Index hors limites. .")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un numéro.")
