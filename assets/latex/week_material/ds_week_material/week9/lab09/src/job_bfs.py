# job_bfs.py
# ============================================================
# Lab 09 – ส่วนที่ 6  Job Sequencing ด้วย BFS และ Queue
# ============================================================
#
# แนวคิด: BFS (Breadth-First Search)
#   เยี่ยม node ทีละ "ระดับ" ก่อนลึกลงไปถัดไป
#   → เหมาะกับการจัดลำดับ quest ที่ต้องทำก่อน–หลัง
#
#   กุญแจสำคัญ: ใช้ Queue  (FIFO)  เป็นโครงสร้างหลัก
#   (DFS ใช้ Stack / Recursion  —  BFS ใช้ Queue)
#
# โครงสร้างข้อมูล quest tree:
#   ใช้ Python dict  →  { node_name: [child1, child2, ...] }
#
# ตัวอย่าง quest_tree และ BFS order:
#
#                 Start
#                /     \
#              Q1        Q2
#             /  \         \
#          Q1.1  Q1.2      Q2.1
#                   \
#                 Q1.2.1
#
#   BFS order: Start → Q1 → Q2 → Q1.1 → Q1.2 → Q2.1 → Q1.2.1
#   (เยี่ยม level 0 ก่อน, แล้ว level 1, แล้ว level 2, ...)
#
# โครงสร้างที่ใช้:  QueueArray  (ที่นักศึกษาเขียนเองในส่วน 4.1)
#
# งานนักศึกษา: เติม bfs_job_sequence ใน function ด้านล่าง
# ============================================================

import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from queue_array import QueueArray


# ตัวอย่าง quest tree (ใช้ทดสอบ – เตรียมไว้แล้ว)
quest_tree: dict[str, list[str]] = {
    "Start":  ["Q1", "Q2"],
    "Q1":     ["Q1.1", "Q1.2"],
    "Q2":     ["Q2.1"],
    "Q1.1":   [],
    "Q1.2":   ["Q1.2.1"],
    "Q2.1":   [],
    "Q1.2.1": [],
}


def bfs_job_sequence(
    tree: dict[str, list[str]],
    start: str,
) -> list[str]:
    """
    คืนลำดับการทำงานแบบ BFS โดยเริ่มจาก start
    ใช้ QueueArray ที่นักศึกษาสร้างเอง

    Parameters
    ----------
    tree  : dict ของ { node_name: [children] }
    start : ชื่อ node เริ่มต้น

    Returns
    -------
    list[str]  ลำดับ node ที่เยี่ยมตามแบบ BFS

    อัลกอริทึม BFS  (3 ขั้นหลัก):
      1. enqueue start node เข้า queue

      2. วนซ้ำ จนกว่า queue จะว่าง:
           a. dequeue node หน้าสุดออกมา  (เรียกว่า current)
           b. เพิ่ม current เข้า order
           c. enqueue ลูกทุกตัวของ current เข้า queue
              คำใบ้: ลูก = tree[current]  →  วน for loop แล้ว enqueue แต่ละตัว

      3. คืน order

    *** สำคัญ: ต้องเรียก is_empty(), enqueue(), dequeue() ผ่าน QueueArray ***
    """
    q = QueueArray()    # ต้องใช้ QueueArray ที่นักศึกษาสร้างเอง
    order: list[str] = []

    ####### IMPLEMENT HERE ########

    return order


# =============================================================
# demo – รันเพื่อทดสอบ  (python job_bfs.py)
# หมายเหตุ: ผลจะแสดง ✗ ก่อนที่นักศึกษาจะเติม logic ทั้งใน
#           bfs_job_sequence  และ  QueueArray
# =============================================================

if __name__ == "__main__":
    expected = ["Start", "Q1", "Q2", "Q1.1", "Q1.2", "Q2.1", "Q1.2.1"]

    try:
        result = bfs_job_sequence(quest_tree, "Start")
        print("ลำดับ BFS :", result)
        print("คาดหวัง   :", expected)
        if result == expected:
            print("✓ ถูกต้อง!")
        else:
            print("✗ ยังไม่ถูกต้อง — ตรวจสอบ logic ของ bfs_job_sequence และ QueueArray")
    except Exception as e:
        print("! error:", e)
