from abc import ABC, abstractmethod
import json


class VacancyFileHandler(ABC):
    """
    Абстрактный класс для работы с файлами вакансий.

    Этот класс определяет интерфейс для сохранения, получения и удаления вакансий в файле.
    """

    @abstractmethod
    def save_vacancy(self, vacancy):
        """
        Сохраняет вакансию в файл.

        :param vacancy: Объект Vacancy для сохранения.
        """
        pass

    @abstractmethod
    def get_vacancies(self, **criteria):
        """
        Получает список вакансий из файла по заданным критериям.

        :param criteria: Критерии для фильтрации вакансий.
        :return: Список вакансий, удовлетворяющих критериям.
        """
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy_id):
        """
        Удаляет вакансию из файла по ID.

        :param vacancy_id: ID вакансии для удаления.
        """
        pass


class JSONVacancyFileHandler(VacancyFileHandler):
    """
    Класс для работы с вакансиями в формате JSON.

    Этот класс реализует методы сохранения, получения и удаления вакансий в JSON-файле.
    """

    def __init__(self, filename):
        """
        Инициализация объекта JSONVacancyFileHandler.

        :param filename: Имя файла, в котором будут храниться вакансии.
        """
        self._filename = filename

    def save_vacancy(self, vacancy):
        """
        Сохраняет вакансию в JSON-файл.

        :param vacancy: Объект Vacancy для сохранения.
        """
        try:
            vacancies = self.get_vacancies()
        except FileNotFoundError:
            vacancies = []

        vacancies.append({
            'title': vacancy.title,
            'url': vacancy.url,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'description': vacancy.description
        })

        with open(self._filename, 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def get_vacancies(self, **criteria):
        """
        Получает список вакансий из JSON-файла по заданным критериям.

        :param criteria: Критерии для фильтрации вакансий.
        :return: Список вакансий, удовлетворяющих критериям.
        """
        with open(self._filename, 'r', encoding='utf-8') as f:
            vacancies = json.load(f)

        # Фильтрация по критериям
        for key, value in criteria.items():
            vacancies = [vac for vac in vacancies if vac.get(key) == value]

        return vacancies

    def delete_vacancy(self, vacancy_url):
        """
        Удаляет вакансию из JSON-файла по URL.

        :param vacancy_url: URL вакансии для удаления.
        """
        try:
            vacancies = self.get_vacancies()
            updated_vacancies = [vac for vac in vacancies if vac['url'] != vacancy_url]
            with open(self._filename, 'w', encoding='utf-8') as f:
                json.dump(updated_vacancies, f, ensure_ascii=False, indent=4)

        except FileNotFoundError:
            pass