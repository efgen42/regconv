def convert(linelist,fpout, verbose, fpin_path, low, up):
    try:
        f = open(fpout, "w", encoding="utf-8")
        print("\nВыбран режим {} регистра:\n".format(
             "понижения" if low else "повышения") if verbose else ""
             )
        for line in linelist:
            if low:
                f.write(line.lower()) and (print(line.lower(), end="") if verbose else "")
            elif up:
                f.write(line.upper()) and (print(line.upper(), end="") if verbose else "")
        f.close
    except (OSError, IOError) as err:
        print ("\nОшибка доступа к файлу {0} \nФайл отсутствует или недоступен\n".format(fpin_path))