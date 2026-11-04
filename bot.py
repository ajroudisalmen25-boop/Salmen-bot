from PIL import Image, ImageDraw, ImageFont
import io

def make_logo(text):
    # خلفية سوداء
    img = Image.new('RGB', (1080, 1080), color='black')
    draw = ImageDraw.Draw(img)
    
    # فونت ابيض كبير في الوسط
    try:
        font = ImageFont.truetype("arial.ttf", 120)  # جرب فونت موجود
    except:
        font = ImageFont.load_default()  # كان ما لقاش فونت
    
    # احسب وين نحط الكتابة في الوسط
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (1080 - text_width) / 2
    y = (1080 - text_height) / 2
    
    # اكتب بالابيض مش بالاسود 👹
    draw.text((x, y), text, fill="white", font=font)
    
    # ستايل ملعون
    draw.text((x+5, y+5), text, fill="red", font=font)  # ظل احمر
    
    return img
