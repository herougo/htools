


"""
Incomplete (with Incomplete API)
"""



OPEN_CLOSE_PAIRS = {
    "'": "'", '"': '"', '(': ')', '[': ']', '"""': '"""'
}
QUOTES = ['"', "'"]
TRIPLE_QUOTE = '"""'
class CodeCharacterIterator:
    def __init__(self, code):
        self._code = code

    def __iter__(self):
        open_stack = []
        in_string = False
        ignore = 0
        for i, character in enumerate(self._code):
            if ignore > 0:
                ignore -= 1
            elif len(open_stack) > 0 and OPEN_CLOSE_PAIRS[open_stack[-1]] == character:
                # closing
               in_string = False
               open_stack.pop(-1)
            elif len(open_stack) > 0 and open_stack[-1] == TRIPLE_QUOTE and self._code[i:i+3] == TRIPLE_QUOTE:
                # closing triple quote
                in_string = False
                open_stack.pop(-1)
            elif character in OPEN_CLOSE_PAIRS.keys():
                # opening
                if character in QUOTES:
                    in_string = True
                    if self._code[i:i+3] == TRIPLE_QUOTE:
                        ignore = 2
                open_stack.append(character)
            yield i, character, in_string
        


class CodeRepo:
    def __init__(self, path):
        self._path = path

class CodeFile:
    __delimiter    = '\n'
    def __init__(self, path, base_path=None):
        self._path = path
        self._base_path = base_path

    def get_required_import(self):
        pass

    def convert_relative_imports(self):
        pass
    
    def convert_star_imports(self):
        pass

# IDEALLY, USE PYTHON COMPILER CODE

CODE = """
import sort
from sort.bad import *
from sorting import There
import yes.good.hello

# Comment


YU = None
MODIFIED_TWICE = 1
MODIFIED_TWICE = 2
USED_BY_CLASS_1 = 1
USED_BY_CLASS_2 = 2

class Empty:
  pass

class Hi:
  def __init__(self):
    pass

class Large:
  _constant = None
  def __init__(self, asdf, **kwargs):
    do_stuff()
    self._asdf = asdf

  def adder(self, other):
    global USED_BY_CLASS_1
    USED_BY_CLASS_1 = 0

  def say_hi(self):
    return USED_BY_CLASS_2

class UnusedClass:
  def __init__(self):
    pass

def my_func():
  \"\"\"
  Multi-line comment
  \"\"\"
  not_comment = \"\"\"
  not a multi-line comment
  \"\"\"
  global YU
  YU = 2
  MODIFIED_TWICE = 3 # no effect
  return None

def func(a, b, c, *vargs, **kwargs):
  pass
  
def          unused_func(**kwargs):
  pass

if True:
  # global variables, classes, and functions
  hi = yu
  z = Empty()
  a = Hi()
  b = my_func()
  c = func(1, 4, 2, 2, 54, 5, yes="yes")
  
  # Large
  l = Large(a, no="no")
  l.adder("yes")
  l.say_hi()
  
  # import using
  a = sort.bell()
  b = yes.good.hello.hi()
  c = There()
  
  # Not defined yet
  d = ClassNotDefinedYet()
  d.function_not_defined_yet(a, b, c=c)
  e = other_function_not_defined_yet(a, b, c=c)
"""

defined_global_variables = [
    'YU', 'MODIFIED_TWICE', 'MODIFIED_TWICE', 'USED_BY_CLASS_1', 'USED_BY_CLASS_2']
defined_classes = ['Large', 'Hi', 'Empty', 'UnusedClass']
defined_class_functions = ['Large.adder', 'Large.say_hi']
defined_functions = ['my_func', 'func', 'unused_func']
import_statements = [
    'import sort', 'from sort.bad import *', 'from sorting import There', 'import yes.good.hello'
]

used_global_variables = defined_global_variables
used_classes = ['Large', 'Hi', 'Empty']
used_functions = ['my_func', 'func']
used_imported_variables = [, 
    'yes.good.hello.hi', 'sort.bell', 'There', 'ClassNotDefinedYet', 
    'ClassNotDefinedYet.function_not_defined_yet', 'other_function_not_defined_yet'
]


def parser_example():
    import parser
    import parser

    code = Code
    e = parser.suite(code)
    f = e.compile()
    f.co_varnames
    f.co_freevars
    f.co_consts
    f.co_cellvars
    f.co_names
    f.co_name

def get_parse_tree(file_path):
    import parser
    # keywords: parse tree, compile
    

def extract_definitions(python_path, base_repo_path):
    # get name, import statement, code location
    return {
        'global_variable_definitions': None,
        'class_definitions': None,
        'function_definitions': None
    }

def extract_uses(python_path):
    return {
        'global_variable_uses': None,
        'class_uses': None,
        'function_uses': None
    }

def get_import_statement(name, repo_path):
    pass


import ast
import astor
from pprint import pprint
import parser


''' To Do
AST
- (Editing)
- (Local Search)
r'FAIL:\w+{1} \({2}\)'
- 2nd line number
- globals
 - handle "global" keyword and globals dict too
- sublime tool
'''


