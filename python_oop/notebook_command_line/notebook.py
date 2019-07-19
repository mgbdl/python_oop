import datetime

# Store the next available id for all notes
last_id = 0

class Note:
    '''Represent a note in the notebook. Match against a
    string in searches and store tags for each note.'''

    def __init__(self, memo, tag=''):
        '''initialize a note with memo and optioan
        space-separated tags. Automatically set the note's
        creation date and a unique id.'''
        self.memo = memo
        self.tag = tag
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''Determine if this note matches the filter
        text. Return True if it matches, False otherwise.

        Search is case sensitibe and matches both text and tags.'''
        return filter in self.memo or filter in self.tag

# TESTING
# n1 = Note('Hello first')
# n2 = Note('Hello again')
# print(n1.id)
# print(n2.id)
# print(n1.match('first'))
# print(n1.match('again'))

class Notebook:
    '''Represent a collection of notes that can be tagged,
    modified, and searched.'''

    def __init__(self):
        '''Initialize a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
            return Note

    def modify_memo(self, note_id, memo):
        '''Find the note with the given id and change its
        memo to the given value.'''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        '''Find the note with the given id and change its
        tags to the given value.'''
        note = self._find_note(note_id)
        if note:
            note.tag = tags
            return True
        return False


    # def modify_memo(self, note_id, memo):
    #     '''Find the note with the given id and change its
    #     memo to the given value'''
    #     for note in self.notes:
    #         if note.id == note_id:
    #             note.memo = memo
    #             break
    #
    # def modify_tags(self, note_id, tags):
    #     '''Find the note with the given id and change its
    #     tags to the give value'''
    #     for note in self.notes:
    #         if note.id == note_id:
    #             note.tag = tags
    #             break

    def seach(self, filter):
        '''Find all notes that match the given filter
        string'''
        return [note for note in self.notes if note.match(filter)]

# TESTIN
# n = Notebook()
# n.new_note('hello world')
# n.new_note('hello again')
# print(n.notes)
# print(n.notes[0].id)
# print(n.notes[1].id)
# print(n.notes[1].memo)
# print(n.seach('hello'))
# print(n.seach('world'))
# n.modify_memo(1, 'hi world')
# print(n.notes[0].memo)
