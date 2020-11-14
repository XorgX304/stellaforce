from abc import abstractmethod
from typing import Protocol



class DecryptorProtocol(Protocol):
    @abstractmethod
    def decrypt(self, file_path: str) -> dict:
        raise NotImplementedError

