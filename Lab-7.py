import sys

# Створюємо словник для зберігання даних
schools = {}

# Додаємо записи до словника
for i in range(6):
  school_type = input("Введіть тип навчального закладу: ")
  school_students = int(input("Введіть кількість учнів у навчальному закладі: "))
  schools[school_type] = school_students

# Обробляємо виключні ситуації
try:
  # Визначаємо загальну кількість учнів шкіл
  total_school_students = sum(schools.values())

  # Виводимо на екран результат
  print("Загальна кількість учнів шкіл:", total_school_students)
except KeyError as e:
  print("Немає навчального закладу з типом", e)
except ValueError as e:
  print("Некоректне значення", e)

# Завершуємо програму
sys.exit(0)



