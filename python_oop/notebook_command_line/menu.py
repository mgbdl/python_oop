import sys
from notebook import Notebook

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit
        }

    def display_menu(self):
        print("""
            Notebook Menu

            1. Show all notes
            2. Search Notes
            3. Add Note
            4. Modify Note
            5. Quit
        """)

    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(str(choice))
            if action:
                action()
            else:
                print('{0} is not valid choice'.format(choice))

    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes

        for note in notes:
            print("{0}: {1} {2}".format(
                note.id, note.tag, note.memo))

    def search_notes(self):
        filter = input("Seach for: ")
        notes = self.notebook.seach(filter)
        self.show_notes(notes)

    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note hasd been added.")

    def modify_note(self):
        id = input("Enter note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        status = False
        if memo and id:
            status = self.notebook.modify_memo(id, memo)
        if tags and id:
            status = self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == '__main__':
    Menu().run()
