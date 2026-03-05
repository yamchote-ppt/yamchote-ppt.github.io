# Lab 09: Stack & Queue Applications

**725103 Data Structures and Algorithms**
ภาคเรียนที่ 2/2568

แลปนี้เป็นการนำ **Stack** และ **Queue** ไปใช้กับงานจริง 2 แบบ:

* **Expression Evaluation** ด้วย **Stack**
* **Breadth-First Traversal (BFS) Job Sequencing** ด้วย **Queue**

ก่อนจะไปถึงจุดนั้น นักศึกษาจะได้ฝึกพื้นฐานที่จำเป็นก่อน ได้แก่:

* การใช้งาน **OOP ใน Python**
* การใช้งาน **LinkedList**
* การสร้าง **Stack** และ **Queue** ทั้งแบบ Array และแบบ LinkedList

---

## เป้าหมายของแลปนี้

เมื่อทำแลปนี้เสร็จ นักศึกษาควรจะสามารถ:

1. เข้าใจและใช้งานพื้นฐานของ **OOP** ใน Python ได้
2. ใช้งาน **LinkedList** ที่เตรียมไว้ให้ และเติม method ที่กำหนดได้
3. สร้าง **Stack** และ **Queue** ได้จากหลายแนวทาง
4. ใช้ **Stack** ในการคำนวณนิพจน์ทางคณิตศาสตร์
5. ใช้ **Queue** ในการทำ **BFS** เพื่อจัดลำดับการทำงาน

---

## โครงสร้างโปรเจกต์

โปรเจกต์นี้มีโครงสร้างประมาณนี้:

```text
lab09/
├─ src/
│  ├─ oop_basics.py
│  ├─ linked_list.py
│  ├─ stack_array.py
│  ├─ stack_linkedlist.py
│  ├─ queue_array.py
│  ├─ queue_linkedlist.py
│  ├─ expression_eval.py
│  └─ job_bfs.py
└─ report/
   └─ Lab09_Report.pdf
```

---

## สิ่งสำคัญที่ต้องเข้าใจก่อนเริ่ม

ไฟล์ในโปรเจกต์นี้เป็น **starter code** หรือโครงเริ่มต้น
นั่นหมายความว่า:

* มีบางส่วนที่อาจเขียนไว้ให้แล้ว
* มีบางส่วนที่นักศึกษาต้องเติมเอง
* จะมีจุดที่เว้นไว้ในรูปแบบนี้:

```python
####### IMPLEMENT HERE ########
pass
```

ส่วนที่มีรูปแบบนี้คือ **ส่วนที่นักศึกษาต้องเขียน logic เอง**

---

## งานที่ต้องทำ

## 1) OOP Warm-up

ไฟล์: `src/oop_basics.py`

ในไฟล์นี้จะมี class ตัวอย่าง เช่น:

* `Player`
* `Quest`
* `InventoryItem`

สิ่งที่ต้องทำ:

* ทดลองสร้าง object จาก class ที่ให้
* ทดลองเรียก method ที่มีอยู่
* ทำความเข้าใจความต่างระหว่าง:

  * class
  * object
  * attribute
  * method
* เติม logic ใน method ที่เว้นไว้ เช่น `gain_exp(...)`

จุดประสงค์ของส่วนนี้คือให้ทุกคนเริ่มใช้ class และ object ได้ก่อนเข้าสู่ data structure

---

## 2) LinkedList

ไฟล์: `src/linked_list.py`

ในไฟล์นี้จะมีโครงของ:

* `Node`
* `LinkedList`

สิ่งที่ควรลองก่อน:

* เพิ่มข้อมูลที่หัว (`addHead`)
* เพิ่มข้อมูลที่ท้าย (`addTail`)
* แปลง list ออกมาเป็น Python list (`to_list`)

สิ่งที่ต้องเติมเอง:

* `find(value)`
* `remove_first(value)`

ตรงนี้ต้องระวังกรณีขอบ เช่น:

* list ว่าง
* ค่าที่หาไม่เจอ
* ลบตัวแรก
* ลบตัวกลาง
* ลบตัวท้าย

---

## 3) Stack

## 3.1 Stack จาก Array

ไฟล์: `src/stack_array.py`

ให้สร้าง `StackArray` โดยใช้ Python `list` เป็น storage ภายใน

method ที่เกี่ยวข้อง:

* `push`
* `pop`
* `peek`
* `is_empty`
* `__len__`

แนวคิดสำคัญ:

* Stack ทำงานแบบ **LIFO** (Last In, First Out)

---

## 3.2 Stack จาก LinkedList

ไฟล์: `src/stack_linkedlist.py`

ให้สร้าง `StackLinkedList` โดยใช้ `LinkedList` ที่มีอยู่แล้ว

สิ่งที่ควรคิด:

* ควร push/pop ที่หัวหรือท้าย?
* ทำตรงไหนจึงจะเหมาะสมกว่าในเชิงประสิทธิภาพ?

---

## 4) Queue

## 4.1 Queue จาก Array

ไฟล์: `src/queue_array.py`

ให้สร้าง `QueueArray` โดยใช้ Python `list` ร่วมกับตัวชี้

* `front_index`
* `rear_index`

method ที่เกี่ยวข้อง:

* `enqueue`
* `dequeue`
* `peek`
* `is_empty`
* `__len__`

แนวคิดสำคัญ:

* Queue ทำงานแบบ **FIFO** (First In, First Out)

---

## 4.2 Queue จาก LinkedList

