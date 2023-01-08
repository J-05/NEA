def calculate_index(i, num):
    if i == 0:
        return num

    return calculate_index(i - 1, (num + 2) % 3)

if __name__ == "__main__":
    for x in range(1, 7):
        print(f"x: {x}, output: " + str(calculate_index(x, 2)))