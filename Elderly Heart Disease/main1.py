import sys
import PySimpleGUI as sg

sg.theme("dark grey 10")

def GUI():
    layout = [[sg.Text("Enter 2 numbers to perform any process you want")], [sg.InputText("a")], [sg.InputText("b")],
              [sg.Radio("Yes", group_id=1)], [sg.Radio("No", group_id=1)],
              [sg.Checkbox("do want to display the entered values")],
              [sg.Submit(), sg.Cancel()]]

    window = sg.Window("Demo program", layout, size=(400, 400))

    events, values = window.read()
    for i in values:
        if values[i] == True:
            selection = i - 1

    file = open("user input.txt", "w")

    file.write(str(values[0]) + '\n')
    file.write(str(values[1]) + '\n')
    file.write(str(selection) + '\n')

    file.close()

    window.close()


print("Enter 2 number to perform one of 4 processes: "
      "\n1: a + b"
      "\n2: a - b"
      "\n3: a * b"
      "\n4: a / b")

GUI()
sys.stdin = open("user input.txt")
a = int(input())
b = int(input())
s = int(input())

if s == 1:
    sg.popup("a + b", a + b)
    # print(a + b)
elif s == 2:
    sg.popup("a - b", a - b)
# print(a - b)
elif s == 3:
    sg.popup("a * b", a * b)
    # print(a * b)
elif s == 4:
    sg.popup("a / b", a / b)
    # print(a / b)
