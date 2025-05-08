from tkinter import *
from tkinter import ttk

# สีหลัก
BG_COLOR = "#FFF5E1"       # สีพื้นหลังครีมอ่อน
LABEL_COLOR = "#333333"    # สีข้อความเข้ม
BTN_COLOR = "#FFB347"      # สีปุ่มส้มอ่อน
BTN_ACTIVE = "#FFA07A"     # สีปุ่มเมื่อ hover
ENTRY_BG = "#FFFFFF"       # สีช่องกรอก

# สร้างหน้าต่างหลัก
root = Tk()
root.title("tempFlipper")
root.geometry("500x300")
root.iconbitmap("tempFlipper.ico")  # ตรวจสอบว่าไฟล์อยู่ในโฟลเดอร์เดียวกัน
root.resizable(0, 0)
root.configure(bg=BG_COLOR)

# ฟังก์ชันรีเซ็ตค่า
def reset():
    output_txt.delete(0, "end")
    input_txt.delete(0, "end")
    temp_combo.set("เควิน")

# ฟังก์ชันแปลงอุณหภูมิ
def convert():
    output_txt.delete(0, END)
    try:
        celcius_value = float(input_txt.get())
        unit_value = temp_combo.get()
        if unit_value == "เควิน":
            kelvin = celcius_value + 273.15
            output_txt.insert(0, f"{kelvin:.2f}")
        elif unit_value == "ฟาเรนไฮน์":
            fahrenheit = celcius_value * 1.8 + 32
            output_txt.insert(0, f"{fahrenheit:.2f}")
        else:
            output_txt.insert(0, "เลือกหน่วยให้ถูกต้อง")
    except ValueError:
        output_txt.insert(0, "ป้อนตัวเลขเท่านั้น")

# ฟอนต์
font = ("Kanit", 14)

# สร้างองค์ประกอบ
input_label = Label(root, text="อุณหภูมิ (เซลเซียส)", font=font, bg=BG_COLOR, fg=LABEL_COLOR)
input_txt = Entry(root, width=20, font=font, bg=ENTRY_BG)

unit_label = Label(root, text="แปลงเป็นหน่วย", font=font, bg=BG_COLOR, fg=LABEL_COLOR)
unit_list = ["ฟาเรนไฮน์", "เควิน"]
temp_combo = ttk.Combobox(root, values=unit_list, font=font, width=18)
temp_combo.set("เควิน")

output_label = Label(root, text="ผลลัพธ์", font=font, bg=BG_COLOR, fg=LABEL_COLOR)
output_txt = Entry(root, width=20, font=font, bg=ENTRY_BG)

convertBtn = Button(
    root, text="แปลง", font=font, bg=BTN_COLOR, activebackground=BTN_ACTIVE,
    relief="raised", command=convert
)
resetBtn = Button(
    root, text="ล้าง", font=font, bg=BTN_COLOR, width=7, activebackground=BTN_ACTIVE,
    relief="raised", command=reset
)

# จัดวาง Layout ด้วย Padding
input_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)
input_txt.grid(row=0, column=1, padx=10, pady=10)

unit_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)
temp_combo.grid(row=1, column=1, padx=10, pady=10)

output_label.grid(row=2, column=0, padx=10, pady=10, sticky=W)
output_txt.grid(row=2, column=1, padx=10, pady=10)

convertBtn.grid(row=3, column=1, sticky=W, padx=10, pady=10)
resetBtn.grid(row=3, column=1, sticky=E, padx=10, pady=10)

# เริ่มโปรแกรม
root.mainloop()
