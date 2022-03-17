from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel


class TxtIngestor(IngestorInterface):
    """A class inherits IngestorInerface to handle txt input files."""
    valid_extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []

        with open(path) as infile:
            for line in infile:
                line_list = line.split(' - ')
                new_quote = QuoteModel(line_list[0], line_list[1])
                quotes.append(new_quote)
        return quotes
