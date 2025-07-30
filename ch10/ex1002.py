# 10-2. Learning C:
# You can use the replace() method to replace any word in a
# string with a different word.
# replace the word Python with the name of another language, such as C

from pathlib import Path

path = Path("ch10/learning_python.txt")
contents = path.read_text()

lines = contents.splitlines()
for line in lines:
    line = line.replace("Python", "C")
    print(line)
