import json
import re

from sale import send_radix


def check(info):
    #info = ['TransferTokens', 'rdx1qspsgtz8wxzhs7h3m5dxz4uw0a350qp567zz4v9xgamcag8kavsxvpctcgge2', 'rdx1qspgm8zxzr80fsdy33agmmfsx7vvgwynunmaqtq3futu95t7vjyefagra0vvf', '800', 'xrd_rr1qy5wfsfh', 'I want to buy NFTs ID: 0001, 0002, 12333, 1322']
    with open("metadata.json") as file:
        data_json = json.load(file)

    if info[0] == 'TransferTokens' and info[4] == 'xrd_rr1qy5wfsfh' and info[5] != '-':

        value = int(float(info[3]) / 200)
        digits = re.findall(r'\d+', info[5])
        i=0
        numbers = [num.zfill(4) for num in digits]
        for num in numbers:
            i+=1
            found = False
            for item in data_json:
                if item["ID"] == num:
                    found = True
                    if item["owner"] == "available":
                        idf = item["ID"]
                        print(f"New owner for NFT ID - {idf}")
                        item["owner"] = info[1]
                    else:
                        message=f"NFT with ID {num} already owned"
                        print(message)
                        send_radix(info[1],message)
            if not found:
                message = f"NFT with ID {num} not found"
                print(message)
                send_radix(info[1],message)
            if i==value:
                break

            # Сохраняем изменения в файле metadata.json
        with open("metadata.json", "w") as file:
            json.dump(data_json, file)
    else:
        print("its not TransferTokens or token not xrd or message = null")




