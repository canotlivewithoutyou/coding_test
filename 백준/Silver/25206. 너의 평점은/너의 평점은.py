import sys

total_score=0
total_subject=0
scores={"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0,"C+":2.5, "C0":2.0, "D+":1.5, "D0":1.0, "F":0}
for line in sys.stdin:
    if not line.strip():
        continue
    subject, score, grade=line.split()
    if grade!="P":
        total_score+=float(score)*scores[grade]
        total_subject+=float(score)
print(total_score/total_subject)