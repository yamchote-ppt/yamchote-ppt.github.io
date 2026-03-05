# expression_eval.py
# ============================================================
# Lab 09 – ส่วนที่ 5  Expression Evaluation ด้วย Stack
# ============================================================
#
# แนวทาง 2 ขั้น:
#
#   ขั้น 1: infix → postfix  (Shunting-Yard algorithm)
#     ตัวอย่าง:  "3 + 4 * 2"  →  ["3", "4", "2", "*", "+"]
#     เหตุผล:    postfix ไม่มีวงเล็บ  →  ประเมินค่าได้ง่ายกว่า
#
#   ขั้น 2: ประเมินค่า postfix  (value stack)
#     - อ่านทีละ token
#     - ถ้าเป็นตัวเลข → push
#     - ถ้าเป็น operator → pop สองตัว คำนวณ แล้ว push ผลลัพธ์
#
# โครงสร้างที่ใช้:  StackArray  (ที่นักศึกษาเขียนเองในส่วน 3.1)
#
# ตาราง precedence:
#   * /  → 2   (precedence สูง)
#   + -  → 1   (precedence ต่ำ)
#
# งานนักศึกษา: เติม infix_to_postfix  และ  eval_postfix
# ============================================================

import sys
import os

# รองรับการ import เมื่อรันจากโฟลเดอร์ src/ หรือระดับบน
sys.path.insert(0, os.path.dirname(__file__))

from stack_array import StackArray

# ตาราง precedence ของ operator (เตรียมไว้แล้ว – ใช้ได้เลย)
PRECEDENCE: dict[str, int] = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}


def tokenize(expr: str) -> list[str]:
    """
    แยกนิพจน์ infix ออกเป็น list ของ token  (เตรียมไว้แล้ว – ไม่ต้องแก้)

    รองรับ: จำนวนเต็ม/ทศนิยม, +, -, *, /, (, ), ช่องว่าง

    ตัวอย่าง:
        "(3 + 4) * 2"  →  ["(", "3", "+", "4", ")", "*", "2"]
    """
    tokens: list[str] = []
    i = 0
    while i < len(expr):
        ch = expr[i]
        if ch.isspace():
            i += 1
            continue
        if ch in "+-*/()":
            tokens.append(ch)
            i += 1
        elif ch.isdigit() or ch == ".":
            # อ่านตัวเลขทั้งหมด (อาจเป็นทศนิยม)
            j = i
            while j < len(expr) and (expr[j].isdigit() or expr[j] == "."):
                j += 1
            tokens.append(expr[i:j])
            i = j
        else:
            raise ValueError(f"อักขระที่ไม่รู้จัก: {ch!r}")
    return tokens


def infix_to_postfix(tokens: list[str]) -> list[str]:
    """
    แปลง list of tokens จาก infix เป็น postfix  (Shunting-Yard algorithm)
    ใช้ StackArray เป็น operator stack

    Returns
    -------
    list[str]  list ของ token ที่เรียงลำดับแบบ postfix

    Shunting-Yard algorithm (แบบย่อ – ไม่มี ^ และ right-associativity):

      สำหรับแต่ละ token:
        ก. ถ้าเป็นตัวเลข
             → ส่งตรงเข้า output  (output.append(tok))
        ข. ถ้าเป็น operator (+, -, *, /)
             → pop operator ที่อยู่บน op_stack ออกจนกว่า:
                 - op_stack ว่าง  หรือ
                 - top เป็น '('  หรือ
                 - precedence ของ top < precedence ของ tok ปัจจุบัน
               แล้วจึง push tok ลง op_stack
               คำใบ้: PRECEDENCE[tok]  ดู precedence จากตาราง
        ค. ถ้าเป็น '('
             → push ลง op_stack
        ง. ถ้าเป็น ')'
             → pop output จนกว่าจะเจอ '(' (ไม่ใส่ '(' ลง output)
               คำใบ้: วนซ้ำ pop แล้ว append ไปที่ output จนกว่า pop ได้ '('

      หลัง loop เสร็จ:
        → pop operator ที่เหลือใน op_stack ทั้งหมดเข้า output

    ตัวอย่าง:
        tokens = ["3", "+", "4", "*", "2"]
        output = ["3", "4", "2", "*", "+"]
    """
    output: list[str] = []
    op_stack = StackArray()   # ต้องใช้ StackArray ที่นักศึกษาสร้างเอง

    for tok in tokens:
        ####### IMPLEMENT HERE ########
        pass

    # pop operators ที่เหลืออยู่ใน op_stack ทั้งหมดออก หลังวน loop เสร็จ
    ####### IMPLEMENT HERE ########
    pass
    return output


def eval_postfix(postfix: list[str]) -> float:
    """
    ประเมินค่านิพจน์ postfix และคืนผลลัพธ์เป็น float
    ใช้ StackArray เป็น value stack

    Returns
    -------
    float  ผลลัพธ์ของนิพจน์

    อัลกอริทึม (value stack):
      สำหรับแต่ละ token:
        ก. ถ้าเป็นตัวเลข
             → แปลงเป็น float แล้ว push เข้า stack
        ข. ถ้าเป็น operator (+, -, *, /)
             → pop สองตัว:  b = pop()  แล้ว  a = pop()
               *** สำคัญ: pop ครั้งแรกได้ b (ตัวขวา), pop ครั้งสองได้ a (ตัวซ้าย) ***
               คำนวณ  a op b  แล้ว push ผลลัพธ์กลับ

      หลัง loop เสร็จ:
        → pop ค่าที่เหลืออยู่บน stack คือคำตอบสุดท้าย

    ตัวอย่าง:
        postfix = ["3", "4", "2", "*", "+"]
        คำนวณ:  push 3, push 4, push 2
                 pop 2, pop 4 → 4*2=8 → push 8
                 pop 8, pop 3 → 3+8=11 → push 11
        คืน 11.0
    """
    val_stack = StackArray()   # value stack – เก็บตัวเลขระหว่างการคำนวณ

    for tok in postfix:
        ####### IMPLEMENT HERE ########
        pass

    return val_stack.pop()


def evaluate(expr: str) -> float:
    """
    รับนิพจน์ infix (string) และคืนผลลัพธ์เป็น float
    เรียกใช้ tokenize → infix_to_postfix → eval_postfix  (เตรียมไว้แล้ว)
    """
    tokens = tokenize(expr)
    postfix = infix_to_postfix(tokens)
    return eval_postfix(postfix)


# =============================================================
# demo – รันเพื่อทดสอบ  (python expression_eval.py)
# หมายเหตุ: ผลจะแสดง ✗ ก่อนที่นักศึกษาจะเติม logic ทั้งสอง function
# =============================================================

if __name__ == "__main__":
    test_cases = [
        ("3 + 4 * 2",       11.0),   # precedence: * ก่อน +
        ("(3 + 4) * 2",     14.0),   # วงเล็บบังคับ + ก่อน
        ("10 / (5 - 3)",     5.0),   # วงเล็บกับหาร
    ]

    print("ทดสอบ evaluate (tokenize เตรียมไว้แล้ว – ตรวจ infix_to_postfix + eval_postfix):")
    for expr, expected in test_cases:
        try:
            result = evaluate(expr)
            status = "✓" if result == expected else "✗"
            print(f"  {status}  evaluate({expr!r}) = {result}  (คาดหวัง {expected})")
        except Exception as e:
            print(f"  !  evaluate({expr!r}) → error: {e}")