''' IDEAS
expand parser parse tree by whitespace or comments
- assume all non whitespace or comment text is present in the parse tree in order
current approach: use AST for line numbers
- then move code at the string/line level
structure python file by imports, globals, fns and classes, if __name__ == '__main__'
when considering a class defn code block, consider comments and whitespace stuff around it to expand

gazeteers by folder and builders
(gazeteers > normal_imports > built-in.txt, github.txt)
Save name lists as Json files
- Name to path in repo
- Path in repo to name

'''




def main():
   hi = "/Users/hromel/tem.py"
   with open('/Users/hromel/PycharmProjects/playground/hi/hi2/hello.py', "r") as source:
       tree = ast.parse(source.read())
       parse_tree = parser.suite(source.read())
   print(astor.to_source(tree))
   print(type(tree))

   analyzer = Analyzer()
   analyzer.visit(tree)
   analyzer.report()

def code_to_parse_tree(code):
   pass

def parse_tree_to_code(parse_tree):
   pass


class Analyzer(ast.NodeVisitor):
   def __init__(self):
       self.stats = {"import": [], "from": []}

   def visit_Import(self, node):
       for alias in node.names:
           self.stats["import"].append(alias.name)

       self.generic_visit(node)

   def visit_ImportFrom(self, node):
       # print('visit_ImportFrom', node.__dict__)
       for alias in node.names:
           self.stats["from"].append(alias.name)
       self.generic_visit(node)

   def visit_ClassDef(self, node):
       # print('visit_Class', node.__dict__)
       node.name
       pass

   def visit_FunctionDef(self, node):
       node.name
       print('Function', node.name)
       self.generic_visit(node)

   def visit_ImportFrom(self, node):
       lineno = node.lineno
       _from = node.module
       node.names[0].name
       pass

   def visit_Import(self, node):
       lineno = node.lineno # starts at 1
       node.names[0].name
       pass

   def visit_Name(self, node):
       print('name', node.id, node.lineno)
       pass

   def visit_Assign(self, node):
       return
       print('--------------------')
       print('visit_assign', node)
       print('  visit_assign', node.__dict__)
       print('  ', node.targets[0].__dict__)
       print('  ', node.value.__dict__)
       self.generic_visit(node)

   def report(self):
       pprint(self.stats)


if __name__ == "__main__":
   main()

print('hello')



import os
class CodeRepo:
   def __init__(self, folder_path):
       self._folder_path = folder_path
       file_paths = self._get_python_file_paths()
       self._code_files = [CodeFile(file_path) for file_path in file_paths]

   def _get_python_file_paths(self):
       result = []
       for paths, subdirs, files in os.walk(self._folder_path):
           for file in files:
               if file.endswith('.py'):
                   pure_path = os.path.join(paths, file)
                   result.append(pure_path)
       return result

   def move_function_definition(self, source_file_path, dest_file_path, function_name):
       pass

   def move_class_definition(self, source_file_path, dest_file_path, class_name):
       # also handle dependencies
       pass

   # ???? have e.g. transform_relative_imports passed to each CodeFile


class CodeFile:
   def __init__(self, file_path, update_imports=True):
       '''
       :param file_path: str .py file file path
       :param update_imports: bool automatically update update imports when updating code
       '''
       self._update_imports = update_imports
       self._file_path = file_path
       with open(file_path, 'r') as source:
           self._source_lines = source.read().split('\n')
       # ?? load ast, extract values, unload ast


   ''' Know how '''
   def _load_imports(self):
       # dict mapping line number to line
       pass

   def get_globally_defined_class_names(self):
       pass

   def get_globally_defined_function_names(self):
       pass

   def get_globally_defined_class_names_with_methods(self):
       pass

   def transform_relative_imports(self, package=None):
       # (assume getting variable uses is already done)
       pass

   ''' (Modifying Code) '''
   def add_function(self, node):
       pass

   def remove_function(self, function_name):
       # ????
       return node

   def add_class_definition(self, node):
       pass

   def remove_class_definition(self, class_name):
       # ????
       return node

   ''' To Do '''
   def _set_flags_recursively(self):
       # ??
       pass

   def get_calls_to_particular_function(self, function_name):
       pass

   def get_calls_to_particular_class_function(self, class_function_name):
       pass

   def get_uses_of_global_variables(self):
       # includes classes, functions, etc
       # be careful of local variables with the same name
       # be aware of what's locally defined and what isn't
       pass

   def set_global_variable(self, var_name, value):
       pass

   def get_defined_global_variables(self):
       pass

   def add_missing_imports(self):
       pass

   def replace_function_with_its_logic(self):
       pass

   def save(self):
       pass


class ParseTreeWrapper:
   def __init__(self):
       pass

   def get_func_defs(self):
       # list of node, name, start_pos, end_pos
       pass

   def get_class_defs(self):
       # list of node, name, start_pos, end_pos
       pass

   def get_global_defs(self):
       # list of node, name, start_pos, end_pos
       pass

   def get_imports(self):
       # list of node, name, start_pos, end_pos
       pass


