sub_str = input()
count = 0
ref_str = "hello"

for char in sub_str:
    if char == ref_str[count]:
        count += 1

    if count == len(ref_str):
        break

if count == len(ref_str):
    print("YES")
else:
    print("NO")
