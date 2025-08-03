n = int(input())
weapons = list(map(int, input().split()))

even_count = 0
odd_count = 0

for w in weapons:
    if w % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

if even_count > odd_count:
    print("READY FOR BATTLE")
else:
    print("NOT READY")
