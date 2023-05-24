st = "Review the metadata for the legal agreements and evidence backing up this bankruptcy claim NFT with token ID 1 of collection 0x250229b4887Edc2144015AE4468bDf96c16C14575 on Gnosis Chain (EVM chain ID 100)."

st1 = st[:45]  # Review the metadata for the legal agreements
st2 = st[46:90]  # and evidence backing up this bankruptcy claim

nft_index = st.find("NFT")  # Найти индекс первого вхождения слова "NFT"
collection_index = st.find("collection")  # Найти индекс первого вхождения слова "collection"

st3 = st[nft_index:collection_index+10]  # NFT with token ID 1 of collection

address_start_index = st.find("0x")  # Найти индекс первого вхождения "0x"
address_end_index = address_start_index + 1  # Инициализировать индекс конца адреса

for i in range(address_start_index + 1, len(st)):
    if st[i] == " ":
        address_end_index = i
        break

st4 = st[address_start_index:address_end_index]  # 0x250229b4887Edc2144015AE4468bDf96c16C14575



st5 = st[address_end_index+1:]  # on Gnosis Chain (EVM chain ID 100).

print(st1)
print(st2)
print(st3)
print(st4)
print(st5)