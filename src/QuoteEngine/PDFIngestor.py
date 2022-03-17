from typing import List
import subprocess
import os

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel


class PDFIngestor(IngestorInterface):
    """A class inherits IngestorInerface to handle pdf input files."""
    valid_extensions = ['pdf']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        temp = 'temp.txt'
        call = subprocess.call(['pdftotext', path, temp])

        file_ref = open(temp, "r")

        for line in file_ref.readlines():
            line = line.strip()
            if len(line) > 0:
                line = line.strip('\r\n').strip()
                parsed = line.split(' - ')
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)

        file_ref.close()
        try:
            os.remove(temp)
        except OSError:
            pass
        return quotes
