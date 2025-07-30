from pathlib import Path

path = Path("ch10/learning_python.txt")
contents = path.read_text()
print(contents)

print("\nLooping over the lines")
lines = contents.splitlines()
for line in lines:
    print(line)
