TOKEN_REGEX = {
    "int": r'^\d+$',
    "float": r'^\d+\.\d*?$',
    "string": r'^({})$'.format("('.*'|" + '".*")'),
    "image_path": r'',
    "video_path": r'',
    "pdf_path": r'',
    "python_variable_name": r'',
    "python_class_name": r'',
    "python_function_name": r''
}

PYTHON_CODE_INDENT = ' ' * 4

def gen_blocked_code(prefix, condition, code_block):
    """
    For example, gen_blocked_code('if', '(True)', 'pass') produces
    if (True):
        pass
    """
    header_line = '{}{}:'.format(prefix, condition)
    new_code_block = '\n'.join([PYTHON_CODE_INDENT + line for line in code_block.split('\n')])
    return header_line + '\n' + new_code_block


def gen_if_elif_block_code(conditions, code_blocks):
    # example: gen_if_elif_block_code(['foo is None', 'foo in bar'], ['assert foo is None', 'pass'])
    if len(conditions) != len(code_blocks):
        raise ValueError('Lengths are not equal:\n{}\n{}'.format(conditions, code_blocks))
    if_blocks = []
    for i in range(len(conditions)):
        condition = conditions[i]
        code_block = code_blocks[i]
        if i == 0:
            prefix = 'if '
        else:
            prefix = 'elif '
        if_blocks.append(gen_blocked_code(prefix, condition, code_block))
    return '\n'.join(if_blocks)
    
    
def gen_switch_code(var_name, var_values, code_blocks):
    # example: gen_switch_code('animal', ['"dog"', '"cat"'], ['pass', 'pass'])
    conditions = ['{} == {}'.format(var_name, var_value) for var_value in var_values]
    return gen_if_elif_block_code(conditions, code_blocks)
    
def gen_fn_code(fn_name, arg_str, code_block):
    # example: gen_fn_code('foo', 'arg1, arg2, **kwargs', 'pass')
    return gen_blocked_code('def {}({})'.format(fn_name, arg_str), '', code_block)
    
def gen_if_main_code(code_block):
    # example: gen_if_main_code('pass')
    return gen_blocked_code('if ', '__name__ == "__main__"', code_block)