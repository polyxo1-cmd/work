import os

def compare_directories():
    dir1 = input("첫 번째 하위 디렉토리 이름: ")
    dir2 = input("두 번째 하위 디렉토리 이름: ")

    files1 = {}
    files2 = {}

    for entry in os.scandir(dir1):
        if entry.is_file():
            files1[entry.name] = entry

    for entry in os.scandir(dir2):
        if entry.is_file():
            files2[entry.name] = entry

    if len(files1) != len(files2):
        print("파일 개수가 다릅니다.")
        return

    if set(files1.keys()) != set(files2.keys()):
        print("파일 이름이 다릅니다.")
        return

    for name in files1:
        file1 = files1[name]
        file2 = files2[name]

        if file1.stat().st_size != file2.stat().st_size:
            print(name, "파일 크기가 다릅니다.")
            return

        f1 = open(file1.path, "r", encoding="utf-8")
        f2 = open(file2.path, "r", encoding="utf-8")

        content1 = f1.read()
        content2 = f2.read()

        f1.close()
        f2.close()

        if content1 != content2:
            print(name, "파일 내용이 다릅니다.")
            return

    print("두 디렉토리의 파일들이 모두 같습니다.")

compare_directories()
