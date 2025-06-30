from collections import defaultdict


def get_num_words(file_contents):
    return len(file_contents.split())


def count_char(file_contents):
    char_count = defaultdict(int)
    for char in file_contents:
        char_count[char.lower()] += 1
    return char_count


def sort_on(items):
    return items["num"]


def sorted_count(char_count):
    char_sort = []
    for key, value in char_count.items():
        char_sort.append({"char": key, "num": value})
    char_sort.sort(reverse=True, key=sort_on)
    return char_sort
