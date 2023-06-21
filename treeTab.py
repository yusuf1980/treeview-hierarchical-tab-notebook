from tkinter import *
from tkinter import ttk

root = Tk()
notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

# create frames
frame1 = ttk.Frame(notebook, width=400, height=10)
frame2 = ttk.Frame(notebook, width=400, height=10)

frame1.pack(fill='both', expand=True)
frame2.pack(fill='both', expand=True)

# add frames to notebook

notebook.add(frame1, text='General Information')
notebook.add(frame2, text='Profile')
label = Label(root, text="Treeview Tab").pack(side=TOP, pady=10)

treeview = ttk.Treeview(root, height=7)
treeview.pack()
treeview.insert('','0','item0', text="First Item")
treeview.insert('','1','item1', text="Second Item")
treeview.insert('','2','item2', text="Third Item")
treeview.insert('','3','item3', text="Fourth Item")
treeview.insert('','4','item4', text="Fifth Item")
#moving items
treeview.move('item1','item0', 'end')
treeview.move('item2','item0', 'end')


root.geometry("350x220")
root.title("Threeview Hierarchical")
root.mainloop()