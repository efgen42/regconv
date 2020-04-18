def info(fpin, fpout, workdir, counts):
    l = len(workdir) if len(workdir) >= len(fpin) else len(fpin)
    l = l if l >= len(fpout) else len(fpout)
    print("\n{0:=>65}".format("") + l*"=")
    print("{0}".format((
        "Всего строк: {0:<32}Рабочая директория: {1}\nКонвертированных строк: {2:<21}Входной файл: {3} \
        \nНеобработанных строк: {4:<23}Выходной файл: {5}"
        .format(counts["cstr"], workdir, (counts["cstr"] - counts["cskip"]), fpin, counts["cskip"], fpout
        ))))
    print("{0:=>65}".format("") + l*"=" + "\n")