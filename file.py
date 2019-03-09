with open('referat.txt', 'r', encoding='utf-8') as referat:
    content = referat.read()
    print("Длина контента составляет: ", len(content), "символов")#считаем длину контента всего

with open('referat.txt', 'r', encoding='utf-8') as referat_slova:#считаем длину пробелов, как разделителей между словами.
    content = referat_slova.read()
    print("Длина контента составляет: ", len(content.split(" ")), "слов")#считаем длину контента всего

     
with open('referat.txt', 'r', encoding='utf-8') as referat_voskl:
    for voskl in referat_voskl:
        voskl = voskl.replace (".","!")#заменяем точки на восклицательные знаки
        with open('referat2.txt', 'a', encoding='utf-8') as referat2:#открываем новый файл referat2.txt, нужно добавлять каждую строчку в конец.
            referat2.write(voskl)