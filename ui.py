import fetchLists as fl
from tkinter import *
from tkinter import ttk
import tkhtmlview as tw

root = Tk()

root.geometry("1500x700")
root.title("Compare Lists")

def make(amount, language):
    names = []
    for widget in root.winfo_children():
        widget.destroy()
    for i in range(int(amount)):
        names.append(ttk.Entry(root))
        names[i].grid(row=2, column=i, padx=5, pady=5)
    ttk.Button(root, text="Go Back", command=lambda: mainMenu()).grid(row=0, column=0, pady=3, sticky=NW)
    ttk.Button(root, text="Compare", command=lambda: compare(names, language)).grid(row=1, column=0, pady=3, sticky=W)



def compare(names, language):

    lists = []
    listboxes = []
    listframes = []
    root.grid_columnconfigure([i for i in range(len(names))], weight=1, uniform="column")
    resultframe = ttk.Frame(root)
    resultframe.grid(row=4, column=0, columnspan=len(names), pady=3)
    resultbox = tw.HTMLScrolledText(resultframe, pady=1)
    resultbox.pack()

    for i in range(len(names)):
        print(f"Fetching {names[i].get()}'s list")
        lists.append(fl.getTitlesFromUsername_List_Language(names[i].get(), "Completed", language))
        lists[i].sort()
        listframes.append(ttk.Frame(root))
        listframes[i].grid(row=3, column=i, padx=3)
        listboxes.append(tw.HTMLScrolledText(listframes[i], pady=1))
        listboxes[i].pack()
    
    print("All lists fetched")
    for i in range(len(lists)):
        print(f"Displaying {names[i].get()}'s list")
        
        text = "<html><body>"
        for title in lists[i]:
            print(f"Adding {title}")
            text += f"<h6>{title}</h6><br>"
        text += "</body></html>"
        listboxes[i].set_html(text)

    common = set(lists[0])
    for i in range(1, len(lists)):
        common = common & set(lists[i])
    print(f"Common items: {len(common)}")
    common = list(common)
    common.sort()
    result = "<html><body>"
    for anime in common:
        result += f"<h6>{anime}</h6><br>"
    result += "</body></html>"
    resultbox.set_html(result)

def mainMenu():
    for widget in root.winfo_children():
        widget.destroy()
    root.grid_columnconfigure(0, weight=0)
    ttk.Label(root, text="People to compare:").grid(row=0, column=0, padx=2, pady=2)
    e = ttk.Entry(root)
    e.grid(row=0, column=1, padx=5, pady=5)
    ttk.Label(root, text="Language:").grid(row=1, column=0, padx=2, pady=2)
    lang = ttk.Combobox(root, values=["romaji", "english"], state="readonly")
    lang.grid(row=1, column=1, padx=5, pady=5)
    lang.current(0)
    ttk.Button(root, text="Enter", command=lambda: make(e.get(), lang.get())).grid(row=2, column=0, columnspan=2, pady=5)

if __name__ == "__main__":
    mainMenu()
    root.mainloop()