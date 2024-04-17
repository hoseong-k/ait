import os
import shutil

def fileList(path_before):
    """
    주어진 디렉터리에서 모든 파일을 읽고, 파일명의 마지막 단어를 분류 기준으로 사용하여
    중복 없는 카테고리 리스트를 생성하여 반환합니다.
    """
    file_list = os.listdir(path_before)
    category = set()  # 직접 set을 사용하여 중복을 피함
    for file in file_list:
        category_name = file.split(" ")[-1]  # 파일명을 공백으로 나누고 마지막 부분을 사용
        category.add(category_name)
    return list(category)

def makeFolder(path_after, file_list):
    """
    파일 분류별로 폴더를 생성합니다. 이미 폴더가 존재하면 생성을 시도하지 않습니다.
    """
    for file in file_list:
        directory = os.path.join(path_after, file)
        if not os.path.exists(directory):
            os.makedirs(directory)

def moveFile(path_before, path_after):
    """
    주어진 원본 경로에서 대상 경로로 파일을 해당 카테고리에 맞게 이동시킵니다.
    대상 경로에 동일한 파일이 존재할 경우 파일을 이동하지 않고 메시지를 출력합니다.
    """
    filelist = os.listdir(path_before)
    moved_count = 0
    skipped_count = 0
    total_files = len(filelist)

    for file in filelist:
        category_name = file.split(" ")[-1]
        target_path = os.path.join(path_after, category_name, file)

        if os.path.exists(target_path):
            print(f"Skipping {file}: Target file already exists.")
            skipped_count += 1
        else:
            shutil.move(os.path.join(path_before, file), target_path)
            moved_count += 1
            print(f"Moved {file} to {target_path}")
    
    print(f"\nSummary: Total files: {total_files}, Moved: {moved_count}, Skipped: {skipped_count}")

if __name__ == "__main__":
    path_before = r"I:\Baidu\# Candidate"
    file_list = fileList(path_before)

    path_after = r"I:\Baidu\# Actor"
    makeFolder(path_after, file_list)
    moveFile(path_before, path_after)
