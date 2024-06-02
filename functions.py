import os
from docx import Document
from docx.shared import Pt

def Task2():

    folder_path = "./Files" # Путь к папке с документами
    files= os.listdir(folder_path) # Получение списка файлов в папке
    return files

def Task1():
    file_list=Task2()
    folder_path = "./Files"
# Проход по каждому файлу
    for file_name in file_list:
        if file_name.endswith(".docx"):
            file_path = os.path.join(folder_path, file_name)

        # Открытие документа
        doc = Document(file_path)

        # Изменение параметров
        for paragraph in doc.paragraphs:
            # Изменение шрифта и размера шрифта
            for run in paragraph.runs:
                run.font.name = "Times New Roman"
                run.font.size = Pt(14)           
                paragraph.paragraph_format.line_spacing = 1.5 # Изменение межстрочного интервала        
            doc.save(file_path)# Сохранение изменений