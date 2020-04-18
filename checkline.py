def checkline(fpin, linelist, counts, fpin_path):
    class ExtException(Exception): pass # класс исключения расширения файла
    try:
        if not fpin.endswith(".txt"):
            raise ExtException()
        for line in open(fpin, encoding="utf-8"):
                if not (line.lower().islower() or line == ''): # если все символы строки не поддерживают приведение к регистру либо строка пустая
                    counts["cskip"] +=1  # увеличиваем счетчик необработанных строк
                linelist.append(line)   # наполняем список строк
                counts["cstr"] += 1  # увеличиваем общий счетчик строк
    except ExtException:
        print('\nОшибка формата файла {0}\nВходной файл должен быть текстовым\n(".txt")'.format(fpin_path))
    except (OSError, IOError) as err:
        print ("\nОшибка доступа к файлу {0} \nФайл отсутствует или недоступен\n".format(fpin_path))
    except (UnicodeDecodeError, LookupError) as err:
        print("\nОшибка кодировки файла {0}\nВходной файл должен быть в кодировке utf-8\n".format(fpin_path))
    return linelist, counts
 