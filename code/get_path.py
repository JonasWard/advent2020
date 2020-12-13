import pathlib

def get_data_path():
    return str(pathlib.Path(__file__).parent.parent.absolute()) + "/data"

def get_code_path():
    return str(pathlib.Path(__file__).parent.parent.absolute()) + "/code"

