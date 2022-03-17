import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except ValueError as e:
            print(f'ValueError: {e}')

    images_path = "./_data/photos/dog/"

    imgs = []
    for root, dir, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form['image_url']
    body = request.form['body']
    author = request.form['author']
    temp_img = './temp_img.jpg'
    img_content = requests.get(image_url, stream=True).content
    with open(temp_img, "wb") as infile:
        infile.write(img_content)
    # Use the meme object to generate a meme using this temp
    # file and the body and author form paramaters.
    path = meme.make_meme(temp_img, body, author)
    os.remove(temp_img)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
