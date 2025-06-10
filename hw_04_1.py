import pathlib

current_dir = pathlib.Path(__file__).parent

def total_salary(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            total = 0
            count = 0

            for line in file:
                parts = line.strip().split(',')
                if len(parts) == 2:
                    try:
                        salary = int(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        # Якщо зарплата не є числом, пропускаємо рядок
                        continue

            average = total / count if count > 0 else 0
            return total, average

    except FileNotFoundError:
        return "Не вдалося знайти файл salary_file.txt."

total, average = total_salary("salary_file.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
