import Model
import View

def main_menu():
    while True:
        View.print_menu()
        choice = int(input('Выберите пункт: '))
        if choice == 0:
            View.printPhoneBook("Телефонный справочник", Model.phonebook)
        elif choice == 1:
            open_file()
            print('\nФайл открыт!')
            View.printPhoneBook("Телефонный справочник", Model.phonebook)
        elif choice == 2:
            save_file()
            print('\nФайл сохранен!')
        elif choice == 3:
            Model.add_contact()
        elif choice == 4:
            Model.change_contact()           
        elif choice == 5:
            Model.remove_contact()
        elif choice == 6:
            Model.find_contact()
        elif choice == 7:
            save_backup()
            print('\nРезервная копия сохранена!')
        elif choice == 8:
            save_backup()
            print('\nФайл восстановлен с резервной копии!')
        elif choice == 9:
            break
        else:
            print('\nНеправильно набран номер!')

def start():
    open_file()
    main_menu()

def open_file():
    with open(Model.path, "r", encoding="UTF-8") as data:
        contacts_list = data.read().split("\n")
        Model.phonebook = contacts_list

def save_file():
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(('\n'.join(Model.phonebook)))

def save_backup():
    with open(Model.path, "r", encoding="UTF-8") as source:
        backup = source.read()
    with open(Model.path_backup, "w", encoding="UTF-8") as data:
        data.write(backup)

def restore_from_backup():
    with open(Model.path_backup, "r", encoding="UTF-8") as source:
        backup = source.read()
    with open(Model.path, "w", encoding="UTF-8") as data:
        data.write(backup)

def try_enter_int(enter_text):
    while True:
        text = input(f'{enter_text}')
        try:
            return int(text)
        except:
            print ('\nНеправильно набран номер')
        
