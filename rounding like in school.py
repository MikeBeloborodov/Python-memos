data = """5356766 263
9115 1670
9031701 824
7477140 4493811
195 10
2024517 -2469830
19289 790
5730879 643
2707489 611
5853241 578
19703 1732
9000599 557
6169 1496
37 2
-384908 -193535
-6212090 -336846
5708621 13
6175 508
9474643 -1873629
-1948326 -1258794
4967118 808
2025330 527
-7630813 90930
9847 1926
17731 1674
8094474 1197715
11505 900
273 14""".replace("\n", " ").strip().split(" ")

import math

def make_two_arrays(init_data: list) -> list:
    data = [int(a) for a in init_data]
    list1 = []
    list2 = []
    
    for n in range(len(data)):
        if n % 2 != 0: list1.append(data[n])
        else: list2.append(data[n])
        
    return [list1, list2]
    
def rounding_floats(list1: list, list2: list) -> str:
    results = []
    
    for n in range(len(list1)):
        divis = list2[n] / list1[n]
        if divis > 0:
            results.append(math.trunc(list2[n] / list1[n] + 0.5))
        else:
            results.append(math.trunc(list2[n] / list1[n] - 0.5))
            
    return " ".join(str(a) for a in results)

two_arrays = make_two_arrays(data)
list1 = two_arrays[0]
list2 = two_arrays[1]

print(rounding_floats(list1, list2))

