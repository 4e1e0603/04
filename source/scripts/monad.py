from abc import ABC, abstractmethod

class Monad(ABC):
    """
    Abstract class for monads.
    """

    @abstractmethod
    def bind(self) -> None:
        raise NotImplementedError

    @abstractmethod
    def unit(self) -> None:
        raise NotImplementedError
