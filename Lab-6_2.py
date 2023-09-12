def reverse_list(list):
  """
  Виконує перестановку елементів списку у зворотньому порядку.

  Аргументи:
    list: Список, який потрібно переставити.

  Повертає:
    Новий список, з переставленими елементами.
  """
  new_list = []
  for index in range(len(list) - 1, -1, -1):
    new_list.append(list[index])
  return new_list


if __name__ == "__main__":
  # Вводимо список від користувача
  list = [int(element) for element in input("Введіть список чисел через пробіл: ").split()]

  # Переставляємо елементи списку у зворотньому порядку
  new_list = reverse_list(list)

  # Виводимо список на екран
  print("Новий список:", new_list)
