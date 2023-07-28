import io
import os


cache_index_file = '../../cache/index.txt'

def absoluteFilePath(relativePath):
    script_dir = os.path.dirname(__file__)
    abs_file_path = os.path.join(script_dir, relativePath)
    return abs_file_path

def generate_next_index():
    index_abs_file_path = absoluteFilePath(cache_index_file)
    f = open(index_abs_file_path, "r")
    index_text = f.read()
    next_index = int(index_text) + 1
    f = open(absoluteFilePath(cache_index_file), "w")
    f.write(str(next_index))
    f.close()
    return next_index