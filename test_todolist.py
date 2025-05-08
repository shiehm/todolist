import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_length(self):
        self.assertEqual(3, len(self.todos))
    
    def test_to_list(self):
        lst = [self.todo1, self.todo2, self.todo3]
        self.assertEqual(lst, self.todos.to_list())
    
    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())
    
    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())
    
    def test_all_done(self):
        self.assertFalse(self.todos.all_done())
    
    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            self.todos.add(123)
        with self.assertRaises(TypeError):
            self.todos.add('123')
        with self.assertRaises(TypeError):
            self.todos.add(TodoList())


if __name__ == "__main__":
    unittest.main()