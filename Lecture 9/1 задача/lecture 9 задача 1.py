import os
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

if not os.path.exists(f"*.{extensions}"):
    os.mkdir(f"{extensions}")

sum_1 = 0
size = 0
for filename in os.listdir():
    if f"*.{extensions}" in filename:
        size += os.path.getsize(filename)
        os.replace(filename, f"{extensions}/{filename}")
        sum_1 += 1

print(f"{sum_1} файл/-ов перемещено в папку {extensions} общим размером - {size} кб")

# os.rename(f"data_txt/{filename_txt}", "data_txt/renamed.txt")
# print(f"Файл {filename_txt} был переименован в renamed.txt")
