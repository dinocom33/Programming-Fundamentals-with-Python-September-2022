def find_file(text):
    if "." in text:
        file_name, extension = text.split(".")
        print(f"File name: {file_name}")
        print(f"File extension: {extension}")


file_path = input().split("\\")

for word in file_path:
    find_file(word)
