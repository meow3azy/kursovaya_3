from abc import ABC, abstractmethod
import requests


class VacancyAPI(ABC):
    @abstractmethod
    def fetch_vacancies(self, keyword, area=1, per_page=10, page=0):
        pass


class HeadHunterAPI(VacancyAPI):
    def fetch_vacancies(self, keyword, area=1, per_page=10, page=0):
        url = "https://api.hh.ru/vacancies"
        params = {
            "text": keyword,
            "area": area,
            "per_page": per_page,
            "page": page
        }
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()['items']
