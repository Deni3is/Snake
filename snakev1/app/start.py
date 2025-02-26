from app.snake.snake import Snake 



class Menu:
    def __init__(self):
        self.score = 0
        self.options = ["This is snake", "Start", "Score", "Exit"]
    
    def display_menu(self):
        print("Please choose an option:")
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

    def activate(self):
        while True:
            self.display_menu()
            choice = input("Enter the number of your choice: ")
            if choice.isdigit():
                choice_index = int(choice) - 1
                if 0 <= choice_index < len(self.options):
                    self.handle_choice(choice_index)
                else:
                    print("Invalid choice, please try again.")
            else:
                print("Invalid input, please enter a number.")

    def handle_choice(self, choice_index):
        if choice_index == 0:
            print("You selected: This is snake")
        elif choice_index == 1:
            print("Starting the game...")
        elif choice_index == 2:
            print("Showing score...")
        elif choice_index == 3:
            print("Exiting the program...")
            exit()  # Завершает выполнение программы
        else:
            print("Invalid option!")


