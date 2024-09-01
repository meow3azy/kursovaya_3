from src.file_handler import JSONVacancyFileHandler
from src.vacancy import Vacancy


def user_interaction():
    # Задайте имя файла для хранения вакансий
    filename = 'vacancies.json'

    # Создайте обработчик файлов с указанием имени файла
    file_handler = JSONVacancyFileHandler(filename)

    # Пример взаимодействия с пользователем
    while True:
        print("\n1. Добавить вакансию")
        print("2. Удалить вакансию")
        print("3. Показать все вакансии")
        print("4. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите название вакансии: ")
            url = input("Введите ссылку на вакансию: ")
            salary_from = input("Введите нижний предел зарплаты (оставьте пустым, если не указано): ")
            salary_to = input("Введите верхний предел зарплаты (оставьте пустым, если не указано): ")
            description = input("Введите краткое описание вакансии: ")

            salary_from = int(salary_from) if salary_from else None
            salary_to = int(salary_to) if salary_to else None

            vacancy = Vacancy(title, url, salary_from, salary_to, description)
            file_handler.save_vacancy(vacancy)
            print("Вакансия добавлена.")

        elif choice == '2':
            url = input("Введите ссылку на вакансию для удаления: ")
            file_handler.delete_vacancy(url)
            print("Вакансия удалена.")

        elif choice == '3':
            vacancies = file_handler.get_vacancies()
            if not vacancies:
                print("Вакансии не найдены.")
            else:
                for vac in vacancies:
                    print(f"Название: {vac['title']}")
                    print(f"URL: {vac['url']}")
                    print(f"Зарплата: {vac.get('salary_from', 'Не указана')} - {vac.get('salary_to', 'Не указана')}")
                    print(f"Описание: {vac['description']}")
                    print("-" * 20)

        elif choice == '4':
            print("Выход из программы.")
            break

        else:
            print("Некорректный выбор. Попробуйте еще раз.")


if __name__ == '__main__':
    user_interaction()