ไฟล์: `src/queue_linkedlist.py`

ส่วนนี้เป็นโครงเพิ่มเติม ให้ดูแนวคิดไว้ก่อน

สิ่งที่ควรคิด:

* Queue ควร enqueue ที่ท้าย
* Queue ควร dequeue ที่หัว

และลองพิจารณาว่า LinkedList แบบพื้นฐานที่มีอยู่ เหมาะกับ Queue แค่ไหน

---

## 5) ใช้ Stack ทำ Expression Evaluation

ไฟล์: `src/expression_eval.py`

โจทย์คือเขียนโปรแกรมเพื่อคำนวณนิพจน์ เช่น:

* `3 + 4 * 2`
* `(3 + 4) * 2`
* `10 / (5 - 3)`

แนวคิดหลักมี 2 ขั้นตอน:

1. แปลงจาก **infix** เป็น **postfix**
2. ประเมินค่า **postfix**

สิ่งที่ควรเข้าใจ:

* ทำไมต้องใช้ stack
* operator precedence คืออะไร
* วงเล็บมีผลอย่างไร

ในไฟล์นี้จะมีฟังก์ชันที่ต้องเกี่ยวข้อง เช่น:

* `tokenize(...)`
* `infix_to_postfix(...)`
* `eval_postfix(...)`
* `evaluate(...)`

บางส่วนจะมี TODO ให้นักศึกษาเติมเอง

---

## 6) ใช้ Queue ทำ BFS Job Sequencing

ไฟล์: `src/job_bfs.py`

ส่วนนี้เป็นการใช้ **Queue** เพื่อเดินแบบ **Breadth-First Search (BFS)**

แทนที่จะอธิบายเป็นกราฟโดยตรง ให้มองเป็นสถานการณ์แบบนี้:

* ทำงานหนึ่งเสร็จ
* จะปลดล็อกงานลูกต่อไป
* งานแตกแขนงออกไปเรื่อย ๆ
* ไม่มีการย้อนกลับมารวมกัน

โครงสร้างข้อมูลจะเก็บในรูปแบบ Python dictionary เช่น:

```python
quest_tree = {
    "Start": ["Q1", "Q2"],
    "Q1": ["Q1.1", "Q1.2"],
    "Q2": ["Q2.1"],
    "Q1.1": [],
    "Q1.2": ["Q1.2.1"],
    "Q2.1": [],
    "Q1.2.1": []
}
```

สิ่งที่ต้องทำคือเขียนฟังก์ชัน:

* `bfs_job_sequence(tree, start)`

เพื่อคืนลำดับการเดินแบบ BFS

---

## ลำดับการทำงานที่แนะนำ

แนะนำให้ทำตามลำดับนี้:

1. อ่าน `oop_basics.py` และลองรันดู
2. ทำความเข้าใจ `linked_list.py`
3. ทำ `stack_array.py`
4. ทำ `stack_linkedlist.py`
5. ทำ `queue_array.py`
6. ดู `queue_linkedlist.py`
7. ทำ `expression_eval.py`
8. ทำ `job_bfs.py`

ถ้าข้ามไปทำ application ก่อน ทั้งที่ Stack/Queue ยังไม่พร้อม จะทำให้สับสนง่าย

---

## สิ่งที่ต้องส่ง

นักศึกษาต้องส่ง 2 ส่วน:

1. โค้ดในโฟลเดอร์ `src/`
2. รายงาน `Lab09_Report.pdf`

---

## สิ่งที่ควรมีในรายงาน

รายงานควรมีอย่างน้อย:

### สำหรับ Expression Evaluation

* ตัวอย่างการแปลง **infix -> postfix**
* trace การคำนวณ postfix
* อธิบายสั้น ๆ ว่าทำไมโดยรวมเป็น `O(n)`

### สำหรับ BFS Job Sequencing

* วาด tree อย่างน้อย 1 ตัวอย่าง
* trace การทำงานของ queue อย่างน้อย 6 step
* อธิบายสั้น ๆ ว่า BFS มีแนวคิดเป็น `O(V + E)` และในกรณี tree มองได้เป็น `O(n)`

---

## คำแนะนำในการทำแลป

* อย่ารีบเขียนทุกอย่างรวดเดียว
* ลองทดสอบทีละ method
* ลองพิมพ์ค่าดูบ่อย ๆ เพื่อเช็กสถานะ
* ถ้าเจอ bug ให้ดูเคสง่ายที่สุดก่อน
* สำหรับ Stack/Queue ให้ลองเขียนตัวอย่างเล็ก ๆ ด้วยมือก่อน แล้วค่อยแปลงเป็นโค้ด

---

## ข้อควรระวัง

* อย่าแก้ชื่อ class / method โดยไม่จำเป็น
* อย่าลบ TODO placeholders ทิ้งก่อนเข้าใจว่าต้องทำอะไร
* ระวังกรณี list ว่าง
* ระวังการ pop/dequeue จากโครงสร้างที่ไม่มีข้อมูล
* ตรวจสอบว่า logic ของ Stack กับ Queue ไม่สลับกัน

---

## หมายเหตุ

แลปนี้ไม่ได้เน้น “เขียนให้สั้นที่สุด”
แต่เน้น:

* เข้าใจโครงสร้างข้อมูล
* เห็นการทำงานทีละขั้น
* อธิบายได้ว่าทำไมต้องใช้ Stack หรือ Queue

ดังนั้นขอให้เขียนแบบ **อ่านง่าย ตรวจง่าย และอธิบายตัวเองได้**