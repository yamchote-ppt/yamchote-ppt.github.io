# oop_basics.py
# Lab 09 – Section 1: พื้นฐาน OOP (Warm-up)
#
# แนวคิดหลัก (อ่านก่อนเริ่ม):
#   class     = พิมพ์เขียว  บอกว่า object ชนิดนี้มีอะไรบ้าง
#   object    = สิ่งที่สร้างจาก class เช่น  p = Player("Alice")
#   attribute = ข้อมูลที่เก็บใน object      เช่น  p.level, p.exp
#   method    = ฟังก์ชันที่ผูกกับ object    เช่น  p.show_status()
#               method รับ self เสมอ (self คือ object ตัวนั้นเอง)
#
# ไฟล์นี้มี 3 class ให้แล้ว:
#   - InventoryItem   → ของชิ้นหนึ่งในกระเป๋า
#   - Quest           → ภารกิจหนึ่งในเกม
#   - Player          → ผู้เล่น
#
# งาน 1.1 : สร้าง object อย่างน้อย 2 ตัวจากแต่ละ class และเรียกใช้ method ที่มีให้
# งาน 1.2 : เติม logic ใน Player.gain_exp() เพียงจุดเดียว


# =============================================================
# class InventoryItem – ของในกระเป๋า
# =============================================================

class InventoryItem:
    """
    แทนของชิ้นหนึ่งในกระเป๋าของผู้เล่น

    --- Attributes (ข้อมูลที่เก็บใน object) ---
        name     (str) : ชื่อของ          เช่น "Potion"
        quantity (int) : จำนวน            เช่น 5
        value    (int) : มูลค่าต่อชิ้น   เช่น 20

    --- Methods (สิ่งที่ object ทำได้) ---
        total_value()  → คืนมูลค่ารวม
        describe()     → คืนสตริงอธิบายของชิ้นนี้
    """

    def __init__(self, name: str, quantity: int, value: int) -> None:
        # self.xxx = yyy  คือการกำหนด attribute ให้ object
        self.name = name          # attribute: ชื่อของ
        self.quantity = quantity  # attribute: จำนวน
        self.value = value        # attribute: มูลค่าต่อชิ้น

    # --- methods ที่ทำงานได้แล้ว (ลองเรียกใช้และสังเกตผลลัพธ์) ---

    def total_value(self) -> int:
        """คืนมูลค่ารวม = quantity × value"""
        return self.quantity * self.value

    def describe(self) -> str:
        """คืนสตริงอธิบายของชิ้นนี้ในรูปแบบที่อ่านง่าย"""
        return f"{self.name} x{self.quantity}  (มูลค่ารวม {self.total_value()} G)"

    def __repr__(self) -> str:
        # __repr__ ใช้แสดงผลเมื่อ print() object โดยตรง
        return f"InventoryItem({self.name!r}, qty={self.quantity}, val={self.value})"


# =============================================================
# class Quest – ภารกิจ
# =============================================================

class Quest:
    """
    แทนภารกิจหนึ่งในเกม

    --- Attributes ---
        title       (str)  : ชื่อภารกิจ          เช่น "Defeat Slime"
        reward_exp  (int)  : EXP เมื่อทำเสร็จ    เช่น 30
        completed   (bool) : สถานะ               True = เสร็จแล้ว

    --- Methods ---
        complete()  → ทำภารกิจให้เสร็จ คืน EXP ที่ได้
        status()    → คืนสตริงแสดงสถานะปัจจุบัน
    """

    def __init__(self, title: str, reward_exp: int) -> None:
        self.title = title            # attribute: ชื่อภารกิจ
        self.reward_exp = reward_exp  # attribute: EXP รางวัล
        self.completed = False        # attribute: ยังไม่เสร็จตอนสร้าง

    # --- methods ที่ทำงานได้แล้ว ---

    def complete(self) -> int:
        """
        ทำภารกิจให้เสร็จ
        - คืน EXP ที่ได้  (ครั้งแรก)
        - คืน 0           (ถ้าเรียกซ้ำ — ไม่ได้ EXP สองรอบ)
        """
        if self.completed:
            return 0
        self.completed = True   # เปลี่ยน attribute จาก False → True
        return self.reward_exp

    def status(self) -> str:
        """คืนสตริงอธิบายสถานะปัจจุบันของภารกิจ"""
        state = "✓ เสร็จแล้ว" if self.completed else "○ ยังไม่เสร็จ"
        return f"[{state}] {self.title}  (รางวัล {self.reward_exp} EXP)"

    def __repr__(self) -> str:
        return (
            f"Quest({self.title!r}, "
            f"reward={self.reward_exp}, "
            f"completed={self.completed})"
        )


