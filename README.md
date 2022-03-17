# Meme Generator

This is a Udacity Intermediate Python project that can generate a meme by placing a provided text caption onto a provided
image. It can load quotes from a variaty of filetypes (PDF, Word Documents, CSVs, Text files). Load, manipulate and save images.
It accepts dynamic user input through a command-line tool and a web service.


## Packages
Project uses `python 3`, `random`, `PIL`, `abc`, `argparse`, `typing`, `pandas`, `docx`, `os`, `subprocess`, `requests`, `flask`.

## Project Components
This project includes a command line application and a flask application, which reads a file with an image and a file with quotes. Project includes two modules `QuoteEngine` and `MemeGenerator`.

`QuoteEngine` Module parses an input file containing captions including quote and author. A caption input file is to have a one quote and author per line separated by ",".
Module can parse *.docx, *.csv, *.pdf, and *.txt files. Module includes abstract base class `IngestorInterface`. `Ingestor` class selects an appropriate ingestor for a given type of quote input file. Module returns a list of `QuoteModel` objects containing quote text and quote author strings.

`MemeGenerator` Module creates a meme by placing a caption on a provided image. Image file type is *.png or *.jpeg. Module return a path to a created image with the caption.


## Running the program
There are two ways to run this program:

1. Run `app.py` to start flask server and interact. The result file is stored in folder`src/static`


2. Run `python3 meme.py`. The `meme.py` script takes three optional command line arguments:


* `--body` a string quote body
* `--author` a string quote author
* `--path ` an image path

The result is stored in folder  `src/temp `

## Some improvements to do.. 
- Handle user invalid inputs, specifically,  add an /templates/meme_error.html page and redirect to that page.
- Define custom exception classes for different types of exceptions—for things like Invalid File, Invalid Text Input (e.g. too long)
- Use os.walk to automatically discover ingestible files in a directory


## License
`meme.py` is a public domain work, dedicated using [CC0 1.0](https://creativecommons.org/publicdomain/zero/1.0/).
