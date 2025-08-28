""" เขียน function ชื่อ analyze_scores ที่มีคุณสมบัติดังนี้:

รับ list ของคะแนน (ตัวเลข)
return dictionary ที่มี:

total: ผลรวมของคะแนนทั้งหมด
average: คะแนนเฉลี่ย (ปัดเศษ 1 ตำแหน่งหลังจุดทศนิยม)
highest: คะแนนสูงสุด
lowest: คะแนนต่ำสุด
passed: จำนวนคะแนนที่ >= 70 """
def analyze_scores(scores):
    total = sum(scores)
    average = round(total / len(scores), 1)
    highest = max(scores)
    lowest = min(scores)
    passed = len([score for score in scores if score >= 70])
    return {
        "total": total,
        "average": average,
        "highest": highest,
        "lowest": lowest,
        "passed": passed
    }
test_scores = [85, 67, 90, 72, 58, 99, 74]
result = analyze_scores(test_scores)
print(result)
