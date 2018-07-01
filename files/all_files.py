import os

allfiles = os.walk(r"d:\education\git_workspace\python")
for (full_dir, dir_names, files) in allfiles:
    if full_dir.find(".git") >= 0:
        continue
    print("Directory: ", full_dir)
    print("============" + "=" * len(full_dir))

    for dir_name in dir_names:
        print(dir_name)

    for file in files:
        print(file)
