from __future__ import with_statement
import contextlib
import sys
import time

from pyke import knowledge_engine
from pyke import krb_traceback, goal
import sys
import PySimpleGUI as sg


engine = knowledge_engine.engine(__file__)
fc_goal = goal.compile('symptoms.diagnosis($diagnosis)')

def bc_test():
    engine.reset()  # Allows us to run tests multiple times.

    engine.activate('bc_rules')  # STUDENTS: you will need to edit the name of your rule file here

    print("doing proof")

    try:
        with fc_goal.prove(engine) as gen:  # STUDENTS: you will need to edit this line
            for vars, plan in gen:
                print("Your diagnosis is: %s" % (vars['diagnosis']))  # STUDENTS: you will need to edit this line
    except Exception:
        # This converts stack frames of generated python functions back to the
        # .krb file.
        krb_traceback.print_exc()
        sys.exit(1)

    print()
    print("done")
    # engine.print_stats()


bc_test()

sg.theme("dark grey 10")
layout=[
    [
        [
            sg.Text("Question")
        ],
        [
            sg.Button("y")
        ],
        [
            sg.Button("n")
        ],
        [
            sg.Text("Result")
        ]
    ]
]
#Create a window
window = sg.Window ("Expert Heart Deasieases System", layout, size=(400, 400))
while True:
    event, values = window.read()
    print(event)
    if event == sg.WIN_CLOSED:
        break

window.close()
exit()






