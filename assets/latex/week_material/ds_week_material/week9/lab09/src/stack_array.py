# stack_array.py
# Lab 09 – Section 3.1: Stack จาก Array
#
# Stack คือโครงสร้างข้อมูลแบบ LIFO (Last In, First Out)
#   → element ที่ใส่เข้าสุดท้าย (เรียกว่า ดันไว้บน top)
#   → element ที่ pop/peek ออกก่อนคือ element ที่อยู่บน top
#
# ข้อกำหนด (Lab manual):
#   - ใช้ Python list เป็น storage ภายใน
#   - ห้ามใช้ method ที่ติดมากับ list โดยตรง (เช่น .append, .pop)
#   - ต้องจัดการ storage ผ่าน index (self._top) เอง
#
# งาน 3.1: เติม logic ใน push, pop, peek, is_empty, __len__

from typing import Any


class StackArray:
    """
    Stack ADT ที่ใช้ list เป็น storage ภายใน (LIFO)

    --- Attributes (internal) ---
        _data (list) : เก็บ element ทั้งหมด
        _top  (int)  : index ชี้ตำแหน่ง top  (-1 = stack ว่าง)

    --- Methods ที่นักศึกษาต้องเติมทั้งหมด ---
        is_empty()  → คืน True ถ้า stack ว่าง
        __len__()   → คืนจำนวน element
        push(x)     → วาง x บน top
        pop()       → เอา element บน top ออกและคืนค่า
        peek()      → ดูค่า top โดยไม่เอาออก
    """

    def __init__(self) -> None:
        self._data: list[Any] = []  # storage ภายใน — เพิ่มขนาดแบบ dynamic
        self._top: int = -1         # -1 = ยังไม่มี element, 0 = มี 1 element, ...

    def is_empty(self) -> bool:
        """คืน True ถ้า stack ว่าง (ใช้ _top ตรวจเช็ค)"""
        ####### IMPLEMENT HERE ########
        pass

    def __len__(self) -> int:
        """คืนจำนวน element ใน stack ในขณะนั้น"""
        ####### IMPLEMENT HERE ########
        pass

    def push(self, x: Any) -> None:
        """
        วาง x ลงบน top ของ stack

        แนวคิด:
          1. เพิ่ม _top ขึ้น 1
          2. ส่ง x ไปเก็บที่ _data[_top]
             (ถ้าตำแหน่งนั้นยังไม่มีใน _data ต้องขยายก่อนด้วย)
        """
        ####### IMPLEMENT HERE ########
        pass

    def pop(self) -> Any:
        """
        เอา element บน top ออก และคืนค่า

        คืน:
            element บน top 

        Raises:
            IndexError: ถ้า stack ว่าง

        แนวคิด:
          1. ตรวจว่างหรือไม่ → raise ถ้าว่าง
          2. เก็บค่าที่ตำแหน่ง _top ไว้
          3. ลด _top ลง 1 (ตัด element ออกจาก stack)
          4. คืนค่า
        """
        ####### IMPLEMENT HERE ########
        pass

    def peek(self) -> Any:
        """
        ดูค่า top โดยไม่เอาออก

        คืน:
            element บน top (ไม่เปลี่ยน stack)

        Raises:
            IndexError: ถ้า stack ว่าง

        แนวคิด:
            - รูปแบบเหมือน pop แต่ไม่ลด _top
        """
        ####### IMPLEMENT HERE ########
        pass

    def __repr__(self) -> str:
        return f"StackArray(top→{self._data[:self._top + 1]})"


# =============================================================
# demo
# =============================================================

if __name__ == "__main__":
    # หมายเหตุ: demo นี้จะแสดง None / error จนกว่านักศึกษาจะเติม logic
    s = StackArray()

    # is_empty บน stack เปล่า (คาดหวัง True)
    print("[เริ่มต้น]  is_empty คาดหวัง True :", s.is_empty())

    # push แล้วดู peek / pop
    s.push(1)
    s.push(2)
    s.push(3)
    print("หลัง push(1, 2, 3):", s)
    print("  peek คาดหวัง 3 :", s.peek())
    print("  pop  คาดหวัง 3 :", s.pop())
    print("  pop  คาดหวัง 2 :", s.pop())
    print("  len  คาดหวัง 1 :", s._top + 1)  # ดู _top โดยตรง ไว้ก่อนที่ __len__ จะสำเร็จ

    # ทดสอบ IndexError เมื่อ stack ว่าง
    s.pop()  # เอา element สุดท้ายออก
    try:
        s.pop()  # ควร raise IndexError
    except (IndexError, TypeError) as e:
        print("  IndexError จาก pop() บน stack ว่าง:", e)
    try:
        s.peek()  # ควร raise IndexError
    except (IndexError, TypeError) as e:
        print("  IndexError จาก peek() บน stack ว่าง:", e)
