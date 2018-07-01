import os

print("Current directory: ", os.getcwd())
files = os.listdir('..')
for file in files:
    if file.endswith(".py"):
        print(file)
