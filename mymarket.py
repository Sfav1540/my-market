# งบประมาณเริ่มต้น
budget = 1000

# รายการสินค้าและราคา
items = {
    "หมูสับกิโล": 150,
    "เนื้ออกไก่": 105,
    "ไก่บ้าน(ตัว)": 120,
    "มาม่าต้มยำ": 6.50,
    "ข้าวสาร": 150,
    "น้ำตาล": 20,
    "ปลากระป๋องสามแม่ครัว": 10,
    "ซอสมะเขือเทศ": 18,
    "ผงชูรส": 10.25,
    "ไข่แยกดอลลิเบอร์": 120.25,
    "ชาเขียว": 21.50,
    "Pepsi": 29.50,
    "กาแฟ": 15.75,
    "ขนมป๊อปเนย": 19,
    "ชาไทย": 11.50,
}

# แสดงรายการสินค้า
print("รายการสินค้า:")
for i, (item, price) in enumerate(items.items(), start=1):
    print(f"{i}. {item} ราคา {price} บาท")

# เลือกสินค้า
selected_items = []
total_cost = 0

print("\nเลือกสินค้าสูงสุด 15 รายการ (ใส่หมายเลขสินค้า):")
for _ in range(15):
    try:
        choice = int(input("เลือกหมายเลขสินค้า (หรือใส่ 0 เพื่อหยุด): "))
        if choice == 0:
            break
        elif 1 <= choice <= len(items):
            item_name = list(items.keys())[choice - 1]
            item_price = items[item_name]
            if total_cost + item_price > budget:
                print("งบประมาณไม่เพียงพอสำหรับสินค้านี้!")
            else:
                selected_items.append(item_name)
                total_cost += item_price
                print(f"เพิ่ม {item_name} ในรายการ (ยอดรวม: {total_cost:.2f} บาท)")
        else:
            print("กรุณาเลือกหมายเลขสินค้าในช่วงที่กำหนด!")
    except ValueError:
        print("กรุณาใส่หมายเลขสินค้าเป็นตัวเลข!")

# แสดงผลลัพธ์
remaining_budget = budget - total_cost

print("\nรายการสินค้าที่เลือก:")
for item in selected_items:
    print(f"- {item}")
print(f"\nยอดรวมที่ใช้ไป: {total_cost:.2f} บาท")
print(f"เงินคงเหลือ: {remaining_budget:.2f} บาท")
