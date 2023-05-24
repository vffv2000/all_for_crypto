from excel import readXLSX, writeXLSX
from parser_zk import get_info


def main():
    address = readXLSX()
    print("Получены кошельки из excel файла")
    index = 4
    for addres in address:
        print(f"Начинаю работу с адресом {addres}")
        data = get_info(addres)
        index += 1
        data.append(index)
        print(data)
        writeXLSX(data)


if __name__ == "__main__":
    main()
