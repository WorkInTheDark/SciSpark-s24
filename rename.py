import os

def rename_files_in_folder(folder_path):
    try:
        files = os.listdir(folder_path)
        files.sort(reverse=True)  # 确保文件按顺序排列

        for index, filename in enumerate(files):
            # 获取文件扩展名
            file_ext = os.path.splitext(filename)[1]
            if filename == '.DS_Store':
                continue
            # 构建新的文件名
            # if filename[2] == 's':
            #     id = int(filename[1])   
            #     new_filename = f"p{id+2}_{filename[2:]}"
            # if filename[3] == 's':
            #     id = int(filename[1] + filename[2])
            #     new_filename = f"p{id+2}_{filename[3:]}"
            # 获取文件的完整路径
            new_filename = filename.split('_')[0] + filename.split('_')[1]
            old_file = os.path.join(folder_path, filename)
            new_file = os.path.join(folder_path, new_filename)
            # 重命名文件
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_filename}'")

    except Exception as e:
        print(f"An error occurred: {e}")

# 使用示例
folder_path = "./static/files/books/Amara and the Bats/audio/"  # 替换为你的文件夹路径
rename_files_in_folder(folder_path)