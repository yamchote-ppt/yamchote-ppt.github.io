# queue_array.py
# ============================================================
# Lab 09 – ส่วนที่ 4.1  Queue จาก Array
# ============================================================
#
# แนวคิด: Queue = โครงสร้าง FIFO (First In First Out)
#   "person เข้าคิวก่อน ออกก่อน"
#
#   ใน lab นี้เราใช้ Python list เป็น storage ภายใน
#   ร่วมกับ index สองตัวที่ชี้ตำแหน่งหัวและหาง
#
# การออกแบบ index:
#   _front_index  ชี้ที่ element แรกที่จะ dequeue  (หัว queue)
#   _rear_index   ชี้ที่ตำแหน่ง "ถัดจาก" element สุดท้าย (หลัง rear)
#
#   สถานะ queue ว่าง:   _front_index == _rear_index
#   จำนวน element:      _rear_index – _front_index
#
# ข้อสังเกต (naive implementation):
#   ทุกครั้งที่ dequeue, _front_index เลื่อนไปข้างหน้า 1 ช่อง
#   ส่วนหน้าของ _data จะกลายเป็น "cell ว่าง" ที่ไม่ถูกใช้อีก
#   → ใช้งานได้แต่สิ้นเปลือง memory ถ้าทำงานนานมาก
#
# งานนักศึกษา: เติม method ทั้ง 5 ใน class QueueArray
# ============================================================

from typing import Any


class QueueArray:
    """
    Queue ADT ที่ใช้ list + front/rear index

    Attributes ภายใน
    -----------------
    _data         : list[Any]
        array เก็บข้อมูล (ขยายได้ไปเรื่อย ๆ ด้วย append)
    _front_index  : int
        index ของ element แรกใน _data ที่ยังอยู่ใน queue (หัว)
    _rear_index   : int
        index ถัดจาก element สุดท้าย (ใช้ตรวจ empty และนับ size)

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
        self._data: list[Any] = []  # storage ภายใน
        self._front_index: int = 0  # ชี้ element แรก (หัว)
        self._rear_index: int = 0   # ชี้ตำแหน่งถัดจากหาง

    # ----------------------------------------------------------
    # Methods ที่นักศึกษาต้องเติม
    # ----------------------------------------------------------

    def is_empty(self) -> bool:
        """
        คืน True ถ้า queue ว่าง  (ไม่มี element เลย)

        คำใบ้: queue ว่าง ↔ หัวและหางอยู่ที่ตำแหน่งเดียวกัน
               เปรียบเทียบ  _front_index  กับ  _rear_index
        """
        ####### IMPLEMENT HERE ########
        pass

    def __len__(self) -> int:
        """
        คืนจำนวน element ใน queue  (ต้อง return เป็น int เสมอ)

        คำใบ้: ระยะห่างระหว่าง front และ rear คือจำนวน element ทั้งหมด
               _rear_index – _front_index
        """
        ####### IMPLEMENT HERE ########
        pass

    def enqueue(self, x: Any) -> None:
        """
        เพิ่ม x เข้าทางหาง queue  (ต่อคิว = เข้าจากหลัง)

        คำใบ้ (2 ขั้น):
          1. append x เข้า self._data       → เพิ่ม x ที่หลัง array
          2. เลื่อน _rear_index ขึ้น 1      → อัพเดทตำแหน่งหาง
        """
        ####### IMPLEMENT HERE ########
        pass

    def dequeue(self) -> Any:
        """
        นำ element จากหัว queue ออกและคืนค่า  (ออกก่อน = ออกจากหน้า)

        Returns
        -------
        Any  ค่าที่อยู่หัว queue ก่อนถูกนำออก

        Raises
        ------
        IndexError  ถ้า queue ว่าง

        คำใบ้ (3 ขั้น):
          1. ตรวจว่า queue ว่างหรือไม่ → ถ้าว่าง raise IndexError
          2. เก็บค่าหัว:  val = self._data[self._front_index]
          3. เลื่อน _front_index ขึ้น 1 แล้วคืน val
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

        คำใบ้: คล้าย dequeue แต่ไม่ต้องเลื่อน _front_index
               แค่ return self._data[self._front_index] (หลังตรวจ empty)
        """
        ####### IMPLEMENT HERE ########
        pass

    # ----------------------------------------------------------
    # Method ที่เตรียมไว้แล้ว – ไม่ต้องแก้
    # ----------------------------------------------------------

    def __repr__(self) -> str:
        active = self._data[self._front_index:self._rear_index]
        return f"QueueArray(front→{active}←rear)"


# =============================================================
# demo – รันเพื่อทดสอบ  (python queue_array.py)
# หมายเหตุ: ค่าที่แสดงจะเป็น None ก่อนที่นักศึกษาจะเติม method
# =============================================================

if __name__ == "__main__":
    q = QueueArray()

    # is_empty บน queue เปล่า (คาดหวัง True)
    print("[เริ่มต้น]  is_empty คาดหวัง True :", q.is_empty())

    # enqueue แล้วดู peek / dequeue
    q.enqueue("job1")
    q.enqueue("job2")
    q.enqueue("job3")
    print("หลัง enqueue job1, job2, job3:", q)
    print("  peek     คาดหวัง 'job1' :", q.peek())
    print("  dequeue  คาดหวัง 'job1' :", q.dequeue())
    print("  dequeue  คาดหวัง 'job2' :", q.dequeue())

    # dequeue จนว่าง แล้วทดสอบ IndexError
    q.dequeue()   # เอา job3 ออก
    try:
        q.dequeue()   # ควร raise IndexError
    except (IndexError, TypeError) as e:
        print("  IndexError จาก dequeue() บน queue ว่าง:", e)
    try:
        q.peek()      # ควร raise IndexError
    except (IndexError, TypeError) as e:
        print("  IndexError จาก peek() บน queue ว่าง:", e)
