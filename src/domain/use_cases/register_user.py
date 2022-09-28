from abc import ABC, abstractmethod
from typing import Dict

from src.domain.models import Users


class RegisterUser(ABC):
    """Interface tp Registry use case"""

    @abstractmethod
    def register(self, name: str, password: str) -> Dict[bool, Users]:
        """Case"""
        raise Exception("Should implement method: register")
