from PIL import Image, ImageDraw, ImageFont
import random
import textwrap


class MemeEngine:
    """Class that get the image and draw meme on it."""
    def __init__(self, out_path='./temp'):
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500) -> str:

        img = Image.open(img_path)

        file_ext = img_path.split('.')[-1]

        if width is not None:
            ratio = width/float(img.size[0])
            height = int(ratio * float(img.size[1]))
            img = img.resize((width, height), Image.NEAREST)

        if text and author is not None:
            draw = ImageDraw.Draw(img)
            fnt_size = int(height / 12)
            fnt = ImageFont.truetype('OpenSans-Italic-VariableFont.ttf',
                                     size=fnt_size)

            textwrapped = textwrap.wrap(f'"{text}"\n-{author}', width=width/20)
            draw.text((10, 30),
                      '\n'.join(textwrapped),
                      font=fnt,
                      fill='white')

        img.save(f'{self.out_path}/{random.randint(0,10**6)}.{file_ext}')
        return f'{self.out_path}/{random.randint(0,10**6)}.{file_ext}'


