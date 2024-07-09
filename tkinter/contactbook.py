#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import messagebox

c = []

def g():
    s = cl.curselection()
    if s:
        i = int(s[0])
        m = c[i]
        messagebox.showinfo("Selected Contact", f"Name: {m['n']}\nNumber: {m['p']}")
    else:
        messagebox.showwarning("Warning", "Please select a contact.")

def a():
    n = ne.get()
    p = pe.get()
    if n and p:
        c.append({'n': n, 'p': p})
        u()
        r()
    else:
        messagebox.showwarning("Warning", "Please enter both name and number.")

def e():
    s = cl.curselection()
    if s:
        i = int(s[0])
        n = ne.get()
        p = pe.get()
        if n and p:
            c[i] = {'n': n, 'p': p}
            u()
            r()
        else:
            messagebox.showwarning("Warning", "Please enter both name and number.")
    else:
        messagebox.showwarning("Warning", "Please select a contact to edit.")

def v():
    s = cl.curselection()
    if s:
        i = int(s[0])
        m = c[i]
        ne.delete(0, tk.END)
        ne.insert(tk.END, m['n'])
        pe.delete(0, tk.END)
        pe.insert(tk.END, m['p'])
    else:
        messagebox.showwarning("Warning", "Please select a contact.")

def r():
    ne.delete(0, tk.END)
    pe.delete(0, tk.END)

def u():
    cl.delete(0, tk.END)
    for m in c:
        cl.insert(tk.END, m['n'])

root = tk.Tk()
root.title("Contact Book")

f = tk.Frame(root)
f.pack(padx=10, pady=10)

nl = tk.Label(f, text="Name:")
nl.grid(row=0, column=0, sticky="e")

ne = tk.Entry(f)
ne.grid(row=0, column=1)

pl = tk.Label(f, text="Number:")
pl.grid(row=1, column=0, sticky="e")

pe = tk.Entry(f)
pe.grid(row=1, column=1)

ab = tk.Button(f, text="Add", command=a)
ab.grid(row=2, column=0, columnspan=2, pady=5)

eb = tk.Button(f, text="Edit", command=e)
eb.grid(row=3, column=0, columnspan=2, pady=5)

vb = tk.Button(f, text="View", command=v)
vb.grid(row=4, column=0, columnspan=2, pady=5)

gsb = tk.Button(f, text="Get Selected Contact", command=g)
gsb.grid(row=5, column=0, columnspan=2, pady=5)

cl = tk.Listbox(f)
cl.grid(row=0, column=2, rowspan=6, padx=10)

rb = tk.Button(f, text="Reset Fields", command=r)
rb.grid(row=6, column=0, columnspan=2, pady=5)

root.mainloop()


# In[ ]:




