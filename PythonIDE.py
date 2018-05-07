from tkinter import *
import tkinter.messagebox
from io import StringIO
root = Tk()
root.geometry('800x500')
root.title('Run your Python Code here')
color = 'gray77'
root.configure(bg=color)
root.resizable(width=False, height=False)

def clear_python():
    python_code.delete('1.0', END)

def run():
    old_stdout = sys.stdout
    redirected_output = sys.stdout = StringIO()
    exec(python_code.get('1.0', END))
    sys.stdout = old_stdout
    tkinter.messagebox.showinfo('Result', redirected_output.getvalue())

top = Frame(root, width=800, height=50, bg=color)
top.pack(side=TOP)

bottom = Frame(root, width=800, height=500, bg=color)
bottom.pack(side=BOTTOM)

btn_clear = Button(top, text='Clear', highlightbackground=color,
                   font=('arial', 25, 'bold'),width=10, command= lambda : clear_python())
btn_clear.pack(side=TOP)

btn_run = Button(top, text='Run', highlightbackground=color,
                   font=('arial', 25, 'bold'), width=10, command=lambda : run())
btn_run.pack(side=TOP)

python_code = Text(bottom, font=('arial', 25, 'bold'), bg='gray88')
python_code.pack(side=TOP)

root.mainloop()


'''
for i in range(1,10):
	print(i)
'''