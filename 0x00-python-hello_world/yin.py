import dis
def magic_calculation(a, b):
    code = """
        0 LOAD_CONST 1
        3 LOAD_FAST 0
        6 LOAD_FAST 1
        9 BINARY_POWER
        10 BINARY_ADD
        11 RETURN_VALUE
    """
    return eval(compile(code, '<string>', 'exec'))
dis.dis(magic_calculation)
