from appJar import gui
import PhonebookDB as DB


def press(name):

    if name == "Add":
        DB.createPerson(win.getEntry("nameEntry"), win.getEntry("phoneEntry"), win.getEntry("emailEntry"), int(win.getEntry("ageEntry")))
        win.clearAllEntries()

    elif name == "Cancel":
        win.stop()

    elif name == "Search":
        win.clearListBox("listbox")
        fillListbox(DB.searchPerson(win.getEntry("searchEntry")))

def fillListbox(list):
    print(list)
    win.addListItem("listbox", list[0])
    win.addListItem("listbox", list[1])
    win.addListItem("listbox", list[2])
    win.addListItem("listbox", list[3])


# Frame
# win.setSize("600x600")
win = gui("Addressbok")
win.setResizable(True)

# Search button
win.addButton("Search", press, 0, 0)
win.addEntry("searchEntry", 0, 1)

# Person Entry
win.addLabel("nameLbl", "Name", 1, 0)
win.addEntry("nameEntry", 2, 0, )

win.addLabel("phoneLbl", "Phone", 3, 0)
win.addEntry("phoneEntry", 4, 0)

win.addLabel("emailLbl", "Email", 5, 0)
win.addEntry("emailEntry", 6, 0)

win.addLabel("ageLbl", "Age", 7, 0)
win.addEntry("ageEntry", 8, 0)

# Add & Cancel button
win.addButtons(["Add", "Cancel"], press, 11)

# Listbox
win.addListBox("listbox", None, 12, 1)

# Launch
win.go()
