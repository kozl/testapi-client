from typing import Tuple
from abc import ABC, abstractclassmethod

from src.models import(
    UserInfoResponse,
    AuthResponse,
    UpdateResponse,
    UpdateRequest
)


class TestApiClient(ABC):

    @abstractclassmethod
    def authorize(login, password: str) -> AuthResponse:
        """
        Авторизуется в testapi, возвращает статус авторизации и токен,
        если авторизация была успешна. В противном случае возвращает пустую строку
        """
        pass

    @abstractclassmethod
    def get_user(username, token: str) -> UserInfoResponse:
        """
        Получает и возвращает данные о пользователе
        """
        pass

    @abstractclassmethod
    def update_user(user_id: int, token: str, request: UpdateRequest) -> UpdateResponse:
        """
        Обновляет данные пользователя
        """
        pass
