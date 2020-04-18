import argparse, os
import info
import convert
import checkline
from datetime import datetime
import time

parser = argparse.ArgumentParser(description="Утилита для конвертации текстового файла методом смены регистра символов")
parser = argparse.ArgumentParser(add_help=False)

# Аргументы
parser.add_argument("fpin", type=str, help="Имя входного файла")
parser.add_argument("fpout", type=str, nargs="?", default="outfile.txt", help="Имя выходного файла")

parser.add_argument("-u", "--uppercase", action="store_true", help="Поднять регистр")
parser.add_argument("-l", "--lowercase", action="store_true", help="Опустить регистр" )
parser.add_argument("-v", "--verbose", action="store_true", help="Показать подробную информацию")
parser.add_argument("-h","--help",action='help', default=argparse.SUPPRESS, help="Вывод справочной информации")
args = parser.parse_args() # парсим аргументы
low = args.lowercase
up = args.uppercase
workdir = os.path.dirname(os.path.abspath(__file__)) # определяем путь к дир-рии программы (раб. дир.)
fpin_path = os.path.abspath(args.fpin)
os.chdir(workdir)   # переходим в раб. дир.
linelist = []
counts = {"cstr" : 0, "cskip" : 0}    # счётчики обработанных и необработанных строк


def main():
    start_time = datetime.now()
    class ArgsException(Exception): pass    # класс исключения наличия аргумента
    class NameException(Exception): pass    # класс исключения уникальности имен файлов
    try:
        if (args.lowercase and args.uppercase) or (not args.lowercase and not args.uppercase):  # проверка наличия аргумента {u|l}
            raise ArgsException()
        if args.fpin == args.fpout :    # проверка имен файлов на уникальность
            raise NameException()
        checkline.checkline(args.fpin, linelist, counts, fpin_path)    
        convert.convert(linelist, args.fpout, args.verbose, fpin_path, low, up)
        if args.verbose:
            info.info(args.fpin, args.fpout, workdir, counts)
    except ArgsException:
        print("\nОшибка! Ожидается обязательный параметр -l --lowercase или -u --uppercase.\n")
    except NameException:
        print("\nОшибка! Имена входного и выходного файла должны отличаться.\n")
    print(datetime.now() - start_time)

main()