with open("text_4.txt", 'r', encoding="utf-8") as f:
    use = [f'{line}. {" ".join(count.split())} - {len(count.split())} слов'
           for line, count in enumerate(f, 1)]
    print(*use, f"Всего строк - {len(use)}.", sep="\n")
