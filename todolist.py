from todo import Todo
import copy

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = []

    @property
    def title(self):
        return self._title
    
    @property
    def todos(self):
        return self._todos
    
    def validate_todo(self, other):
        if not isinstance(other, Todo):
            raise TypeError('Please pass in a Todo object.')
    
    def add(self, todo):
        self.validate_todo(todo)
        self._todos.append(todo)
    
    def __str__(self):
        output_lines = [f'----- {self.title} -----']
        output_lines += [str(todo) for todo in self.todos]
        return '\n'.join(output_lines)

    def __len__(self):
        return len(self._todos)
        
    def first(self):
        return self._todos[0]
    
    def last(self):
        return self._todos[-1]
        
    def to_list(self):
        return copy.deepcopy(self._todos)
        
    def todo_at(self, index):
        return self._todos[index]
        
    def mark_done_at(self, index):
        self._todos[index].done = True
    
    def mark_undone_at(self, index):
        self._todos[index].done = False
    
    def mark_all_done(self):
        # for todo in self._todos:
        #     todo.done = True
        def mark_done(todo):
            todo.done = True
        self.each(mark_done)
    
    def mark_all_undone(self):
        # for todo in self._todos:
        #     todo.done = False
        def mark_undone(todo):
            todo.done = False
        self.each(mark_undone)
    
    def all_done(self):
        done = [todo.done for todo in self._todos]
        return all(done)
        
    def remove_at(self, index):
        self._todos.pop(index)
    
    def each(self, callback):
        for todo in self._todos:
            callback(todo)
    
    def select(self, callback):
        new_list = TodoList(self._title)
        for todo in self._todos: 
            if callback(todo):
                new_list.add(todo)
        return new_list
        
    def find_by_title(self, string):
        for todo in self._todos:
            if todo.title == string:
                return todo
        raise IndexError('Title not found.')
    
    def done_todos(self):
        return self.select(lambda todo: todo.done)
    
    def undone_todos(self):
        return self.select(lambda todo: not todo.done)
    
    def mark_done(self, string):
        self.find_by_title(string).done = True


empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list