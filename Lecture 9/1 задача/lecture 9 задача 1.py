import os
import platform

print("Operating system: ", platform.system())
print("Current directory: ", os.getcwd())
if not os.path.exists("data_txt"):
    os.mkdir("data_txt")
if not os.path.exists("data_rar"):
    os.mkdir("data_rar")
if not os.path.exists("data_pdf"):
    os.mkdir("data_pdf")
sum_txt = 0
sum_rar = 0
sum_pdf = 0
txt_size = 0
rar_size = 0
pdf_size = 0
for filename_txt in os.listdir():
    if ".txt" in filename_txt:
        txt_size += os.path.getsize(filename_txt)
        os.replace(filename_txt, f"data_txt/{filename_txt}")
        sum_txt += 1
for filename_rar in os.listdir():
    if ".rar" in filename_rar:
        rar_size += os.path.getsize(filename_rar)
        os.replace(filename_rar, f"data_rar/{filename_rar}")
        sum_rar += 1
for filename_pdf in os.listdir():
    if ".pdf" in filename_pdf:
        pdf_size += os.path.getsize(filename_pdf)
        os.replace(filename_pdf, f"data_pdf/{filename_pdf}")
        sum_pdf += 1
print(f"{sum_txt} файл/-ов перемещено в папку data_txt общим размером - {txt_size} кб")
print(f"{sum_rar} файл/-ов перемещено в папку data_rar общим размером - {rar_size} кб")
print(f"{sum_pdf} файл/-ов перемещено в папку data_pdf общим размером - {pdf_size} кб")
os.rename(f"data_txt/{filename_txt}", "data_txt/renamed.txt")
print(f"Файл {filename_txt} был переименован в renamed.txt")
