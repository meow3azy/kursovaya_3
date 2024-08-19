import unittest
from src.vacancy import Vacancy
from src.file_handler import JSONVacancyFileHandler


class TestVacancy(unittest.TestCase):

    def test_salary_validation(self):
        with self.assertRaises(ValueError):
            Vacancy("Test", "http://example.com", salary_from=-1000)

    def test_comparison(self):
        vac1 = Vacancy("Vac 1", "http://example.com/1", salary_to=5000)
        vac2 = Vacancy("Vac 2", "http://example.com/2", salary_to=10000)
        self.assertTrue(vac2 > vac1)


class TestJSONVacancyFileHandler(unittest.TestCase):

    def setUp(self):
        self.handler = JSONVacancyFileHandler("test_vacancies.json")
        self.vacancy = Vacancy("Test", "http://example.com", salary_from=1000, salary_to=2000)

    def tearDown(self):
        self.handler._save_to_file([])  # Очистка файла после тестов

    def test_save_and_load_vacancy(self):
        self.handler.save_vacancy(self.vacancy)
        vacancies = self.handler.get_vacancies()
        self.assertEqual(len(vacancies), 1)
        self.assertEqual(vacancies[0]['title'], "Test")

    def test_delete_vacancy(self):
        self.handler.save_vacancy(self.vacancy)
        self.handler.delete_vacancy("http://example.com")
        vacancies = self.handler.get_vacancies()
        self.assertEqual(len(vacancies), 0)


if __name__ == "__main__":
    unittest.main()
