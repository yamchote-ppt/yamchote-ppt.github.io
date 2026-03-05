# linked_list.py
# Lab 09 – Section 2: Singly Linked List
#
# โครงสร้างข้อมูล linked list ใช้ Node เป็นหน่วยเล็กสุด
# แต่ละ Node เก็บ:
#   data  → ค่าข้อมูล
#   next  → pointer ชี้ไปโหนดถัดไป (None ถ้าเป็น Node สุดท้าย)
#
# LinkedList ถือ pointer เดียวคือ _head (ชี้ Node แรก)
# การ traverse ทำโดย  current = current.next  วนจนถึง None
#
# งาน 2.1 : ทดลองใช้ addHead, addTail, to_list ที่ทำให้แล้ว
# งาน 2.2 : เติม find(value) และ remove_first(value)

from __future__ import annotations
from typing import Any


# =============================================================
# class Node – โหนดหนึ่งตัวใน linked list
# =============================================================

class Node:
    """
    โหนดหนึ่งตัวใน singly linked list

    Attributes:
        data (Any)       : ค่าข้อมูลที่เก็บในโหนดนี้
        next (Node|None) : pointer ชี้ไปโหนดถัดไป
                           (None หมายถึงโหนดนี้เป็นโหนดสุดท้าย)
    """

    def __init__(self, data: Any) -> None:
        self.data = data               # เก็บค่าข้อมูล
        self.next: Node | None = None  # ยังไม่มีโหนดถัดไป

    def __repr__(self) -> str:
        return f"Node({self.data!r})"


# =============================================================
# class LinkedList – singly linked list
# =============================================================

class LinkedList:
    """
    Singly linked list แบบง่าย สำหรับ Lab 09

    --- Attributes (internal) ---
        _head (Node|None) : pointer ชี้โหนดแรก  (None = list ว่าง)
        _size (int)       : จำนวนโหนดทั้งหมด

    --- Methods ที่เตรียมไว้แล้ว ---
        is_empty()            → ตรวจว่า list ว่างหรือไม่
        __len__()             → คืนจำนวนโหนด
        addHead(data)         → เพิ่มโหนดที่หัว
        addTail(data)         → เพิ่มโหนดที่หาง
        to_list()             → แปลงเป็น Python list เพื่อแสดงผล

    --- Methods ที่นักศึกษาต้องเติม ---
        find(value)           → หา index ของโหนดที่มีค่าตรงกัน
        remove_first(value)   → ลบโหนดแรกที่มีค่าตรงกัน
    """

    def __init__(self) -> None:
        self._head: Node | None = None  # pointer ชี้โหนดแรก
        self._size: int = 0             # จำนวนโหนดใน list

    # ----------------------------------------------------------
    # methods ที่เตรียมไว้แล้ว (ศึกษา pattern การ traverse)
    # ----------------------------------------------------------

    def is_empty(self) -> bool:
        """คืน True ถ้า list ว่าง (ไม่มีโหนดเลย)"""
        return self._head is None

    def __len__(self) -> int:
        """คืนจำนวนโหนดทั้งหมดใน list"""
        return self._size

    def addHead(self, data: Any) -> None:
        """
        เพิ่มโหนดใหม่ที่หัว list (O(1))

        ขั้นตอน:
          1. สร้าง Node ใหม่
          2. ให้ new_node.next ชี้ไป _head เดิม
          3. เลื่อน _head มาชี้ new_node
        """
        new_node = Node(data)
        new_node.next = self._head  # เชื่อมต่อกับ list เดิม
        self._head = new_node       # เลื่อน head มาชี้โหนดใหม่
        self._size += 1

    def addTail(self, data: Any) -> None:
        """
        เพิ่มโหนดใหม่ที่หาง list (O(n))

        ขั้นตอน:
          1. สร้าง Node ใหม่
          2. ถ้า list ว่าง → new_node กลายเป็น head
          3. ถ้าไม่ว่าง → traverse จนถึงโหนดสุดท้าย แล้วเชื่อมต่อ

        *** pattern การ traverse นี้ใช้ใน find และ remove_first ด้วย ***
        """
        new_node = Node(data)
        if self._head is None:
            # list ยังว่างอยู่ → โหนดใหม่คือหัว
            self._head = new_node
        else:
            # เดินไปจนถึงโหนดสุดท้าย (current.next is None)
            current = self._head
            while current.next is not None:
                current = current.next  # เลื่อนไปโหนดถัดไป
            current.next = new_node     # เชื่อมโหนดใหม่ต่อท้าย
        self._size += 1

    def to_list(self) -> list[Any]:
        """
        แปลง linked list เป็น Python list
        ใช้เพื่อแสดงผลหรือทดสอบ
        """
        result = []
        current = self._head
        while current is not None:
            result.append(current.data)
            current = current.next  # เลื่อนไปโหนดถัดไป
        return result

    def __repr__(self) -> str:
        return f"LinkedList({self.to_list()})"

    # ----------------------------------------------------------
    # methods ที่นักศึกษาต้องเติม – งาน 2.2
    # ----------------------------------------------------------

    def find(self, value: Any) -> int:
        """
        หาโหนดแรกที่มีค่าเท่ากับ value

        คืนค่า:
            index (int, 0-based) ถ้าพบ
            -1                   ถ้าไม่พบ

        กรณีขอบที่ต้องจัดการ:
            - list ว่าง → คืน -1 ทันที

        แนวคิด:
            - ใช้ตัวนับ index เพิ่มขึ้นทุกครั้งที่เลื่อน current
            - ดู pattern การ traverse ใน addTail เพื่อเป็นแนวทาง
        """
        ####### IMPLEMENT HERE ########
        pass

    def remove_first(self, value: Any) -> bool:
        """
        ลบโหนดแรกที่มีค่าเท่ากับ value

        คืนค่า:
            True   ถ้าลบสำเร็จ
            False  ถ้าไม่พบ value ใน list

        กรณีขอบที่ต้องจัดการทั้งหมด:
            1. list ว่าง           → คืน False ทันที
            2. ลบโหนดที่หัว        → เลื่อน _head ไปโหนดถัดไป
            3. ลบโหนดที่กลาง/ท้าย → ให้ prev.next ข้ามโหนดที่จะลบ

        แนวคิด:
            - เก็บ prev (โหนดก่อนหน้า) ไว้ด้วยขณะ traverse
            - แล้วใช้  prev.next = current.next  เพื่อตัดโหนดออก
        """
        ####### IMPLEMENT HERE ########
        pass


