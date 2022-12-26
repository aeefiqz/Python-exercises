import random


def generate_random_sequence(number):
    num_sequence = []
    while len(num_sequence) < number:
        num = random.randint(1, number + 1)
        if num in num_sequence:
            continue
        else:
            num_sequence.append(num)
    print(num_sequence)


def play_guessing_game(sequence,number):
    current_number = sequence[0]

    
def main():
    


main()