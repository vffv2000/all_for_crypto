from PIL import Image, ImageDraw, ImageFont, ImageFilter
import json

json_data = {
    "title": "Celsius Claim 123456789",
    "subtitle1": "Petition Date Value: 12344567.89 USD",
    "subtitle2": "Estate: Celsius Network LLC",
    "description": "Review the metadata for the legal agreements and evidence backing up this bankruptcy claim NFT with token ID 1 of collection 0x250229b4887Edc2144015AE4468bDf96c16C14575 on Gnosis Chain (EVM chain ID 100)."
}


def CreateBlurText(json_data):
    image = Image.new('RGBA', (750, 1250), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)

    font_subtitle = ImageFont.truetype("Bebas-Regular.otf", size=32)
    font_title = ImageFont.truetype("Bebas-Regular.otf", size=50)
    black_color = (0, 0, 0)  # Черный цвет обводки
    title_size = draw.textsize(json_data["title"], font=font_title)
    title_x = (image.width - title_size[0]) / 2
    title_y = 80
    draw.text((title_x, title_y), json_data["title"], font=font_title, fill=black_color, stroke_width=1)

    subtitle1_size = draw.textsize(json_data["subtitle1"], font=font_subtitle)
    subtitle2_size = draw.textsize(json_data["subtitle2"], font=font_subtitle)

    subtitle1_x = (image.width - subtitle1_size[0]) / 2
    subtitle2_x = (image.width - subtitle2_size[0]) / 2
    subtitle1_y = 675
    subtitle2_y = subtitle1_y+55


    draw.text((subtitle1_x, subtitle1_y), json_data["subtitle1"], font=font_subtitle, fill=black_color, stroke_width=1)
    draw.text((subtitle2_x, subtitle2_y), json_data["subtitle2"], font=font_subtitle, fill=black_color, stroke_width=1)


    vertitle_size=draw.textsize('Verified by CEX.Claims', font=font_subtitle)
    vertitle_size_x = (image.width - vertitle_size[0]+45) / 2
    subtitle1_y = 1025
    draw.text((vertitle_size_x, subtitle1_y), 'Verified by CEX.Claims', font=font_subtitle, fill=black_color, stroke_width=1)



    image = image.filter(ImageFilter.BLUR)
    image.save('blur_text_img.png')


