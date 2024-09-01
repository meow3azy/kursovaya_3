from abc import ABC, abstractmethod
import requests

class VacancyAPI(ABC):
    """
    Абстрактный класс для работы с API платформ с вакансиями.

    Атрибуты:
    ----------
    base_url : str
        Базовый URL для взаимодействия с API.
    headers : dict
        Заголовки HTTP-запросов для взаимодействия с API.

    Методы:
    -------
    fetch_vacancies(keyword, area=1, per_page=10, page=0):
        Абстрактный метод для получения списка вакансий по ключевому слову.
    """

    def __init__(self, base_url, headers=None):
        """
        Инициализация базового класса для работы с API.

        :param base_url: Базовый URL для взаимодействия с API.
        :param headers: Заголовки HTTP-запросов для API (опционально).
        """
        self.base_url = base_url
        self.headers = headers if headers else {}

    @abstractmethod
    def fetch_vacancies(self, keyword, area=1, per_page=10, page=0):
        """
        Получение списка вакансий по ключевому слову.

        :param keyword: Ключевое слово для поиска вакансий.
        :param area: Регион поиска (по умолчанию Москва).
        :param per_page: Количество вакансий на странице.
        :param page: Номер страницы.
        :return: Список вакансий в формате JSON.
        """
        pass

class HeadHunterAPI(VacancyAPI):
    """
    Реализация класса для работы с API hh.ru (HeadHunter).

    Атрибуты:
    ----------
    base_url : str
        Базовый URL для взаимодействия с API hh.ru.
    headers : dict
        Заголовки HTTP-запросов для API hh.ru.

    Методы:
    -------
    fetch_vacancies(keyword, area=1, per_page=10, page=0):
        Получение списка вакансий с платформы hh.ru по ключевому слову.
    """

    def __init__(self):
        """
        Инициализация объекта для работы с API hh.ru.

        Устанавливаются базовый URL и заголовки для взаимодействия с API hh.ru.
        """
        super().__init__(
            base_url="https://api.hh.ru/vacancies",
            headers={"User-Agent": "API Client"}
        )

    def fetch_vacancies(self, keyword, area=1, per_page=10, page=0):
        """
        Получение списка вакансий с платформы hh.ru по ключевому слову.

        :param keyword: Ключевое слово для поиска вакансий.
        :param area: Регион поиска (по умолчанию Москва).
        :param per_page: Количество вакансий на странице.
        :param page: Номер страницы.
        :return: Список вакансий в формате JSON.
        """
        params = {
            "text": keyword,
            "area": area,
            "per_page": per_page,
            "page": page
        }
        response = requests.get(self.base_url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()['items']
