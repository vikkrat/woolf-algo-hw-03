def move_disk(from_peg, to_peg, disk):
    print(f"Перемістити диск з {from_peg} на {to_peg}: {disk}")

def hanoi(n, source, target, auxiliary):
    if n == 1:
        move_disk(source, target, n)
        pegs[target].append(pegs[source].pop())
        print_state()
    else:
        hanoi(n-1, source, auxiliary, target)
        move_disk(source, target, n)
        pegs[target].append(pegs[source].pop())
        print_state()
        hanoi(n-1, auxiliary, target, source)

def print_state():
    print(f"Проміжний стан: {{'A': {pegs['A']}, 'B': {pegs['B']}, 'C': {pegs['C']}}}")

def main():
    n = int(input("Введіть кількість дисків: "))
    global pegs
    pegs = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
    print(f"Початковий стан: {{'A': {pegs['A']}, 'B': {pegs['B']}, 'C': {pegs['C']}}}")
    hanoi(n, 'A', 'C', 'B')
    print(f"Кінцевий стан: {{'A': {pegs['A']}, 'B': {pegs['B']}, 'C': {pegs['C']}}}")

if __name__ == '__main__':
    main()
