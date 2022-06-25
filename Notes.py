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


our_notes = NoteBook()

name_n1 = Name('First note')
name_n2 = Name('Second note')

tag_1 = Tag('opportunity')

note_1 = Notes(name_n1, 'Huge opportunity', tag_1)
note_2 = Notes(name_n2, 'second step')

print(note_1)
print(note_2)
our_notes.add_to_notebook(note_1)
our_notes.add_to_notebook(note_2)

print(our_notes)