import PySimpleGUI as sg
sg.theme("DarkGreen4")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("NPM    : 2210010416 ")],
                           [sg.Text("Nama   : Ibnu Akbar ")],
                           [sg.Text("Kelas  : 5P Regular Banjarmasin ")],
                           [sg.Text("Matkul : Pemprograman Visual 3 ")]
                           ],
                           size=(400,200))
window()
window.close()