import sys
import io
from foo_bar import fooBar
import unittest

class TestFooBar(unittest.TestCase):
    def test_foo(self):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        fooBar(3)
        terminal_output =  sys.stdout.getvalue()
        assert  'Foo' in terminal_output, "Output must be 'Foo' for number 3"
        sys.stdout.truncate(0);
        fooBar(13)
        terminal_output = sys.stdout.getvalue()
        assert  'Foo' in terminal_output, "Output must be 'Foo' for number 13"
        sys.stdout = stdout
        print("TestCase 'test_foo' passed!")


    def test_bar(self):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        fooBar(10)
        terminal_output =  sys.stdout.getvalue()
        assert  'Bar' in terminal_output, "Output must be 'Bar' for number 10"
        sys.stdout.truncate(0);
        fooBar(52)
        terminal_output = sys.stdout.getvalue()
        assert  'Bar' in terminal_output, "Output must be 'Bar' for number 52"
        sys.stdout = stdout
        print("TestCase 'test_bar' passed!")


    def test_qix(self):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        fooBar(14)
        terminal_output =  sys.stdout.getvalue()
        assert  'Qix' in terminal_output, "Output must be 'Qix' for number 14"
        sys.stdout.truncate(0);
        fooBar(17)
        terminal_output = sys.stdout.getvalue()
        assert  'Qix' in terminal_output, "Output must be 'Qix' for number 17"
        sys.stdout.truncate(0);
        fooBar(37)
        terminal_output = sys.stdout.getvalue()
        assert  'Qix'  not in  terminal_output, "Output should not be 'Qix' for 37"
        sys.stdout = stdout
        print("TestCase 'test_qix' passed!")


    def test_any_other_number(self):
        stdout = sys.stdout
        sys.stdout = io.StringIO()
        fooBar(0)
        terminal_output =  sys.stdout.getvalue()
        assert  '0' in terminal_output, "Output must be '11' for number 0"
        sys.stdout.truncate(0);
        fooBar(19)
        terminal_output = sys.stdout.getvalue()
        assert  '19' in terminal_output, "Output must be 'Qix' for number 19"
        sys.stdout = stdout
        print("TestCase 'test_qix' passed!")
        
if __name__ == '__main__':
    unittest.main()