from src.api import HeadHunterAPI
from src.vacancy import Vacancy
from src.file_handler import JSONVacancyFileHandler

def user_interaction():
    api = HeadHunterAPI()
    file_handler = JSONVacancyFileHandler()

    while True:
        print("\n1. Ввести поисковый запрос для запроса вакансий из hh.ru")
        print("2. Получить топ N вакансий по зарплате")
        print("3. Получить вакансии с ключевым словом в описании")
        print("4. Выйти")
        choice = input("Выберите действие: ")

        if choice == '1':
            keyword = input("Введите ключевое слово для поиска: ")
            vacancies = api.fetch_vacancies(keyword)
            for vac in vacancies:
                salary_from = vac['salary']['from'] if vac['salary'] else None
                salary_to = vac['salary']['to'] if vac['salary'] else None
                vacancy = Vacancy(
                    title=vac['name'],
                    url=vac['alternate_url'],
                    salary_from=salary_from,
                    salary_to=salary_to,
                    description=vac['snippet']['responsibility'] if vac['snippet'] else ""
                )
                file_handler.save_vacancy(vacancy)
            print(f"{len(vacancies)} вакансий сохранено.")

        elif choice == '2':
            N = int(input("Сколько вакансий вывести? "))
            vacancies = file_handler.get_vacancies()
            vacancies = sorted(vacancies, key=lambda x: x['salary_to'] or 0, reverse=True)[:N]
            for vac in vacancies:
                print(f"{vac['title']} - {vac['salary_from']}-{vac['salary_to']} руб. ({vac['url']})")

        elif choice == '3':
            keyword = input("Введите ключевое слово для поиска в описании: ")
            vacancies = file_handler.get_vacancies()
            filtered_vacancies = [vac for vac in vacancies if keyword.lower() in (vac['description'] or "").lower()]
            for vac in filtered_vacancies:
                print(f"{vac['title']} - {vac['salary_from']}-{vac['salary_to']} руб. ({vac['url']})")

        elif choice == '4':
            break

if __name__ == "__main__":
    user_interaction()
