# from tkinter import ttk
# from tkinter import *
#
# # def setvars():
# #     user_acct = acct_entry.get()
# #     user_proj = proj_entry.get()
# #     user_notes = notes_entry.get()
#
#
# root = Tk()
# root.title('Account#/Project#/Notes')
# root.geometry('550x300')
# root.wm_maxsize(width=550, height=300)
# root.iconbitmap('cp.ico')
# proj_lbl = Label(text='Project Number:')
# proj_lbl.pack()
# project = StringVar(root, value='7003.01.006.05')
# proj_entry = Entry(root, textvariable=project)
# # proj_entry.grid(row=0, column=0, pady=5)
# proj_entry.pack(pady=5)
# acct_lbl = Label(text='Account Number:')
# acct_lbl.pack()
# account = StringVar(root, value='610-201-30')
# acct_entry = Entry(root, textvariable=account)
# # acct_entry.grid(row=0, column=1, pady=5)
# acct_entry.pack(pady=5)
# notes_lbl = Label(text='Notes:')
# notes_lbl.pack(pady=15)
# notes = 'SHRO incentive program restocking for prize vault/attire'
# notes_entry = Text(root, width=50, height=6, wrap='word')
# notes_entry.insert(END, notes)
#
# notes_entry.pack(pady=5)
#
# set_var = Button(root, text='Submit', command=setvars)
# set_var.pack(pady=10, padx=20)
#
#
#
# root.mainloop()
#
