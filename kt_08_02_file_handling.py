# =====================  File handling =====================
import os

get_cwd = os.getcwd()
# 1.1 1st run will raise the below Exception, so create a new file using "w"
"""
FileNotFoundError: [Errno 2] No such file or directory:
  'C:\\Users\\muthukus\\Documents\\Python_scripts\\Python_KT\\Log\\example.txt'
"""

# 1.2 Opening a file in read mode
file = open(rf"{get_cwd}\Log\example.txt", "r")
print(file.read())
file.close()

# 1.3 Opening a file in write mode
file1 = open(rf"{get_cwd}\Log\example.txt", "w")
file1.write('Python is a high-level, interpreted, interactive and object-oriented scripting language.\n')
file1.close()

# 1.4 Opening a file in append mode
file2 = open(rf"{get_cwd}\Log\example.txt", "a")
file2.write('Python is designed to be highly readable.\n')
file2.close()

# 1.5 Opening a file in binary read mode
file3 = open(rf"{get_cwd}\Log\example.txt", "ab")
file3.write(b'It uses English keywords frequently where as other languages use punctuation,\n'
            b'and it has fewer syntactical constructions than other languages.')  # io.UnsupportedOperation: write
file3.write(b'\nEnd of the file\n')
print("Name of the file: ", file3.name)
print("Closed or not: ", file3.closed)
print("Opening mode: ", file3.mode)
file3.close()
print("Closed or not:2 ", file3.closed)

# 2. Reading a File in Python
"""
read() − Reads the entire file.
readline() − Reads one line at a time.
readlines() − Reads all lines into a list.
"""

# 2.1 read()
with open(rf"{get_cwd}\Log\example.txt", "r") as file:
    content = file.read()
    print('From read(): ', content)

# 2.2 readline()
with open(rf"{get_cwd}\Log\example.txt", "r") as file:
    line = file.readline()
    print('From readline(): ', line)

# 2.3 readlines()
with open(rf"{get_cwd}\Log\example.txt", "r") as file:
    lines_list = file.readlines()
    print('From readlines(): ', lines_list)
for i in lines_list:
    print(f"Each line from For Loop: {i}")

# 2.4 read() with seek
with open(rf"{get_cwd}\Log\example.txt", "r") as file:
    file.seek(30, 0)
    content = file.read()
    print('From read(): ', content)

# 3. Python Rename and Remove File
import os
import time
import shutil

source_file = rf"{get_cwd}\Log\example.txt"
dst_file = rf"{get_cwd}\Log\example_1.txt"
print("Before copying file: {}".format(os.listdir(os.getcwd())))
print("Adding 5 sec sleep time before Copy")
time.sleep(5)
dest = shutil.copyfile(source_file, dst_file)
list_of_files = os.listdir(rf"{get_cwd}\Log")
print("After copying file: {}".format(list_of_files))
print("Adding 5 sec sleep time after Copy")
time.sleep(5)

# 3.1 Validate the file copy status
file_copy_sts = False
for each_file in list_of_files:
    if os.path.basename(dst_file) == each_file:
        print("For loop==> Successfully copied the file '{}' from this source file '{}'".format(dst_file,
                                                                                                source_file))
        file_copy_sts = True

if file_copy_sts is False:
    print("Failed to copy file!")

# 3.2 Alternative way to check file copy status
if os.path.basename(dst_file) in list_of_files:
    print("Alt if cond==> Successfully copied the file '{}' from this source file '{}'".format(dst_file,
                                                                                               source_file))
else:
    print("Failed to copy file!")

# 3.3 Rename the file
# Current file name
current_name = rf"{get_cwd}\Log\example_1.txt"
# New file name
new_name = rf"{get_cwd}\Log\rename_file.txt"

list_of_files = os.listdir(rf"{get_cwd}\Log")
print("Before renaming file: {}".format(list_of_files))
print("Adding 5 sec sleep time before Rename")
time.sleep(5)
# Rename here
os.rename(current_name, new_name)
print(f"File '{current_name}' renamed to '{new_name}' successfully.")
list_of_files = os.listdir(rf"{get_cwd}\Log")
print("After renaming file: {}".format(list_of_files))
print("Adding 10 sec sleep time after Rename")
time.sleep(10)

# 3.3.1 Clean-up rename to original file
os.rename(new_name, current_name)

