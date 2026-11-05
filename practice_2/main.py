def files_per_folder(files, folders):
    if folders == 0:
        return "На ноль делить нельзя"
    return files / folders

assert files_per_folder(48, 6) == 8.0
assert files_per_folder(10, 0) == "На ноль делить нельзя"
assert files_per_folder(9, 3) == 3.0

words = ["лук", "морковь", "картофель"]
by_length = sorted(words, key=lambda word: len(word))
print(by_length)