# =============================================================
# class Player – ผู้เล่น
# =============================================================

class Player:
    """
    แทนผู้เล่นในเกม

    --- Attributes ---
        name      (str)                : ชื่อผู้เล่น
        level     (int)                : เลเวลปัจจุบัน  (เริ่มที่ 1)
        exp       (int)                : EXP ที่สะสมไว้
        hp        (int)                : HP ปัจจุบัน    (เริ่มที่ 100)
        inventory (list[InventoryItem]): ของในกระเป๋า

    --- Methods ที่เตรียมไว้แล้ว ---
        show_status()    → พิมพ์สถานะทั้งหมด
        pick_up(item)    → หยิบของเข้ากระเป๋า
        heal(amount)     → ฟื้น HP (ดู pattern ก่อนทำ gain_exp)

    --- Method ที่นักศึกษาต้องเติม ---
        gain_exp(amount) → เพิ่ม EXP และ level up ถ้าครบ threshold
    """

    EXP_THRESHOLD: int = 100  # class attribute: EXP ที่ต้องสะสมเพื่อ level up
                               # ค่านี้เหมือนกันทุก Player object

    def __init__(self, name: str) -> None:
        self.name = name                          # attribute: ชื่อผู้เล่น
        self.level: int = 1                       # attribute: เลเวลเริ่มต้น
        self.exp: int = 0                         # attribute: EXP เริ่มต้น
        self.hp: int = 100                        # attribute: HP เริ่มต้น
        self.inventory: list[InventoryItem] = []  # attribute: กระเป๋า (ว่างเปล่า)

    # ----------------------------------------------------------
    # methods ที่ทำไว้ให้แล้ว (อ่าน–เรียกใช้–สังเกต ก่อนทำงาน 1.2)
    # ----------------------------------------------------------

    def show_status(self) -> None:
        """พิมพ์ค่า attribute ทั้งหมดของผู้เล่นคนนี้"""
        print(f"--- {self.name} ---")
        print(f"  Level    : {self.level}")
        print(f"  EXP      : {self.exp}/{self.EXP_THRESHOLD}")
        print(f"  HP       : {self.hp}")
        item_names = [item.name for item in self.inventory]
        print(f"  Inventory: {item_names}")

    def pick_up(self, item: InventoryItem) -> None:
        """หยิบของเข้ากระเป๋า (เพิ่ม item เข้า list inventory)"""
        self.inventory.append(item)
        print(f"  {self.name} หยิบ {item.name} เข้ากระเป๋า")

    def heal(self, amount: int) -> None:
        """
        ฟื้น HP โดยให้ HP ไม่เกิน 100

        *** ศึกษา pattern ของ method นี้ก่อนเขียน gain_exp ***
        สังเกต:
          1. ตรวจ input ก่อน (amount < 0 → ออกทันที)
          2. ปรับ attribute (self.hp)
          3. แสดงผล
        """
        if amount < 0:
            return                                  # input ไม่ถูกต้อง ไม่ทำอะไร
        self.hp = min(100, self.hp + amount)        # HP ต้องไม่เกิน 100
        print(f"  {self.name} ฟื้น {amount} HP  (HP ตอนนี้: {self.hp})")

    # ----------------------------------------------------------
    # method ที่นักศึกษาต้องเติม – งาน 1.2
    # ----------------------------------------------------------

    def gain_exp(self, amount: int) -> None:
        """
        เพิ่ม EXP ให้ผู้เล่น

        เงื่อนไข:
          - EXP ต้องไม่ติดลบ  (จัดการกรณี amount เป็นลบด้วย)
          - ถ้า EXP >= EXP_THRESHOLD → level +1 และลด EXP ลงตาม threshold
          - วนซ้ำได้ถ้า EXP ที่เหลือยังถึง threshold อีก

        ตัวอย่างผลที่คาดหวัง (EXP_THRESHOLD = 100):
          gain_exp(80)  → Level 1, EXP 80
          gain_exp(50)  → Level 2, EXP 30   (80+50=130 → level up, เหลือ 30)
          gain_exp(250) → Level 4, EXP 80   (30+250=280 → level up 2 ครั้ง)
        """
        ####### IMPLEMENT HERE ########
        pass


