import os

relative_path = './new_folder1/test_file1.txt'
abs_path = os.path.abspath(relative_path)
normalised_p = os.path.normpath(abs_path)
print(normalised_p)

walk = os.walk('.')
for i in walk:
    print(i)

ab_path = os.path.abspath('./new_folder2')
norm_path = os.path.join(ab_path, 'test_file3.txt')
print(norm_path)
os.mkdir(os.path.join(ab_path, 'new_folder3'))

os.rmdir(os.path.join(ab_path, 'new_folder3'))
walk = os.walk('.')
for i in walk:
    print(i)

#task2 

stih = """Если б мишки были пчелами,
То они бы нипочем,
Никогда и не подумали,
Так высоко строить дом."""

def writen_file(path, content):
    with open(path, 'wt', encoding='utf-8') as file:
        file.write(content)
writen_file('./test_file2.txt', stih)

def console_stih(path):
    with open(path, 'rt', encoding='utf-8') as file:
        content = file.read()
    print(content)
console_stih('./test_file2.txt')