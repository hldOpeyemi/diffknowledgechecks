seq = [12, 16, 8, 56, 23, 15, 9, 31]

def check_if_greater_than_10(seq):
    if(seq > 10):
        print(f'large: {seq}')
    elif (seq == 10 or seq < 10):
        print(f'not large: {seq}')
    
counter = 0
while (counter < len(seq)):
    # print(seq[counter])
    number = seq[counter]
    check_if_greater_than_10(number)
    counter = counter + 1