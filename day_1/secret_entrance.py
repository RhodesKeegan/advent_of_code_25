MAX_NUMBER = 99

def main():
    current_number = 50
    lines = open('secret_entrance.txt').read().splitlines()
    number_of_zeros = 0

    for line in lines:
        number = int(line[1:])
        number_of_zeros += int(number/(MAX_NUMBER+1))
        
        number_was_zero = current_number==0
        if line[0] == 'L':
            
            current_number -= number % (MAX_NUMBER + 1)
            if current_number < 0:
                current_number += (MAX_NUMBER + 1)
                if current_number != 0 and not number_was_zero:
                    number_of_zeros += 1
        elif line[0] == 'R':
            current_number += number % (MAX_NUMBER + 1)
            if current_number > MAX_NUMBER:
                current_number -= (MAX_NUMBER + 1)
                if current_number != 0 and not number_was_zero:
                    number_of_zeros += 1
        if current_number == 0:
            number_of_zeros += 1
    print(f'answer: {number_of_zeros}')



if __name__ == "__main__":
    main()