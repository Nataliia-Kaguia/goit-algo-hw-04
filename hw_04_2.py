import pathlib

def get_cats_info(path):
    cats = []
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    cat = {
                        "id": parts[0],
                        "name": parts[1],
                        "age": parts[2]
                    }
                    cats.append(cat)
        return cats
    except FileNotFoundError:
        print(f"Файл за шляхом {path} не знайдено.")
        return []
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return []
cats_info = get_cats_info("cats_file.txt")
print(cats_info)
