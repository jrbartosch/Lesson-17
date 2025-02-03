def find_first_set_bit(n):
    if n == 0:
        return -1
    position = 0
    while n and 1 == 0:
        n >>= 1
        position += 1
    return position
number = 8
first_set_bit_position = find_first_set_bit(number)
print ('First Set Bit Position:', first_set_bit_position)