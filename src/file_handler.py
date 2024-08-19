from abc import ABC, abstractmethod
import json

class VacancyFileHandler(ABC):
    @abstractmethod
    def save_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies(self, **criteria):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        pass

class JSONVacancyFileHandler(VacancyFileHandler):
    def __init__(self, filename="data/vacancies.json"):
        self._filename = filename

    def save_vacancy(self, vacancy):
        vacancies = self._load_from_file()
        vacancies.append({
            'title': vacancy.title,
            'url': vacancy.url,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'description': vacancy.description
        })
        self._save_to_file(vacancies)

    def get_vacancies(self, **criteria):
        vacancies = self._load_from_file()
        filtered_vacancies = vacancies
        for key, value in criteria.items():
            filtered_vacancies = [vac for vac in filtered_vacancies if vac.get(key) == value]
        return filtered_vacancies

    def delete_vacancy(self, vacancy_id):
        vacancies = self._load_from_file()
        vacancies = [vac for vac in vacancies if vac['url'] != vacancy_id]
        self._save_to_file(vacancies)

    def _load_from_file(self):
        try:
            with open(self._filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def _save_to_file(self, vacancies):
        with open(self._filename, "w", encoding="utf-8") as file:
            json.dump(vacancies, file, ensure_ascii=False, indent=4)
