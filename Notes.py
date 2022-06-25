from collections import UserDict


class Name:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Tag:
    def __init__(self, tags):
        self.tags = tags

    def __repr__(self):
        return str(self.tags)


class Notes:
    def __init__(self, name: Name, data: str, tag: Tag = None):
        self.name = name
        self.data = data
        self.tags = []
        if tag:
            self.tags.append(tag)

    def __repr__(self):
        if self.tags == []:
            return f'{self.name}, {self.data}'
        return f'{self.name}, {self.data}, Tags: {self.tags}'


class NoteBook(UserDict):
    def add_to_notebook(self, note: Notes):
        self.data[note.name.value] = note


def ex(*args):
    return 'Bye!'


def cmd_error(*args):
    return 'I can`t help you'


COMMANDS = {ex: ['exit', '.']}


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")
    return cmd_error, ['']


def main():
    our_notes = NoteBook()
    # тут просто пока наполняю записную книгу чтоб что-то было
    name_n1 = Name('First note')
    name_n2 = Name('Second note')
    name_n3 = Name('Third note')
    name_n4 = Name('Bandera smuzi')
    tag_1 = Tag('opportunity')
    tag_2 = Tag('cooking')
    note_1 = Notes(name_n1, 'Huge opportunity', tag_1)
    note_2 = Notes(name_n2, 'second step')
    note_3 = Notes(name_n3, '3 eggs, one tomato', tag_2)
    note_4 = Notes(name_n4,'в бутылку до половины объема насыпаются кусочки пенопласта; заливается 1/3 оставшегося объема '
                           'отработанного машинного масла, 2/3 – бензина; но сверху должно оставаться немного места для '
                           'испарения; бутылка плотно закрывается пробкой; на горлышко привязывается фитиль; '
                           'Бандера-смузи готов', tag_2)
    our_notes.add_to_notebook(note_1)
    our_notes.add_to_notebook(note_2)
    our_notes.add_to_notebook(note_3)
    our_notes.add_to_notebook(note_4)

    print(our_notes)
    while True:
        our_command = input("And your command is...> ")
        result, data = parse_command(our_command)
        print(result(our_notes, *data))
        if result is ex:
            break


if '__main__' == __name__:
    main()
