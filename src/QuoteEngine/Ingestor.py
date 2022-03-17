from typing import List

from .IngestorInterface import IngestorInterface
from .Quote import QuoteModel
from .DocxIngestor import DocxIngestor
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TxtIngestor
from .PDFIngestor import PDFIngestor


class Ingestor(IngestorInterface):
    """A class inherits IngestorInerface and encapsulate all four helper
    classes. It can select the appropriate helper for a given file, based
    on the filetype
    """
    ingestors = [DocxIngestor, CSVIngestor, TxtIngestor, PDFIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
