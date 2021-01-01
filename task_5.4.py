r_dic = {"One": "Один,", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_44.txt", "w", encoding='utf-8') as n_file:
    with open("text_4.txt", encoding='utf-8') as m_file:
        n_file.writelines([line.replace(line.split()[0], r_dic.get(line.split()[0])) for line in m_file])
