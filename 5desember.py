puzzle_input = []

with open("puzzle_5.txt") as puzzle:
    for line in puzzle:
        puzzle_input.append(int(line))

num_jumps = 0
current_pos = 0
list_length = len(puzzle_input)

while current_pos < list_length:
    current_pos_value = puzzle_input[current_pos]
    next_pos = current_pos + current_pos_value

    # For puzzle 2, else always incremet by 1
    incr = (1 if current_pos_value < 3 else -1)
    puzzle_input[current_pos] = current_pos_value + incr
    # puzzle_input[current_pos] = current_pos_value + 1

    current_pos = next_pos
    num_jumps += 1
    # print("next post", next_pos)

print("Exited loop after", num_jumps, "jumps")
