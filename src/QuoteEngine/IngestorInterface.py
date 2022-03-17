from abc import ABC, abstractmethod

from typing import List
from .Quote import QuoteModel


class IngestorInterface(ABC):

    valid_extensions = []

    @classmethod
    def can_ingest(cls, path: str):
        ext = path.split('.')[-1]
        return ext in cls.valid_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
