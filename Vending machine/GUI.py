import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import os  # ใช้สำหรับตรวจสอบการมีอยู่ของไฟล์

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("Alice's Artistry")
root.geometry("800x500")

label = tk.Label(root, text="こんにちは。 Welcome to Alice's Artistry ♡", 
                 font=("Arial", 24),   
                 fg="#7f3f1f")
label.pack(pady=20)

cover_image = Image.open("Alice_cover.jpg")
size = cover_image.resize((700, 250), Image.LANCZOS)
photo = ImageTk.PhotoImage(size)

label = tk.Label(root, image=photo)
label.place(x=50, y=100)

def enter_store(): 
    print("Enter to Store")
    my_store = tk.Toplevel(root)
    my_store.title("Alice's Artistry Store")
    my_store.geometry("800x700")

    products = { #สินค้า
    "Pencil": {
        "2B": {"price": 15, "stock": 100, "details": "ดินสอ 2B"},
        "HB": {"price": 10, "stock": 80, "details": "ดินสอ HB"},
        "EE": {"price": 30, "stock": 60, "details": "ดินสอ EE"}
    },
    "Eraser": {
        "Pentel": {"price": 12, "stock": 50, "details": "ยางลบ เล็ก Pentel ZEH-03E"},
        "MONO": {"price": 22, "stock": 30, "details": "ยางลบดินสอ MONO PE-01"},
        "Quantum": {"price": 10, "stock": 100, "details": "ยางลบควอนตั้ม QE600-50"} 
    },
    "Sketchbook": {
        "Master Art": {"price": 32, "stock": 100, "details": "Master Art SP104 A5 สมุดวาดรูป"},
        "Canson Fine Face": {"price": 185, "stock": 43, "details": "Canson Fine Face A3 สมุดวาดรูป"},
        "Derwent Black Paper Pad": {"price": 275 , "stock": 32, "details": "Derwent Black Paper Pad สมุดวาดรูป"} 
        },
    "Brush": {
        "No.0": {"price": 10, "stock": 114, "details": "พู่กันเบอร์ 0"},
        "No.1": {"price": 12, "stock": 136, "details": "พู่กันเบอร์ 1"},
        "No.2": {"price": 13, "stock": 148, "details": "พู่กันเบอร์ 2"},
        "No.3": {"price": 14, "stock": 150, "details": "พู่กันเบอร์ 3"},
        "No.4": {"price": 17, "stock": 197, "details": "พู่กันเบอร์ 4"},
        "No.5": {"price": 19, "stock": 216, "details": "พู่กันเบอร์ 5"},
        "No.6": {"price": 20, "stock": 228, "details": "พู่กันเบอร์ 6"},
        "No.7": {"price": 23, "stock": 262, "details": "พู่กันเบอร์ 7"},
        "No.8": {"price": 27, "stock": 307, "details": "พู่กันเบอร์ 8"},
        "No.9": {"price": 34, "stock": 387, "details": "พู่กันเบอร์ 9"},
        "No.10": {"price": 42, "stock": 558, "details": "พู่กันเบอร์ 10"},
    },
    "100 pound paper": {
        "Size A4": {"price": 5, "stock": 200, "details": "กระดาษร้อยปอนด์ขนาด A4"},
        "Size A3": {"price": 10, "stock": 112, "details": "กระดาษร้อยปอนด์ขนาด A3"},
        "Size A2": {"price": 20, "stock": 50, "details": "กระดาษร้อยปอนด์ขนาด A2"},
        "Size A1": {"price": 25, "stock": 60, "details": "กระดาษร้อยปอนด์ขนาด A1"},

    },
    "color palette": {
        "Grade A": {"price": 5, "stock": 50, "details": "Grade A"},
        "Grade B": {"price": 20, "stock": 23, "details": "Grade B"},
        "Grade C": {"price": 38, "stock": 14, "details": "Grade C"},
    },
    "poster color": {        
        "White": {"price": 25, "stock": 20, "details": "สีโปสเตอร์สีขาว"},
        "Blue": {"price": 25, "stock": 25, "details": "สีโปสเตอร์สีน้ำเงิน"},
        "Black": {"price": 25, "stock": 12, "details": "สีโปสเตอร์สีดำ"},
        "Red": {"price": 25, "stock": 8, "details": "สีโปสเตอร์สีแดง"},
        "Yellow": {"price": 25, "stock": 16, "details": "สีโปสเตอร์เหลือง"},
        },
}

    # ฟังก์ชันเมื่อเลือกสินค้าหลักใน dropdown
    def Select_product(event):
        selected_product = product_dropdown.get()
        if selected_product in products:
            # ลบปุ่มสินค้าชนิดย่อยที่มีอยู่ก่อนหน้านี้
            for widget in sub_product_frame.winfo_children():
                widget.destroy()
            
            # สร้างปุ่มสำหรับสินค้าชนิดย่อยพร้อมรูปภาพ (ถ้ามี)
            for sub_product in products[selected_product]:
                image_path = f"{sub_product}.jpg"  # สมมติว่ารูปภาพมีชื่อไฟล์เหมือนกับชื่อชนิดย่อย เช่น "2B.jpg"
                
                if os.path.exists(image_path):  # ตรวจสอบว่ารูปภาพมีอยู่หรือไม่
                    # โหลดและปรับขนาดรูปภาพ
                    img = Image.open(image_path)
                    img = img.resize((50, 50), Image.LANCZOS)
                    img_photo = ImageTk.PhotoImage(img)

                    # สร้างปุ่มพร้อมรูปภาพและข้อความ
                    sub_product_btn = tk.Button(sub_product_frame, text=sub_product, image=img_photo,
                                                compound=tk.TOP,  
                                                command=lambda p=selected_product, sp=sub_product: on_sub_product_select(p, sp))
                    sub_product_btn.image = img_photo  # เก็บการอ้างอิงรูปภาพไว้เพื่อป้องกันการถูก garbage collected
                else:
                    # สร้างปุ่มธรรมดาถ้าไม่มีรูปภาพ
                    sub_product_btn = tk.Button(sub_product_frame, text=sub_product,
                                                command=lambda p=selected_product, sp=sub_product: on_sub_product_select(p, sp))
                
                sub_product_btn.pack(side=tk.LEFT, padx=5, pady=5)

    # ฟังก์ชันเมื่อกดปุ่มเลือกชนิดสินค้าย่อย
    def on_sub_product_select(product, sub_product):
        info = products[product][sub_product]
        product_info.config(text=f"{sub_product}\n"
                                 f"Price: {info['price']} THB\n"
                                 f"Stock: {info['stock']} ชิ้น\n"
                                 f"Details: {info['details']}")
        add_to_cart_btn.config(command=lambda: add_to_cart(product, sub_product))

    # ฟังก์ชันเพิ่มสินค้าลงตะกร้า
    def add_to_cart(product, sub_product):
        if products[product][sub_product]['stock'] > 0:
            cart_listbox.insert(tk.END, f"{sub_product} - {products[product][sub_product]['price']} THB")
            products[product][sub_product]['stock'] -= 1
            update_total_price()

    # ฟังก์ชันอัพเดทราคาสินค้ารวม
    def update_total_price():
        total = 0
        for item in cart_listbox.get(0, tk.END):
            price = int(item.split("-")[-1].strip().split()[0])
            total += price
        total_label.config(text=f"Total: {total} THB")

    # ฟังก์ชันลบสินค้าจากตะกร้า
    def remove_from_cart():
        selected_index = cart_listbox.curselection()
        if selected_index:
            cart_listbox.delete(selected_index)
            update_total_price()

    # ฟังก์ชันยืนยันการสั่งซื้อ
    def confirm_purchase():
        if not cart_listbox.get(0, tk.END):
            messagebox.showwarning("Warning", "ไม่มีสินค้าในตะกร้า")
            return

        total_price = 0
        for item in cart_listbox.get(0, tk.END):
            price = int(item.split("-")[-1].strip().split()[0])
            total_price += price

        payment_window = tk.Toplevel(my_store)
        payment_window.title("สรุปรายการและชำระเงิน")
        payment_window.geometry("400x500")

        cart_summary = tk.Label(payment_window, text="รายการสินค้าในตะกร้า" ,background="#f1ddc9" )
        cart_summary.pack(pady=5)

        for item in cart_listbox.get(0, tk.END):
            cart_item_label = tk.Label(payment_window, text=item)
            cart_item_label.pack(pady=5)

        # แสดงยอดรวมทั้งหมด
        total_summary_label = tk.Label(payment_window, text=f"ยอดรวมทั้งหมด: {total_price} THB")
        total_summary_label.pack(pady=5)

        payment_methods = ["PromptPay", "เงินสด"]
        payment_method_var = tk.StringVar(value=payment_methods[0])
        payment_method_label = tk.Label(payment_window, text="เลือกวิธีชำระเงิน")
        payment_method_label.pack(pady=5)

        payment_dropdown = ttk.Combobox(payment_window, textvariable=payment_method_var, values=payment_methods,background="#f1ddc9")
        payment_dropdown.pack(pady=5)

        qr_label = tk.Label(payment_window)
        cash_label = tk.Label(payment_window)
        cash_entry = tk.Entry(payment_window)

        def on_payment_select(event):
            selected_payment = payment_method_var.get()
            qr_label.pack_forget()
            cash_label.pack_forget()
            cash_entry.pack_forget()

            if selected_payment == "PromptPay":
                qr_label.config(text="สแกน QR Code เพื่อชำระเงิน")
                qr_label.pack(pady=5)
            elif selected_payment == "เงินสด":
                cash_label.config(text="กรอกจำนวนเงิน")
                cash_label.pack(pady=5)
                cash_entry.pack(pady=5)

        payment_dropdown.bind("<<ComboboxSelected>>", on_payment_select)

        def confirm_payment():
            selected_payment = payment_method_var.get()
            if selected_payment == "เงินสด":
                cash_entered = int(cash_entry.get())
                if cash_entered >= total_price:
                    change = cash_entered - total_price
                    messagebox.showinfo("Payment Successful", f"ชำระเงินสำเร็จ! เงินทอน: {change} THB")
                else:
                    messagebox.showerror("Error", "จำนวนเงินไม่เพียงพอ")
            else:
                messagebox.showinfo("Payment Successful", "ชำระเงินสำเร็จ! \nขอบคุณที่มาอุดหนุนสินค้านะคะ")

            receipt = tk.Toplevel(payment_window)
            receipt.title("ใบเสร็จ")
            receipt.geometry("300x300")
            receipt_label = tk.Label(receipt, text="ใบเสร็จ\nรายการสินค้า")
            receipt_label.pack(pady=5)
            receipt_label = tk.Label(receipt, text="------------------------------------")
            receipt_label.pack(pady=5)
            for item in cart_listbox.get(0, tk.END):
                receipt_item_label = tk.Label(receipt, text=item)
                receipt_item_label.pack(pady=5)
            total_label = tk.Label(receipt, text=f"รวม: {total_label.cget('text')}")
            total_label.pack(pady=5)

            payment_window.destroy()
            my_store.destroy()

        confirm_payment_btn = tk.Button(payment_window, text="ยืนยันการชำระเงิน",background="#f1ddc9", command=confirm_payment)
        confirm_payment_btn.pack(pady=10)

