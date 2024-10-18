def count_inv_m(a_i, a_d):
    new_array = []
    i = 0
    d = 0
    inv = 0
    while i < len(a_i) and d < len(a_d):
        if a_i[i] <= a_d[d]:
            new_array.append(a_i[i])
            i += 1
        else:
            new_array.append(a_d[d])
            d += 1
            inv += (len(a_i)-i)
    return inv

def count_inv(array):
    if len(array) == 1:
        return 0
    
    mid = int((len(array)/2))
    ci = count_inv(array[:mid])
    cd = count_inv(array[mid:])
    cm = count_inv_m(sorted(array[:mid]), sorted(array[mid:]))
    return ci + cd + cm

print(count_inv([4, 3, 7, 0]))