import unittest
from src.vacancy import Vacancy
from src.file_handler import JSONVacancyFileHandler

class TestJSONVacancyFileHandler(unittest.TestCase):
    def setUp(self):
        self.filename = 'test_vacancies.json'
        self.handler = JSONVacancyFileHandler(self.filename)
        self.vacancy = Vacancy(
            title="Software Engineer",
            url="https://example.com/vacancy/1",
            salary_from=100000,
            salary_to=150000,
            description="Looking for an experienced software engineer."
        )

    def tearDown(self):
        import os
        if os.path.isfile(self.filename):
            os.remove(self.filename)

    def test_save_vacancy(self):
        self.handler.save_vacancy(self.vacancy)
        vacancies = self.handler.get_vacancies()
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['title'], self.vacancy.title)

    def test_get_vacancies(self):
        self.handler.save_vacancy(self.vacancy)
        vacancies = self.handler.get_vacancies(title="Software Engineer")
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['title'], self.vacancy.title)

    def test_delete_vacancy(self):
        self.handler.save_vacancy(self.vacancy)
        self.handler.delete_vacancy(self.vacancy.url)
        vacancies = self.handler.get_vacancies()
        self.assertEqual(len(vacancies), 0)

if __name__ == '__main__':
    unittest.main()
