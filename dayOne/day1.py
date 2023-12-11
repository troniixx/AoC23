#part 1
def combine(path_input):
    sol = 0
    with open(path_input, "r") as f:
        for line in f:
            digits = [char for char in line if char.isdigit()]
            if digits:
                if len(digits) > 1:
                    combined_number = int(str(digits[0]) + str(digits[-1]))
                else:
                    combined_number = int(str(digits[0]) + str(digits[0]))
                sol += combined_number

    return sol

#part 2
def calib(path_input):
    mapped = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
    sol = 0

    with open(path_input, "r") as f:
        for line in f:
            words = line.split()
            for i, word in enumerate(words):
                if word.lower() in mapped:
                    words[i] = mapped[word.lower()]
            line = ''.join(words)
            digits = [char for char in line if char.isdigit()]
            if digits:
                if len(digits) > 1:
                    combined_number = int(str(digits[0]) + str(digits[-1]))
                else:
                    combined_number = int(str(digits[0]) + str(digits[0]))
                sol += combined_number

    return sol


if __name__ == '__main__':
    #print(combine("/Users/merterol/Desktop/AoC23/dayOne/input_simple.txt"))
    #print(combine("/Users/merterol/Desktop/AoC23/dayOne/input.txt"))
    #print("---------------------")
    print(calib("/Users/merterol/Desktop/AoC23/dayOne/input_calib.txt"))
    print(calib("/Users/merterol/Desktop/AoC23/dayOne/input_calib_simple.txt"))
