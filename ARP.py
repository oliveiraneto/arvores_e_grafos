# Aluno: Sebastião Oliveira Silva Neto - 2011478
def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = []
    right = []

    for i in range(1, len(data)):
        if data[i][0] < pivot[0]:
            left.append(data[i])
        else:
            right.append(data[i])

    return quick_sort(left) + [pivot] + quick_sort(right)


def bubble_sort(data):
    n = len(data)
    for i in range(n):
        for j in range(0, n-i-1):
            if data[j][0] > data[j+1][0]:
                data[j], data[j+1] = data[j+1], data[j]
    return data


def selection_sort(data):
    for i in range(len(data)):
        min_idx = i
        for j in range(i+1, len(data)):
            if data[min_idx][0] > data[j][0]:
                min_idx = j
        data[i], data[min_idx] = data[min_idx], data[i]
    return data


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j][0] > key[0]:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


if __name__ == '__main__':
    patients_data = [
        (37, 'F', 4000, 'Leste', 3),
        (32, 'F', 2000, 'Centro', 4),
        (45, 'M', 3500, 'Jardins', 3),
        (55, 'M', 8000, 'Norte', 5),
        (22, 'F', 1500, 'Sul', 2),
    ]

    sorted_data = quick_sort(patients_data)
    print(f"QuickSort: {sorted_data}")

    sorted_data = bubble_sort(patients_data)
    print(f"BubbleSort: {sorted_data}")

    sorted_data = selection_sort(patients_data)
    print(f"SelectionSort: {sorted_data}")

    sorted_data = insertion_sort(patients_data)
    print(f"InsertionSort: {sorted_data}")
