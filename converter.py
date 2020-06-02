import PySimpleGUI as sg
from docx2pdf import convert

sg.theme('Dark Blue 3')
layout = ([sg.Text('Конвертировать 1 файл')],
          [sg.Input(), sg.FileBrowse()],
          [sg.Text('Конвертировать папку')],
          [sg.Input(), sg.FolderBrowse()],
          [sg.Text('Куда конвертировать папку (необязательно)')],
          [sg.Input(), sg.FolderBrowse()],
          [sg.Button('Начать')])

window = sg.Window('docx 2 pdf', layout)
vent, values = window.read()
directorFile = values[0]
directoryFolderInput = values[1]
directoryFolderOutput = values[2]
if directorFile != "":
    convert(directorFile)
if directoryFolderInput != "" and directoryFolderOutput != "":
    convert(directoryFolderInput, directoryFolderOutput)
if directorFile != "":
    convert(directoryFolderInput)
window.close()