def CreateNormalText(json_data):
    image = Image.new('RGBA', (750, 1250), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)


    font_title = ImageFont.truetype("Bebas-Regular.otf", size=50)
    font_subtitle = ImageFont.truetype("Bebas-Regular.otf", size=32)
    font_description = ImageFont.truetype("bahnschrift.ttf", size=20)
    font_font = ImageFont.truetype("Helvetica-Bold.ttf", size=17)

    white_color = (255, 255, 255)  # Белый цвет текста

    title_size = draw.textsize(json_data["title"], font=font_title)
    title_x = (image.width - title_size[0]) / 2
    title_y = 80
    draw.text((title_x, title_y), json_data["title"], font=font_title, fill=white_color)
    image.save('normal_text_img.png')

    subtitle1_size = draw.textsize(json_data["subtitle1"], font=font_subtitle)
    subtitle2_size = draw.textsize(json_data["subtitle2"], font=font_subtitle)

    subtitle1_x = (image.width - subtitle1_size[0]) / 2
    subtitle2_x = (image.width - subtitle2_size[0]) / 2
    subtitle1_y = 675
    subtitle2_y = subtitle1_y+55

    draw.text((subtitle1_x, subtitle1_y), json_data["subtitle1"], font=font_subtitle, fill=white_color)
    draw.text((subtitle2_x, subtitle2_y), json_data["subtitle2"], font=font_subtitle, fill=white_color)

    st = json_data["description"]

    st1 = st[:45]  # Review the metadata for the legal agreements
    st2 = st[45:90]  # and evidence backing up this bankruptcy claim

    nft_index = st.find("NFT")  # Найти индекс первого вхождения слова "NFT"
    collection_index = st.find("collection")  # Найти индекс первого вхождения слова "collection"

    st3 = st[nft_index:collection_index + 10]  # NFT with token ID 1 of collection

    address_start_index = st.find("0x")  # Найти индекс первого вхождения "0x"
    address_end_index = address_start_index + 1  # Инициализировать индекс конца адреса

    for i in range(address_start_index + 1, len(st)):
        if st[i] == " ":
            address_end_index = i
            break

    st4 = st[address_start_index:address_end_index]  # 0x250229b4887Edc2144015AE4468bDf96c16C14575

    st5 = st[address_end_index + 1:]  # on Gnosis Chain (EVM chain ID 100).

    description_size1 = draw.textsize(st1, font=font_description)
    description_size2 = draw.textsize(st2, font=font_description)
    description_size3 = draw.textsize(st3, font=font_description)
    description_size4 = draw.textsize(st4, font=font_description)
    description_size5 = draw.textsize(st5, font=font_description)

    description_x_1 = (image.width - description_size1[0]) / 2
    description_x_2 = (image.width - description_size2[0]) / 2
    description_x_3 = (image.width - description_size3[0]) / 2
    description_x_4 = (image.width - description_size4[0]) / 2
    description_x_5 = (image.width - description_size5[0]) / 2

    description_y1 = subtitle2_y + subtitle2_size[1]+30
    description_y2 = description_y1 + description_size1[1]+4
    description_y3 = description_y2 + description_size2[1]+4
    description_y4 = description_y3 + description_size3[1]+10
    description_y5 = description_y4 + description_size4[1]+10

    draw.text((description_x_1, description_y1), st1, font=font_description, fill=white_color)
    draw.text((description_x_2, description_y2), st2, font=font_description, fill=white_color)
    draw.text((description_x_3, description_y3), st3, font=font_description, fill=white_color)
    draw.text((description_x_4, description_y4), st4, font=font_description, fill=white_color)
    draw.text((description_x_5, description_y5), st5, font=font_description, fill=white_color)

    vertitle_size=draw.textsize('Verified by CEX.Claims', font=font_subtitle)
    vertitle_size_x = (image.width - vertitle_size[0]+45) / 2
    subtitle1_y = 1025
    draw.text((vertitle_size_x, subtitle1_y), 'Verified by CEX.Claims', font=font_subtitle, fill=white_color)


    checkmark_image = Image.open("checkmark_image.png")
    new_size = (30, 40)  # Новый размер для изображения галочки
    resized_checkmark = checkmark_image.resize(new_size)
    x = int(vertitle_size_x)-35  # Координата X для вставки
    y = subtitle1_y  # Координата Y для вставки
    image.paste(resized_checkmark, (x, y), resized_checkmark)


    image.save('normal_text_img.png')

def GenerateImgIntoIpfs(json_data, name_of_center, name_of_card):
    main_image = Image.open(f'{name_of_card}.png')
    blur_text = Image.open('blur_text_img.png')
    normal_text = Image.open('normal_text_img.png')

    if blur_text.size != main_image.size:
        blur_text = blur_text.resize(main_image.size)

    if normal_text.size != main_image.size:
        normal_text = normal_text.resize(main_image.size)

    if blur_text.mode != main_image.mode:
        blur_text = blur_text.convert(main_image.mode)

    if normal_text.mode != main_image.mode:
        normal_text = normal_text.convert(main_image.mode)

    combined_image = Image.alpha_composite(blur_text, normal_text)
    combined_image.save('ddd.png')
    finall_image = Image.alpha_composite(main_image,combined_image)


    checkmark_image = Image.open(f"{name_of_center}.png")
    checkmark_image=checkmark_image.convert(main_image.mode)
    new_size = (350, 350)  # Новый размер для изображения галочки
    resized_checkmark = checkmark_image.resize(new_size)
    x = 200  # Координата X для вставки
    y = 193  # Координата Y для вставки
    finall_image.paste(resized_checkmark, (x, y), resized_checkmark)

    finall_image.save(f'CERTIFICADO-{json_data["title"]}.png')

def CreateImg(json_data,name_of_center,name_of_card):
    CreateBlurText(json_data)
    CreateNormalText(json_data)
    GenerateImgIntoIpfs(json_data, name_of_center, name_of_card)

name_of_center=input("imput name of center( center1 )")
name_of_card=input("imput name of center( card1 )")

CreateImg(json_data, name_of_center, name_of_card)
