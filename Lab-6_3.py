text = input("Введіть текст: ")

# Формуємо множину з літер, що входять у текст
letter_set = set(text.lower())

# Визначаємо кількість розділових знаків у тексті
separator_count = 0
for char in text:
  if not char.isalpha():
    separator_count += 1

# Друкуємо результат
print("Множина літер:", letter_set)
print("Кількість розділових знаків:", separator_count)
