def execute_code(code):
    exec_globals = {}
    exec_locals = {}
    try:
        exec(code, exec_globals, exec_locals)
    except Exception as e:
        return str(e)
    return exec_locals
