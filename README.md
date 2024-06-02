* Название, 
* Описание (что делает?), 
* Как установить/начать работу? (какие пакеты скачать и как)

Название : Форматирование файлов

Описание: Программа получает файлы из папки Files, и выполняет следующее форматирование:
- шрифт – Times New Roman
- размер шрифта – 14
- межстрочный интервал – 1,5

Используются пакеты :
os
Document  
docx.shared (Pt)

Для установки пакетов необходимо использовать установщик pip.
pip является лучшей программой установки.
Начиная с Python 3.4, он включен по умолчанию в бинарные инсталляторы Python.

pip install python-docx 
далее подключение ... 
from docx import Document
from docx.shared import Pt

https://python-docx.readthedocs.io/en/latest/user/install.html