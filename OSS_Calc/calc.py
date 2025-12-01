import tkinter as tk


 class Calculator:
     def __init__(self, root):
         self.root = root
         self.root.title("계산기")
         self.root.geometry("300x400")

         self.expression = ""
+        self.history = []

@@
         buttons = [
            ['7', '8', '9', '/'],
            ['4', '5', '6', '*'],
            ['1', '2', '3', '-'],
            ['0', '.', 'C', '+'],
-           ['=']
+           ['=', 'H']
         ]

@@
     def on_click(self, char):
         if char == 'C':
             self.expression = ""
         elif char == '=':
             try:
                 self.expression = str(eval(self.expression))
+                self.history.append(self.expression)
             except Exception:
                 self.expression = "에러"
+        elif char == 'H':
+            self.open_history_window()
         else:
             self.expression += str(char)

@@
+    def open_history_window(self):
+        win = tk.Toplevel(self.root)
+        win.title("계산 기록")
+        win.geometry("300x300")
+
+        listbox = tk.Listbox(win, font=("Arial", 16))
+        listbox.pack(expand=True, fill="both")
+
+        for item in self.history:
+            listbox.insert(tk.END, item)




