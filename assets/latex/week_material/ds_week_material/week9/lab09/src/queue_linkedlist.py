# queue_linkedlist.py
# ============================================================
# Lab 09 – ส่วนที่ 4.2  Queue จาก LinkedList  (ส่วนเสริม)
# ============================================================
#
# ** ทำหลังจากส่วน 4.1 เสร็จแล้ว **
#
# แนวคิด: ใช้ LinkedList แทน array เป็น storage ภายใน
#   - dequeue ที่หัว (head)  → O(1)  เพราะเราเก็บ _head ไว้อยู่แล้ว
#   - enqueue ที่หาง (tail)  → O(n)  ถ้าต้อง traverse ทุกครั้ง !
#
# ปัญหาของ LinkedList ธรรมดา:
#   ไม่มี pointer ชี้ tail โดยตรง
#   ทำให้ enqueue ต้อง traverse ยาว O(n) ก่อนถึงหาง
#
# แนวทางปรับปรุง (ท้องท้าทาย):
#   เพิ่ม _tail pointer ใน __init__ แล้วอัพเดทเมื่อ enqueue ทุกครั้ง
#   → enqueue กลายเป็น O(1)
#
# งานนักศึกษา: เติม method ทั้ง 5 ใน class QueueLinkedList
# ============================================================

from linked_list import LinkedList
from typing import Any


class QueueLinkedList:
    """
    Queue ADT ที่ใช้ LinkedList เป็น storage ภายใน  (ส่วนเสริม)

    Attributes ภายใน
    -----------------
    _ll : LinkedList
        LinkedList ที่ใช้เก็บข้อมูล
        head = หัว queue  (dequeue ออกจากนี่)
        tail = หาง queue  (enqueue เพิ่มที่นี่)

    หมายเหตุ: อาจต้องเพิ่ม _tail pointer เพื่อให้ enqueue เป็น O(1)

    Methods ที่ใช้งานได้แล้ว
    -------------------------
    __repr__  คืน string แสดงสถานะ queue

    Methods ที่นักศึกษาต้องเติม (ทั้งหมด 5 method)
    -------------------------------------------------
    is_empty()    คืน True ถ้า queue ว่าง
    __len__()     คืนจำนวน element ใน queue
    enqueue(x)    เพิ่ม x เข้าทางหาง
    dequeue()     นำ element จากหัวออกและคืนค่า ; raise IndexError ถ้าว่าง
    peek()        ดูหัว queue โดยไม่เอาออก ; raise IndexError ถ้าว่าง
    """

    def __init__(self) -> None:
        self._ll = LinkedList()   # head = front, tail = rear

    # ----------------------------------------------------------
    # Methods ที่นักศึกษาต้องเติม
    # ----------------------------------------------------------

    def is_empty(self) -> bool:
        """
        คืน True ถ้า queue ว่าง

        คำใบ้: ตรวจ self._ll._head ว่าเป็น None หรือไม่
        """
        ####### IMPLEMENT HERE ########
        pass

    def __len__(self) -> int:
        """
        คืนจำนวน element ใน queue  (ต้อง return เป็น int เสมอ)

        คำใบ้: traverse LinkedList และนับ node
               ดูรูปแบบ traverse ได้จาก addTail / find ใน linked_list.py
        """
        ####### IMPLEMENT HERE ########
        pass

    def enqueue(self, x: Any) -> None:
        """
        เพิ่ม x เข้าทางหาง queue

        คำใบ้: ใช้ addTail ของ LinkedList (เรียบง่ายแต่ O(n))
               *** ส่วนเสริม ***: ถ้าเพิ่ม _tail pointer ใน __init__
               ก็ต่อ node ใหม่เข้าหาง O(1) ได้เลย
        """
        ####### IMPLEMENT HERE ########
        pass

    def dequeue(self) -> Any:
        """
        นำ element จากหัว queue ออกและคืนค่า

        Returns
        -------
        Any  ค่าที่อยู่หัว queue ก่อนถูกนำออก

        Raises
        ------
        IndexError  ถ้า queue ว่าง

        คำใบ้: คล้าย pop() ใน StackLinkedList
          1. ตรวจ empty → raise IndexError ถ้าว่าง
          2. val = self._ll._head.data
          3. เลื่อน _head ออก (remove_first หรือเลื่อน _head โดยตรง)
          4. คืน val
        """
        ####### IMPLEMENT HERE ########
        pass

    def peek(self) -> Any:
        """
        ดูค่าหัว queue โดยไม่เอาออก

        Returns
        -------
        Any  ค่าที่อยู่หัว queue

        Raises
        ------
        IndexError  ถ้า queue ว่าง

        คำใบ้: return self._ll._head.data หลังตรวจ empty
        """
        ####### IMPLEMENT HERE ########
        pass

    # ----------------------------------------------------------
    # Method ที่เตรียมไว้แล้ว – ไม่ต้องแก้
    # ----------------------------------------------------------

    def __repr__(self) -> str:
        return f"QueueLinkedList(front→{self._ll.to_list()}←rear)"


# =============================================================
# demo – รันเพื่อทดสอบ  (python queue_linkedlist.py)
# หมายเหตุ: ค่าที่แสดงจะเป็น None ก่อนที่นักศึกษาจะเติม method
# =============================================================

if __name__ == "__main__":
    q = QueueLinkedList()

    # is_empty บน queue เปล่า (คาดหวัง True)
    print("[เริ่มต้น]  is_empty คาดหวัง True :", q.is_empty())

    # enqueue แล้วดู dequeue
    q.enqueue("A")
    q.enqueue("B")
    q.enqueue("C")
    print("หลัง enqueue A, B, C:", q)
    print("  peek     คาดหวัง 'A' :", q.peek())
    print("  dequeue  คาดหวัง 'A' :", q.dequeue())
    print("  dequeue  คาดหวัง 'B' :", q.dequeue())

    # dequeue จนว่าง แล้วทดสอบ IndexError
    q.dequeue()   # เอา C ออก
    try:
        q.dequeue()   # ควร raise IndexError
    except (IndexError, TypeError) as e:
        print("  IndexError จาก dequeue() บน queue ว่าง:", e)
    try:
        q.peek()      # ควร raise IndexError
    except (IndexError, TypeError) as e:
        print("  IndexError จาก peek() บน queue ว่าง:", e)