# 3.4 Remove/Delete the File
# Delete filename
file_to_delete = rf"{get_cwd}\Log\example_1.txt"
# Remove/Delete here
os.remove(file_to_delete)
print(f"File '{file_to_delete}' deleted successfully.")
list_of_files = os.listdir(rf"{get_cwd}\Log")
print("After Deletion files: {}".format(list_of_files))

# 4. Directories in Python
# Checking if a Directory Exists
"""
os.path.exists()

Relative path − A path relative to the current working directory.
Absolute path − A complete path starting from the root directory.
# https://stackoverflow.com/questions/13819496/what-is-the-difference-between-makedirs-and-mkdir-of-os
"""
import os
import time

# 4.1 Python os.path.exists
directory_path = os.getcwd()
if os.path.exists(directory_path):
    print(f"The directory '{directory_path}' exists.")
else:
    print(f"The directory '{directory_path}' does not exist.")

# 4.2 Python makedirs and mkdir
new_directory = "make_new_dir"
nested_new_directory = r"make_new_dir\dir_a\dir_b"
try:
    os.makedirs(nested_new_directory, exist_ok=True)
    print(f"makedirs ==> Directory '{nested_new_directory}' created successfully.")
except OSError as e:
    print(f"makedirs ==> Error: Failed to create directory '{nested_new_directory}'. {e}")

try:
    os.mkdir(new_directory)
    print(f"mkdir ==> Directory '{new_directory}' created successfully.")
except OSError as e:
    print(f"mkdir ==> Error: Failed to create directory '{new_directory}'. {e}")
print("Adding sleep time 5 sec Before changing the Dir")
time.sleep(5)

# 4.3 Python chdir
cwd = os.getcwd()
print(f"Current working directory before change: {cwd}")
change_new_directory = r"%s" % cwd + '\\' + 'make_new_dir\\dir_a\\dir_b'
try:
    print(f"Before==> Current working directory before change: {cwd}")
    os.chdir(change_new_directory)
    print(f"Current working directory changed to '{change_new_directory}'.")
    cwd_after = os.getcwd()
    print(f"After==> Current working directory after change: {cwd_after}")
except OSError as e:
    print(f"Error: Failed to change working directory to '{change_new_directory}'. {e}")

# 4.4 Removing a Directory
"""
os.rmdir(directory_path)
# or
shutil.rmtree(directory_path)
"""

# 4.5 Clean up for previous logic
os.chdir(cwd)
directory_path = change_new_directory
print("Adding sleep 5 sec Before removing the Dir")
time.sleep(5)

try:
    os.rmdir(directory_path)
    print(f"Directory '{directory_path}' successfully removed.")
except OSError as e:
    print(f"Error: Failed to remove directory '{directory_path}'. {e}")
else:
    list_of_files = os.listdir(rf"{new_directory}")
    print("After rmdir: {}".format(list_of_files))

# Open a file
fo = open(rf"{get_cwd}\Log\example.txt", "r")
print("Name of the file: ", fo.name)
file_contents = fo.read()

# Return the file descriptor
fid = fo.fileno()
# Display the file descriptor
print(f"FID: {fid}")
fo.flush()
print("Contents of the file: ", file_contents)
# Close opened file
fo.close()

# 5. Python OS.Popen
# 5.1 Using popen() to execute the 'ls' command(Linux), 'dir' Windows
fileStream = os.popen("dir")
res = fileStream.read()
print(res)

# 5.2 Open a file
fd = os.open(rf"{get_cwd}\Log\example.txt", os.O_RDWR)

# 5.3 getting file size
f_size = os.path.getsize(rf"{get_cwd}\Log\example.txt")

# 5.4 Reading text
ret = os.read(fd, f_size)
print(f"Reading text from file: {f_size}, {ret}")

# 5.5 Close opened file
os.close(fd)
print("file closed successfully!!")

