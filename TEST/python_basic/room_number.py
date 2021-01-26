
for i in range(1,5):
    if i == 3:
        break#continue
    print(f"-------------{i}层----------------")
    for j in range(20):
        if j < 10:
            print(f"L{i}-{i}0{j}")
        else:
            print(f"L{i}-{i}{j}")