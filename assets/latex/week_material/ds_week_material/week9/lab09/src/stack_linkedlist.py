# stack_linkedlist.py
# ============================================================
# Lab 09 – ส่วนที่ 3.2  Stack จาก LinkedList
# ============================================================
#
# แนวคิด: Stack = โครงสร้าง LIFO (Last In First Out)
#   ครั้งนี้เราไม่ใช้ array โดยตรง แต่ใช้ LinkedList ที่เขียนไว้แล้ว
#   เป็น storage ภายใน
#
# กฎสำคัญ: push/pop ต้องทำที่ "หัว" (head) ของ LinkedList เสมอ
#   - push(x)  →  addHead(x)                        O(1)
#   - pop()    →  ดึง head.data แล้วเลื่อน head ออก  O(1)
#   - peek()   →  ดู head.data โดยไม่เอาออก          O(1)
#
#   ทำไมไม่ push/pop ที่หาง?
#   เพราะต้อง traverse ยาว O(n) ก่อนถึงหาง — ไม่มีประสิทธิภาพ
#
# งานนักศึกษา: เติม method ทั้ง 5 ใน class StackLinkedList
# ============================================================

from linked_list import LinkedList
from typing import Any


class StackLinkedList:
    """
    Stack ADT ที่ใช้ LinkedList เป็น storage ภายใน

    Attributes ภายใน
    ----------------
    _ll : LinkedList
        LinkedList ที่ใช้เก็บข้อมูล
        head ของ _ll = top ของ stack  (element ล่าสุดที่ push เข้ามา)

    Methods ที่ใช้งานได้แล้ว
    -------------------------
    __repr__  คืน string แสดงสถานะ stack

    Methods ที่นักศึกษาต้องเติม (ทั้งหมด 5 method)
    -------------------------------------------------
    is_empty()  คืน True ถ้า stack ว่าง
    __len__()   คืนจำนวน element ใน stack
    push(x)     ใส่ x ลงบน top
    pop()       นำ top ออกและคืนค่า ; raise IndexError ถ้าว่าง
    peek()      ดู top โดยไม่เอาออก ; raise IndexError ถ้าว่าง
    """

    def __init__(self) -> None:
        self._ll = LinkedList()   # head ของ _ll = top ของ stack

    # ----------------------------------------------------------
    # Methods ที่นักศึกษาต้องเติม
    # ----------------------------------------------------------

    def is_empty(self) -> bool:
        """
        คืน True ถ้า stack ว่าง  (ไม่มี element เลย)

        คำใบ้: stack ว่าง ↔ LinkedList ไม่มี node เลย
               ตรวจสอบจาก  self._ll._head  ว่าเป็น None หรือไม่
        """
        ####### IMPLEMENT HERE ########
        pass

    def __len__(self) -> int:
        """
        คืนจำนวน element ใน stack  (ต้อง return เป็น int เสมอ)

        คำใบ้: ต้อง traverse ตลอดทั้ง LinkedList แล้วนับ node
               ดูรูปแบบการ traverse ได้ที่ addTail / find ใน linked_list.py
        """
        ####### IMPLEMENT HERE ########
        pass

    def push(self, x: Any) -> None:
        """
        ใส่ x ลงบน top ของ stack

        คำใบ้: "top ของ stack" = "head ของ LinkedList"
               เรียก method ของ self._ll ที่เพิ่ม node ที่หัวได้เลย
        """
        ####### IMPLEMENT HERE ########
        pass

    def pop(self) -> Any:
        """
        นำ element บน top ออกจาก stack และคืนค่า

        Returns
        -------
        Any  ค่าที่อยู่บน top ก่อนถูกนำออก

        Raises
        ------
        IndexError  ถ้า stack ว่าง

        คำใบ้ (3 ขั้น):
          1. ตรวจว่า stack ว่างหรือไม่ → ถ้าว่าง raise IndexError
          2. เก็บค่า top ไว้ก่อน:  val = self._ll._head.data
          3. เลื่อน head ออก: เรียก remove_first หรือเลื่อน _head โดยตรง
             แล้วคืน val
        """
        ####### IMPLEMENT HERE ########
        pass

    def peek(self) -> Any:
        """
        ดูค่า top โดยไม่เอาออก

        Returns
        -------
        Any  ค่าที่อยู่บน top

        Raises
        ------
        IndexError  ถ้า stack ว่าง

        คำใบ้: คล้าย pop แต่ไม่ต้องเอา node ออก
               แค่ return self._ll._head.data (หลังตรวจ empty)
        """
        ####### IMPLEMENT HERE ########
        pass

    # ----------------------------------------------------------
    # Method ที่เตรียมไว้แล้ว – ไม่ต้องแก้
    # ----------------------------------------------------------

    def __repr__(self) -> str:
        return f"StackLinkedList(top→{self._ll.to_list()})"


# =============================================================
# demo – รันเพื่อทดสอบ  (python stack_linkedlist.py)
# หมายเหตุ: ค่าที่แสดงจะเป็น None ก่อนที่นักศึกษาจะเติม method
# =============================================================

if __name__ == "__main__":
    # --- Demo 1: method ที่ใช้งานได้แล้ว ---
    print("=== Demo 1: __repr__ (pre-built) ===")
    s0 = StackLinkedList()
    s0._ll.addHead("A")
    s0._ll.addHead("B")
    s0._ll.addHead("C")
    # คาดหวัง: StackLinkedList(top→['C', 'B', 'A'])
    print("สร้าง stack ตรง ๆ ผ่าน _ll:", s0)

    # --- Demo 2: TODO methods ---
    print("\n=== Demo 2: TODO methods ===")
    s = StackLinkedList()

    # is_empty บน stack เปล่า (คาดหวัง True)
    print("[เริ่มต้น]  is_empty คาดหวัง True :", s.is_empty())

    # push แล้วดู peek / pop
    s.push("A")
    s.push("B")
    s.push("C")
    print("หลัง push A, B, C:", s)
    print("  peek  คาดหวัง 'C' :", s.peek())
    print("  pop   คาดหวัง 'C' :", s.pop())
    print("  pop   คาดหวัง 'B' :", s.pop())

    # pop จนว่าง แล้วทดสอบ IndexError
    s.pop()   # เอา A ออก
    try:
        s.pop()   # ควร raise IndexError
    except (IndexError, TypeError) as e:
        print("  IndexError จาก pop() บน stack ว่าง:", e)
    try:
        s.peek()  # ควร raise IndexError
    except (IndexError, TypeError) as e:
        print("  IndexError จาก peek() บน stack ว่าง:", e)
