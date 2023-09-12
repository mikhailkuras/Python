def delete_even_elements(list):
  """
  Виконує видалення всіх елементів з парним порядковим номером зі списку.

  Аргументи:
    list: Список, з якого потрібно видалити елементи.

  Повертає:
    Новий список, без елементів з парним порядковим номером.
  """
  new_list = []
  for index, element in enumerate(list):
    if index % 2 == 1:
      new_list.append(element)
  return new_list


if __name__ == "__main__":
  # Вводимо список від користувача
  list = [int(element) for element in input("Введіть список чисел через пробіл: ").split()]

  # Видаляємо всі елементи з парним порядковим номером
  new_list = delete_even_elements(list)

  # Виводимо список на екран
  print("Новий список:", new_list)


