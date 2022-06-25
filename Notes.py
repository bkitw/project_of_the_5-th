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
    def __init__(self, name: Name, data: str, tags: Tag = None):
        self.name = name
        self.data = data
        self.tag = []
        if tags:
            self.tag.append(tags)

    def add_tags(self, tags):
        self.tag.append(tags)

    def change_notes(self, data):
        self.data = data

    def __repr__(self):
        if len(self.tag) == 0:
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
            return "Please check your input"
    return wrapper


def ex(*args):
    return 'Bye!'


def cmd_error(*args):
    return 'I can`t help you'


@input_error
def add_to_notebook(notebook: NoteBook, *args):
    temp_name = Name(args[0])
    temp_note_txt = args[1]
    tmp_user_input = input('Do you need to add some Tag to your note? if so - type Y/y -> ')
    if tmp_user_input in ('Y', 'y'):
        tmp_tags_input = input('add Tag: ')
        temp_note = Notes(temp_name, temp_note_txt, Tag(tmp_tags_input))
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
def add_tag(notebook: NoteBook, *args):
    tmp_note = ' '.join(args)
    if tmp_note not in notebook.keys():
        return 'There is no such note'
    for k_notes, v_notes in notebook.data.items():
        if tmp_note == k_notes:
            print(f'the note with name {tmp_note} exist and looks like --> {notebook.get(tmp_note)}')
            Notes.add_tags(v_notes, Tag(input('input tag: ')))
    return f'Tag for Note {tmp_note} was added'


def change_note(notebook: NoteBook, *args):
    tmp_note = ' '.join(args)
    if tmp_note not in notebook.keys():
        return 'There is no such note'
    for k_notes, v_notes in notebook.data.items():
        if tmp_note == k_notes:
            print(f'the note with name {tmp_note} exist and looks like --> {notebook.get(tmp_note)}')
            Notes.change_notes(v_notes, input('change the note: '))
    return f'Note {tmp_note} was changed'


def info(*args):
    print('The commands are:')
    print('"add note" -> to add note, example: add note __Name__ __Note TXT__')
    print('"delete note" -> to delete note , example: delete note __Name__')
    print('"change note" -> to change note , example: change note __Name__')
    print('"add tag" -> to add tag , example: add tag __Name__')
    print('"exit or . " -> to exit')
    return 'make your choice'


COMMANDS = {ex: ['exit', '.'], add_to_notebook: ['add note'], show_all: ["show all"], delete_note: ['delete note'],
            change_note: ['change note'], add_tag: ['add tag'], info: ['info', 'help']}


def parse_command(user_input: str):
    for k, v in COMMANDS.items():
        for i in v:
            if user_input.lower().startswith(i.lower()):
                return k, user_input[len(i):].strip().split(" ")
    return cmd_error, ['']


def main():
    our_notes = NoteBook()
    print('for help with commands type info')
    # тут просто пока наполняю записную книгу чтоб что-то было
    name_n1 = Name('First note')
    name_n2 = Name('Second note')
    name_n3 = Name('Third note')
    name_n4 = Name('Bandera smuzi')
    tag_1 = Tag("Tag1")
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
