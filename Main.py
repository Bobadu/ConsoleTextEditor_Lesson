class TextEditor:
    def __init__(self):
        self.document = ""
        self.undo_stack = []
        self.redo_stack = []

    def add_text(self, text):
        self.undo_stack.append(self.document)
        self.redo_stack.clear()
        self.document += text

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.document)
            self.document = self.undo_stack.pop()
        else:
            print('Brak operacji do cofnięcia.')

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.document)
            self.document = self.redo_stack.pop()
        else:
            print('Brak operacji do ponownego wykonania.')

    def display(self):
        print(self.document)

def main():
    editor = TextEditor()
    print("Komendy: 'dodaj', 'cofnij', 'ponów', 'wyświetl', 'koniec'")
    while 1:
        command = input("Wpisz komendę: ").strip()

        command = command.lower()
        if command == 'dodaj':
            text = input("Wpisz tekst: ")
            editor.add_text(text)
        elif command == 'cofnij':
            editor.undo()
        elif command == 'ponów':
            editor.redo()
        elif command == 'wyświetl':
            editor.display()
        elif command == 'koniec':
            break
        else:
            print("Nieznana komenda.")

if __name__ == '__main__':
    main()