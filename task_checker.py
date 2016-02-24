#!/usr/bin/python3

from tkinter import *
from tkinter import messagebox
import json
from datetime import datetime

fields = ("Task 1", "Task 2", "Task 3")


def enter_tasks(entries):

    task_one = entries["Task 1"].get()
    task_two = entries["Task 2"].get()
    task_three = entries["Task 3"].get()

    present = datetime.today()
    now_string = str(present.year) + "," + \
                str(present.month) + "," + str(present.day)

    with open("daily.json", "w") as f:
        json.dump(
            {"tasks_entered": True, "date_entered": now_string,
                "tasks": [task_one, task_two, task_three]}, f)

    messagebox.showinfo(
        "Submitted", "Your tasks for the day have been submitted.")
    update_journal()
    return


def make_task_form(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field + ": ", anchor="w")
        ent = Entry(row)
        ent.insert(0, "")
        row.pack(side=TOP, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES)
        entries[field] = ent

    return entries


def display_tasks(root):
    with open("daily.json") as f:
        json_data = json.load(f)
        tasks = json_data["tasks"]
        for line in tasks:
            row = Frame(root)
            lab = Label(row, width=50, text=line.strip(), anchor="w")
            row.pack(side=TOP, padx=5, pady=5)
            lab.pack(side=TOP)
    return


def update_journal():
    """
    Inserts a base journal entry for the day containing the date
    as well as headers for the different sections.
    """
    with open("logging.md", "a") as journal:
        now = datetime.now()
        journal.write("\n# " + now.strftime("%B %d, %Y") + "  \n\n")

        with open("journal_base.md") as base:
            previous = ""
            for line in base:
                if previous == "#### Goals\n":
                    with open("daily.json") as f:
                        json_data = json.load(f)
                        tasks = json_data["tasks"]
                        for task in tasks:
                            journal.write("- " + task + "\n")
                else:
                    journal.write(line)

                previous = line

def schedule_check():
    """
    Checks if the tasks for the day have been entered. If they have,
    the present the tasks. Otherwise, allow user to enter day tasks.
    """
    root = Tk()
    root.wm_title("Daily Task Manager")
    ents = None

    tasks_entered = None

    try:
        with open("daily.json") as f:
            json_data = json.load(f)

            # date_info has year, month, then day
            date_info = [int(x) for x in json_data["date_entered"].split(",")]
            past = datetime(date_info[0], date_info[1], date_info[2])

            present = datetime.today()
            if ((present - past).days > 0):
                tasks_entered = False
            else:
                tasks_entered = json_data["tasks_entered"]

    except IOError:
        tasks_entered = False
    finally:
        if tasks_entered:
            display_tasks(root)
        else:
            ents = make_task_form(root, fields)
            root.bind("<Return>", lambda event, e=ents: enter_tasks(e))
            submit = Button(root, text="Submit",
                            command=(lambda e=ents: enter_tasks(e)))
            submit.pack(side=BOTTOM, padx=35, pady=5)

        root.mainloop()

schedule_check()