# =============================================================
# demo – รันเมื่อเรียกไฟล์นี้โดยตรง
# =============================================================

if __name__ == "__main__":
    # ================================================================
    # Demo 1: InventoryItem
    #   สังเกต: สร้าง object 2 ตัวจาก class เดียวกัน → ข้อมูลแยกกัน
    # ================================================================
    print("=" * 50)
    print("Demo 1: InventoryItem")
    print("=" * 50)

    sword  = InventoryItem("Sword",  1, 150)   # object ตัวที่ 1
    potion = InventoryItem("Potion", 5,  20)   # object ตัวที่ 2

    # เรียก method describe() → ใช้ attribute ภายในตัวมันเอง
    print(sword.describe())
    print(potion.describe())

    # เข้าถึง attribute โดยตรง
    print(f"  sword.name     = {sword.name}")
    print(f"  potion.quantity = {potion.quantity}")

    # ================================================================
    # Demo 2: Quest
    #   สังเกต: attribute 'completed' เปลี่ยนได้ด้วย method complete()
    # ================================================================
    print()
    print("=" * 50)
    print("Demo 2: Quest")
    print("=" * 50)

    q1 = Quest("Defeat Slime",   30)
    q2 = Quest("Explore Forest", 50)

    # [ก่อน] สถานะยังไม่เสร็จ
    print("[ก่อน complete()]")
    print(" ", q1.status())
    print(" ", q2.status())

    # เรียก complete() → เปลี่ยน attribute completed จาก False → True
    gained = q1.complete()
    print(f"\n  ทำ '{q1.title}' เสร็จ ได้ {gained} EXP")

    # [หลัง] สถานะเปลี่ยนแล้ว
    print("[หลัง complete()]")
    print(" ", q1.status())
    print(f"  ทำซ้ำ → ได้ {q1.complete()} EXP  (ต้องได้ 0 ไม่เคาะสองรอบ)")

    # ================================================================
    # Demo 3: Player
    #   สังเกต: method heal() เป็นตัวอย่างที่สมบูรณ์ก่อนทำ gain_exp
    # ================================================================
    print()
    print("=" * 50)
    print("Demo 3: Player")
    print("=" * 50)

    p = Player("Alice")

    print("[สร้าง Player ใหม่]")
    p.show_status()

    # pick_up → เพิ่มของเข้า inventory
    print()
    p.pick_up(sword)
    p.pick_up(potion)

    # heal → ตัวอย่าง method ที่เสร็จแล้ว ดู pattern ก่อนทำ gain_exp
    p.hp = 55
    print(f"\n[ลด HP เหลือ {p.hp}]")
    p.heal(30)    # → 85
    p.heal(30)    # → 100 (ไม่เกิน 100)

    # gain_exp – นักศึกษาต้องเติม logic ก่อน ผลลัพธ์จึงจะถูก
    print()
    print("[ทดสอบ gain_exp – ต้องเติม logic ก่อน]")
    p.show_status()

    p.gain_exp(80)
    print("\n  หลัง gain_exp(80)   → คาดหวัง: Level 1, EXP  80")
    p.show_status()

    p.gain_exp(50)
    print("\n  หลัง gain_exp(50)   → คาดหวัง: Level 2, EXP  30")
    p.show_status()

    p.gain_exp(250)
    print("\n  หลัง gain_exp(250)  → คาดหวัง: Level 4, EXP  80")
    p.show_status()
