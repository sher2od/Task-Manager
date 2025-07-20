import sys
from utils import print_main, print_satatus, print_menu
from manager import Manager

def main() -> None:
    manager = Manager()

    while True:
        print_main()
        op = input("> ")

        if op == '1':
            if manager.login():
                while manager.user:
                    print_satatus(f"{manager.user.name} sizni accounting.")
                    print_menu()

                    choice = input(">")

                    if choice == '1':
                        manager.add_task()
                    elif choice == '2':
                        manager.view_tasks()
                    elif choice == '3':
                        pass
                    elif choice == '4':
                        pass
                    elif choice == '5':
                        manager.user = None
                    else:
                        print("xato menu")
        elif op == '2':
            manager.register()
        elif op == '3':
            sys.exit(0)
        else:
            sys.exit(1)

if __name__ == "__main__":
    main()
