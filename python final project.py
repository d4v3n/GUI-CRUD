import tkinter as tk
import os

folder = r"D:\pythoon 2\text"

def create_file():
    try:
        nama_file = f"{teks_nama.get()}.txt"
        if nama_file != "":
            teks = kolom_teks.get("1.0", tk.END)
            with open(os.path.join(folder, nama_file), "w") as file:
                file.write(teks)
            kolom_teks.delete("1.0", tk.END)
            read_text()
    except Exception as e:
        print("Error:", e)

def append_text():
    try:
        nama_file = f"{teks_nama.get()}.txt"
        if nama_file !="":
            teks = kolom_teks.get("1.0", tk.END)
            with open(os.path.join(folder, nama_file), "a") as file:
                file.write(teks)
            kolom_teks.delete("1.0", tk.END)
            read_text()
    except Exception as e:
        print("Error:", e)

def read_text():
    try:
        nama_file = f"{teks_nama.get()}.txt"
        if nama_file != "":
            with open(os.path.join(folder, nama_file), "r") as file:
                data = file.read()
                kolom_tampil.delete("1.0", tk.END)
                kolom_tampil.insert(tk.END, data)
        else:
            kolom_tampil.delete("1.0", tk.END)
    except Exception as e:
        print("Error:", e)

def update_text():
    try:
        nama_file = f"{teks_nama.get()}.txt"
        if nama_file != "":
            search = searchText.get()
            new = updateteks.get()
            with open(os.path.join(folder, nama_file), "r") as file:
                data = file.read()
                data = data.replace(search, new)
            with open(os.path.join(folder, nama_file), "w") as file:
                file.write(data)
            searchText.delete(0, tk.END)
            updateteks.delete(0, tk.END)
            read_text()
    except Exception as e:
        print("Error:", e)

def delete_txt():
    try:
        nama_file = f"{deletefile.get()}.txt"
        if nama_file != "":
            os.remove(os.path.join(folder, nama_file))
            deletefile.delete(0, tk.END)
            kolom_tampil.delete("1.0", tk.END)
            teks_nama.delete(0, tk.END)
    except Exception as e:
        print("Error:", e)


root = tk.Tk()
root.title("GUI CRUD")

root.geometry("1000x500")

label = tk.Label(root, text="Nama File :")
label.place(x=25, y=5)

teks_nama = tk.Entry(root)
teks_nama.place(x=95, y=7)

label = tk.Label(root, text="Teks :")
label.place(x=25, y=35)

kolom_teks = tk.Text(root, width=30, height=7)
kolom_teks.place(x=25, y=60)

button = tk.Button(root, text="Create", command=create_file)
button.place(x=280, y=60)

button = tk.Button(root, text="Append", command=append_text)
button.place(x=280, y=105)

label = tk.Label(root, text="Tampil :")
label.place(x=350, y=35)

kolom_tampil = tk.Text(root, width=30, height=7)
kolom_tampil.place(x=350, y=60)

button = tk.Button(root, text="Read", command=read_text)
button.place(x=605, y=60)

label = tk.Label(root, text="Search Teks :")
label.place(x=25, y=188)

searchText = tk.Entry(root)
searchText.place(x=25, y=210)

label = tk.Label(root, text="Update Teks :")
label.place(x=195, y=188)

updateteks = tk.Entry(root)
updateteks.place(x=195, y=210)

button = tk.Button(root, text="Update", command=update_text)
button.place(x=350, y=202)

label = tk.Label(root, text="File :")
label.place(x=25, y=238)

deletefile = tk.Entry(root)
deletefile.place(x=25, y=260)

button = tk.Button(root, text="Delete", command=delete_txt)
button.place(x=180, y=254)

root.mainloop()