# =============================================================
# demo
# =============================================================

if __name__ == "__main__":
    # ================================================================
    # Demo 1: ทดสอบ methods ที่ทำไว้ให้แล้ว
    # ================================================================
    print("=" * 50)
    print("Demo 1: addHead / addTail / to_list")
    print("=" * 50)

    ll = LinkedList()
    print("[เริ่มต้น]  is_empty =", ll.is_empty(), " to_list =", ll.to_list())

    ll.addTail(10)
    ll.addTail(20)
    ll.addTail(30)
    print("หลัง addTail(10, 20, 30):", ll.to_list())

    ll.addHead(5)
    print("หลัง addHead(5)        :", ll.to_list())
    print("ขนาด (len)             :", len(ll))   # 4

    # ================================================================
    # Demo 2: ทดสอบ find และ remove_first
    #         (นักศึกษาต้องเติม logic ก่อน ผลจึงจะถูกต้อง)
    # ================================================================
    print()
    print("=" * 50)
    print("Demo 2: find / remove_first  [ต้องเติม logic ก่อน]")
    print("=" * 50)
    print("list ปัจจุบัน:", ll.to_list())   # [5, 10, 20, 30]

    # --- find ---
    print("\n  find(20)  คาดหวัง  2 :", ll.find(20))
    print("  find(5)   คาดหวัง  0 :", ll.find(5))
    print("  find(99)  คาดหวัง -1 :", ll.find(99))

    # --- remove_first: กรณีปกติ ---
    print("\n  remove_first(20)  คาดหวัง True  :", ll.remove_first(20))
    print("  list หลังลบ 20   :", ll.to_list())   # [5, 10, 30]

    # --- remove_first: ลบที่หัว ---
    print("\n  remove_first(5)   คาดหวัง True  :", ll.remove_first(5))
    print("  list หลังลบ 5    :", ll.to_list())   # [10, 30]

    # --- remove_first: ไม่พบ ---
    print("\n  remove_first(99)  คาดหวัง False :", ll.remove_first(99))

    # --- find บน list ว่าง ---
    empty_ll = LinkedList()
    print("\n  find(10) บน list ว่าง  คาดหวัง -1 :", empty_ll.find(10))
