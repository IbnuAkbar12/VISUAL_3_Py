import PySimpleGUI as sg
sg.theme("DarkGreen4")
sg.theme_text_color("#FFFF00")
window = sg.Window(title="Profile",
                   layout=[[sg.Text("SELAMAT DATANG DI KELAS",
                                    font=("Arial",25,"italic","bold","underline"))],
                           [sg.Text("NPM : 2210010416 ")],
                           [sg.Text("Nama : Ibnu Akbar ")],
                           [sg.Text("Kelas : 5P REG BJM ")]
                           ],
                   size=(510,200),
                   font=("Times", 18))
window()
window.close()