# 6. OS.Walk
for root, dirs, files in os.walk(".", topdown=True):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
"""
topdown=False
.\Log\array_file.txt
.\Log\example.txt
.\Log\img.jpg
.\MakePackage\build\lib\mypackage\areafunctions.py
.\MakePackage\build\lib\mypackage\mathsfunctions.py
.\MakePackage\build\lib\mypackage\__init__.py
.\MakePackage\build\lib\mypackage
.\MakePackage\build\bdist.win-amd64
.\MakePackage\build\lib
.\MakePackage\dist\mypackage-1.0-py3.10.egg
.\MakePackage\mypackage\__pycache__\areafunctions.cpython-310.pyc
.\MakePackage\mypackage\__pycache__\mathsfunctions.cpython-310.pyc
.\MakePackage\mypackage\__pycache__\__init__.cpython-310.pyc
.\MakePackage\mypackage\areafunctions.py
.\MakePackage\mypackage\mathsfunctions.py
.\MakePackage\mypackage\__init__.py
.\MakePackage\mypackage\__pycache__
.\MakePackage\mypackage.egg-info\dependency_links.txt
.\MakePackage\mypackage.egg-info\PKG-INFO
.\MakePackage\mypackage.egg-info\SOURCES.txt
.\MakePackage\mypackage.egg-info\top_level.txt
.\MakePackage\run_script.py
.\MakePackage\setup.py
.\MakePackage\build
.\MakePackage\dist
.\MakePackage\mypackage
.\MakePackage\mypackage.egg-info
.\make_new_dir\dir_a
.\kt_01_basics_operators.py
.\kt_02_function.py
.\kt_03_01_module.py
.\kt_03_02_execute_module.py
.\kt_04_regex.py
.\kt_05_scope.py
.\kt_06_str_methods.py
.\kt_07_set_dict.py
.\kt_08_01_array_and_array_with_file_handling.py
.\kt_08_02_file_handling.py
.\kt_09_error_and_exception.py
.\kt_10_ssh.py
.\kt_11_oops_01_basics.py
.\kt_11_oops_02_access_modifiers.py
.\kt_11_oops_03_inheritance.py
.\kt_11_oops_04_polymorphism.py
.\kt_11_oops_05_abstraction.py
.\kt_11_oops_06_anonymous_cls_and_decorator.py
.\kt_11_oops_07_enums.py
.\kt_12_01_socket_server.py
.\kt_12_02_socket_client.py
.\kt_13_url_processing.py
.\kt_14_argparse.py
.\kt_15_debug.py
.\Log
.\MakePackage
.\make_new_dir

topdown=True
.\kt_01_basics_operators.py
.\kt_02_function.py
.\kt_03_01_module.py
.\kt_03_02_execute_module.py
.\kt_04_regex.py
.\kt_05_scope.py
.\kt_06_str_methods.py
.\kt_07_set_dict.py
.\kt_08_01_array_and_array_with_file_handling.py
.\kt_08_02_file_handling.py
.\kt_09_error_and_exception.py
.\kt_10_ssh.py
.\kt_11_oops_01_basics.py
.\kt_11_oops_02_access_modifiers.py
.\kt_11_oops_03_inheritance.py
.\kt_11_oops_04_polymorphism.py
.\kt_11_oops_05_abstraction.py
.\kt_11_oops_06_anonymous_cls_and_decorator.py
.\kt_11_oops_07_enums.py
.\kt_12_01_socket_server.py
.\kt_12_02_socket_client.py
.\kt_13_url_processing.py
.\kt_14_argparse.py
.\kt_15_debug.py
.\Log
.\MakePackage
.\make_new_dir
.\Log\array_file.txt
.\Log\example.txt
.\Log\img.jpg
.\MakePackage\run_script.py
.\MakePackage\setup.py
.\MakePackage\build
.\MakePackage\dist
.\MakePackage\mypackage
.\MakePackage\mypackage.egg-info
.\MakePackage\build\bdist.win-amd64
.\MakePackage\build\lib
.\MakePackage\build\lib\mypackage
.\MakePackage\build\lib\mypackage\areafunctions.py
.\MakePackage\build\lib\mypackage\mathsfunctions.py
.\MakePackage\build\lib\mypackage\__init__.py
.\MakePackage\dist\mypackage-1.0-py3.10.egg
.\MakePackage\mypackage\areafunctions.py
.\MakePackage\mypackage\mathsfunctions.py
.\MakePackage\mypackage\__init__.py
.\MakePackage\mypackage\__pycache__
.\MakePackage\mypackage\__pycache__\areafunctions.cpython-310.pyc
.\MakePackage\mypackage\__pycache__\mathsfunctions.cpython-310.pyc
.\MakePackage\mypackage\__pycache__\__init__.cpython-310.pyc
.\MakePackage\mypackage.egg-info\dependency_links.txt
.\MakePackage\mypackage.egg-info\PKG-INFO
.\MakePackage\mypackage.egg-info\SOURCES.txt
.\MakePackage\mypackage.egg-info\top_level.txt
.\make_new_dir\dir_a
"""