#---------------------------------------------------------------------------------------------------------

    # ข้อความที่แสดงก่อน dropdown ในหน้าต่างร้านค้า
    label = tk.Label(my_store, text="เลือกสินค้าที่คุณต้องการได้ที่นี่ Alice's Artistry ยินดีให้บริการ", 
                     font=("Arial", 18),   
                     fg="#7f3f1f")
    label.pack(pady=5)

    # Dropdown สำหรับเลือกสินค้าหลัก
    product_var = tk.StringVar(value="Select a product")
    product_dropdown = ttk.Combobox(my_store, textvariable=product_var, values=list(products.keys()),background="#f1ddc9")
    product_dropdown.pack(pady=10)
    product_dropdown.bind("<<ComboboxSelected>>", Select_product)

    # สร้างเฟรมสำหรับแสดงปุ่มสินค้าชนิดย่อย
    sub_product_frame = tk.Frame(my_store)
    sub_product_frame.pack(pady=10)

    product_info = tk.Label(my_store, text="")
    product_info.pack(pady=10)

    add_to_cart_btn = tk.Button(my_store, text="Add to Cart",background="#f1ddc9", command=None)
    add_to_cart_btn.pack(pady=5)

    cart_listbox = tk.Listbox(my_store)
    cart_listbox.pack(pady=10)

    remove_from_cart_btn = tk.Button(my_store, text="Remove from Cart",background="#f1ddc9", command=remove_from_cart)
    remove_from_cart_btn.pack(pady=5)

    total_label = tk.Label(my_store, text="Total: 0 THB")
    total_label.pack(pady=10)

    confirm_btn = tk.Button(my_store, text="Confirm Purchase",background="#f1ddc9", command=confirm_purchase)
    confirm_btn.pack(pady=20)


# ปุ่มเข้าสู่หน้าร้านค้า
click_enter_store = tk.Button(root, text="Enter to Store",          
                              command=enter_store,      
                              font=("Arial", 16),       
                              bg="#7f3f1f",               
                              fg="White",               
                              width=12,                 
                              height=1,                 
                              bd=3,                         
                              highlightbackground="black")                  
click_enter_store.place(x=330, y=400)


# เริ่มต้นการแสดงผล GUI
root.mainloop()
