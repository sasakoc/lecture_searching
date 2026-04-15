from pathlib import Path
import json


def read_data(file_name, field):
    cwd_path = Path.cwd()
    file_path = cwd_path / file_name

    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get(field)
    except FileNotFoundError:
        print(f"Chyba: Soubor {file_name} nebyl nalezen.")
        return None


def linear_search(searched_data, searched_number):
    for index, value in enumerate(searched_data):
        if value == searched_number:
            return index
    return -1


def binary_search(searched_data, searched_number):
    low = 0
    high = len(searched_data) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = searched_data[mid]

        if guess == searched_number:
            return mid
        if guess > searched_number:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def pattern_search(sequence, pattern):
    positions = []
    m = len(pattern)
    n = len(sequence)
    for i in range(n - m + 1):
        if sequence[i: i + m] == pattern:
            positions.append(i)
    return positions


def binary_search(searched_data, searched_number):
    low = 0
    high = len(searched_data) - 1

    while low <= high:
        mid = (low + high) // 2
        if searched_data[mid] == searched_number:
            return mid
        elif searched_data[mid] < searched_number:
            low = mid + 1
        else:
            high = mid - 1
    return None


def main():
    target = 72
    ordered_list = read_data('sequential.json', 'ordered_numbers')

    if ordered_list is not None:
        result_index = binary_search(ordered_list, target)

        if result_index is not None:
            print(f"Číslo {target} bylo nalezeno na indexu {result_index}.")
        else:
            print(f"Číslo {target} se v seznamu nenachází.")


def main():
    unordered_data = read_data('sequential.json', 'unordered_numbers')
    if unordered_data:
        target = 31
        idx = linear_search(unordered_data, target)
        print(f"Lineární vyhledávání: Číslo {target} nalezeno na indexu {idx}")

    ordered_data = read_data('sequential.json', 'ordered_numbers')
    if ordered_data:
        target = 70
        idx = binary_search(ordered_data, target)
        print(f"Binární vyhledávání: Číslo {target} nalezeno na indexu {idx}")

    dna_seq = read_data('sequential.json', 'dna_sequence')
    if dna_seq:
        pattern = "AGG"
        found_positions = pattern_search(dna_seq, pattern)
        print(f"Vyhledávání vzoru '{pattern}': Nalezeno na pozicích {found_positions}")


if __name__ == "__main__":
    main()
