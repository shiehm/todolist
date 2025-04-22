
class Todo:
    def __init__(self, title, done=False):
        self._title = title
        self._done = done

    @property
    def title(self):
        return self._title
        
    @property
    def done(self):
        return self._done
        
    @done.setter
    def done(self, done=bool):
        self._done = done
        
    def __eq__(self, other):
        if isinstance(other, Todo):
            return self.title == other.title and self.done == other.done
        return NotImplemented
    
    def __str__(self):
        box = '[X]' if self.done else '[ ]'
        return f'{box} {self.title}'


# def test_todo():
#     todo1 = Todo('Buy milk')
#     todo2 = Todo('Clean room')
#     todo3 = Todo('Go to gym')
#     todo4 = Todo('Clean room')

#     print(todo1)                  # [ ] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [ ] Clean room

#     print(todo2 == todo4)         # True
#     print(todo1 == todo2)         # False
#     print(todo4.done)             # False

#     todo1.done = True
#     todo4.done = True
#     print(todo4.done)             # True

#     print(todo1)                  # [X] Buy milk
#     print(todo2)                  # [ ] Clean room
#     print(todo3)                  # [ ] Go to gym
#     print(todo4)                  # [X] Clean room

#     print(todo2 == todo4)         # False

#     todo4.done = False
#     print(todo4.done)             # False
#     print(todo4)                  # [ ] Clean room

# test_todo()