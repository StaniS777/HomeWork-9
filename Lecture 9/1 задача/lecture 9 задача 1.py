import os
import glob
import platform


extensions = {
    "jpg": "images",
    "png": "images",
    "ico": "images",
    "gif": "images",
    "svg": "images",
    "exe": "programs",
    "msi": "programs",
    "pdf": "pdf",
    "xlsx": "Excel",
    "csv": "Excel",
    "rar": "arhive",
    "zip": "arhive",
    "gz": "arhive",
    "tar": "arhive",
    "docx": "word",
    "txt": "text",
    "pptx": "powerpoint",
    "ppt": "powerpoint",
    "mp3": "audio",
    "wav": "audio",
    "mp4": "video",
    "m3u8": "video",
    "webm": "video",
    "ts": "video",
    "json": "json",
    "css": "web",
    "js": "web",
    "html": "web",
    "apk": "apk",
}


def op_sys():
    return f"Operating system: {platform.system()}"


def cur_dir():
    return f"Current directory: {os.getcwd()}"


print(f"{op_sys()}\n{cur_dir()}")


def sort_files():
    path = os.getcwd()
    kol = 1
    for extension, folder_name in extensions.items():
        sum_1 = 0
        size = 0
        files = glob.glob(os.path.join(path, f"*.{extension}"))
        if len(files) != 0:
            print(f"[*] Найдено {len(files)} файлов с {extension} расширением")
            if not os.path.isdir(os.path.join(path, folder_name)) and files:
                print(f"[+] Создание папки {folder_name}")
                os.mkdir(os.path.join(path, folder_name))
                for file in files:
                    basename = os.path.basename(file)
                    dst = os.path.join(path, folder_name, basename)
                    if kol:
                        print(f"[*] перемещение  {file} в {dst}")
                    sum_1 += 1
                    size += os.path.getsize(file)
                    os.replace(file, dst)
                path_1 = os.path.join(path, folder_name)
                os.rename(f"{path_1}/{basename}", f"{path_1}/first.{extension}")
            print(f"{sum_1} файл/-ов перемещено в папку {path_1} общим размером - {size} кб")
            print(f"Файл {basename} был переименован в first.{extension}")
        else:
            continue


sort_files()
