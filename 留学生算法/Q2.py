def number_to_digitLis_reversed_order(num):
    digits = []
    while num != 0:
        digits.append(num % 10)
        num //= 10
    return digits
def numbers_to_digitLis_original_order(num):
    reversed_digits = number_to_digitLis_reversed_order(num)
    n = len(reversed_digits)
    original_digits = []
    for i in range(0, n):
        original_digits.append(reversed_digits[n-i-1])
    return original_digits
def is_lucky_number (num):
    digits = numbers_to_digitLis_original_order(num)
    res = []
    for i in digits:
        if [i,digits.count(i)] not in res:
            res.append([i,digits.count(i)])
    res.sort(key=lambda x:x[1],reverse=True)
    a = res[0][0]
    b = res[-1][0]
    for i in res:
        if i[1] == res[0][1]:
            a = max(i[0],a)
    for i in res:
        if i[1] == res[-1][1]:
            b = max(i[0],b)
    if str(abs(a * res[0][1] - b * res[-1][1]))[-1] == '6':
        return True
    else:
        return False
def count_jumping_scheme(num):
    db = [0 for _ in range(num + 1)]
    db[0] = db[1] = 1
    for i in range(2, num + 1):
        db[i] = db[i - 1] + db[i - 2]
    return db[-1]
number = int(input())
num_of_schemes = count_jumping_scheme(number)
if is_lucky_number(num_of_schemes):
    print("Yes")
else:
    print("No")