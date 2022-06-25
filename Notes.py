from collections import UserDict


class Name:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return str(self.value)


class Tag:
    def __init__(self, *args):
        self.tags = []
        if len(args) == 0:
            self.tags.append(args[0])
        else:
            for tags in args:
                self.tags.append(tags)

    def __repr__(self):
        return str(self.tags)


class Notes:
    def __init__(self, name: Name, data: str, tags: Tag = None):
        self.name = name
        self.data = data
        self.tag = tags

    def __repr__(self):
        if self.tag is None:
            return f'{self.name}: {self.data}'
        else:
            return f'{self.name}: {self.data}, Tags: {self.tag}'


class NoteBook(UserDict):
    def add_to_notebook(self, note: Notes):
        self.data[note.name.value] = note


def input_error(in_func):
    def wrapper(*args):
        try:
            check = in_func(*args)
            return check
        except KeyError:
            return "some error cause"
    return wrapper


def ex(*args):
    return 'Bye!'


def cmd_error(*args):
    return 'I can`t help you'


@input_error
def add_to_notebook(notebook: NoteBook, *args):
    temp_name = Name(args[0])
    temp_note_txt = args[1]
    tmp_user_input = input('Do you need to add some Tags to your note? if so - type Y/y -> ')
    if tmp_user_input in ('Y', 'y'):
        tmp_tags_input = Tag((input('add Tags divided by spaces: ')))
        print(tmp_tags_input)
        # tag_1 = Tag('opportunity', 'test')
        temp_note = Notes(temp_name, temp_note_txt, tmp_tags_input)
    else:
        temp_note = Notes(temp_name, temp_note_txt)
    notebook.add_to_notebook(temp_note)
    return 'Note was added'


@input_error
def show_all(notebook: NoteBook, *args):
    for names, values in notebook.items():
        print(values)
    return 'End of the notes'


@input_error
def delete_note(notebook: NoteBook, *args):
    tmp_note = ' '.join(args)
    notebook.pop(tmp_note)
    return f'Note {tmp_note} were deleted'


@input_error
def add_tags(notebook: NoteBook, *args):
    return 'in add tags'


def change_note(notebook: NoteBook, *args):
    tmp_note = ' '.join(args)
    if tmp_note not in notebook.keys():
        return 'There is no such note'
    print(f'the note with name {tmp_note} exist and looks like --> {notebook.get(tmp_note)}')
    notebook[tmp_note] = Notes(Name(tmp_note), input('change the note: '))

    return f'Note {tmp_note} was changed'


COMMANDS = {ex: ['exit', '.'], add_to_notebook: ['add note'], show_all: ["show all"], delete_note: ['delete note'],
            change_note: ['change note']}


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
    tag_1 = Tag('opportunity', 'test')

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

    # print(our_notes)
    while True:
        our_command = input("And your command is...> ")
        result, data = parse_command(our_command)
        print(result(our_notes, *data))
        if result is ex:
            break


if '__main__' == __name__:
    main()
