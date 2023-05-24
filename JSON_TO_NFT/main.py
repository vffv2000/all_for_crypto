from PIL import Image, ImageDraw, ImageFont
import json

json_data = {
    "title": "Celsius Claim 123456789",
    "subtitle1": "Petition Date Value: 12344567.89 USD",
    "subtitle2": "Estate: Celsius Network LLC",
    "description": "Review the metadata for the legal agreements and evidence backing up this bankruptcy claim NFT with token ID 1 of collection 0x250229b4887Edc2144015AE4468bDf96c16C14575 on Gnosis Chain (EVM chain ID 100)."
}


def GenerateImgIntoIpfs(json_data):

    image = Image.open("CERTIFICADO-EDITABLE.png")

    draw = ImageDraw.Draw(image)

    font_title = ImageFont.truetype("Broadcast_Matter_JeZHxJ.otf", size=69)
    font_subtitle = ImageFont.truetype("Gabriola_JeZHxJ.ttf", size=41)
    font_description = ImageFont.truetype("Gabriola_JeZHxJ.ttf", size=25)
    font_font = ImageFont.truetype("Broadcast_Matter_JeZHxJ.otf", size=49)

    title_size = draw.textsize(json_data["title"], font=font_title)

    title_x = (image.width - title_size[0]) / 2
    title_y = 50
    draw.text((title_x, title_y+401), json_data["title"], font=font_title, fill=(0, 0, 0))

    line_x1, line_y1 = title_x-15, title_y+401 + title_size[1] + 25
    line_x2, line_y2 = title_x + title_size[0]+15, line_y1
    draw.line((line_x1, line_y1, line_x2, line_y2), width=3, fill=(0, 0, 0))

    subtitle1_size = draw.textsize(json_data["subtitle1"], font=font_subtitle)
    subtitle2_size = draw.textsize(json_data["subtitle2"], font=font_subtitle)

    subtitle1_x = (image.width - subtitle1_size[0]) / 2
    subtitle2_x = (image.width - subtitle2_size[0]) / 2
    subtitle1_y = title_y + title_size[1] + 10
    subtitle2_y = subtitle1_y + subtitle1_size[1] + 5

    draw.text((subtitle1_x, subtitle1_y+435), json_data["subtitle1"], font=font_subtitle, fill=(0, 0, 0))
    draw.text((subtitle2_x, subtitle2_y+435), json_data["subtitle2"], font=font_subtitle, fill=(0, 0, 0))

    st = json_data["description"]

    st1 = st[0:73]
    st2 = st[74:124]
    st3 = st[125:184]
    st4 = st[185:]

    description_size1 = draw.textsize(st1, font=font_description)
    description_size2 = draw.textsize(st2, font=font_description)
    description_size3 = draw.textsize(st3, font=font_description)
    description_size4 = draw.textsize(st4, font=font_description)

    description_x_1 = (image.width - description_size1[0]) / 2
    description_x_2 = (image.width - description_size2[0]) / 2
    description_x_3 = (image.width - description_size3[0]) / 2
    description_x_4 = (image.width - description_size4[0]) / 2

    description_y1 = subtitle2_y + subtitle2_size[1] + 20
    description_y2 = description_y1 + description_size1[1]
    description_y3 = description_y2 + description_size2[1]
    description_y4 = description_y3 + description_size3[1]

    draw.text((description_x_1, description_y1+445), st1, font=font_description, fill=(0, 0, 0), align='center')
    draw.text((description_x_2, description_y2+450), st2, font=font_description, fill=(0, 0, 0), align='center')
    draw.text((description_x_3, description_y3+455), st3, font=font_description, fill=(0, 0, 0), align='center')
    draw.text((description_x_4, description_y4+460), st4, font=font_description, fill=(0, 0, 0), align='center')

    verified_text = "Verified by CEX.Claims"
    verified_size = draw.textsize(verified_text, font=font_font)

    verified_x = (image.width - verified_size[0]) // 2
    verified_y = description_y4 + 500

    draw.text((verified_x, verified_y), verified_text, font=font_font, fill=(0, 0, 0))

    create_img=image.save(f'CERTIFICADO-{json_data["title"]}.png')
    return create_img

GenerateImgIntoIpfs(json_data)
