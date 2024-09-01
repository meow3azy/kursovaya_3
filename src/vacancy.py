class Vacancy:
    """
    Класс для представления вакансии.

    Атрибуты:
    ----------
    _title : str
        Название вакансии.
    _url : str
        Ссылка на вакансию.
    _salary_from : int, optional
        Нижний предел зарплаты (может быть None).
    _salary_to : int, optional
        Верхний предел зарплаты (может быть None).
    _description : str
        Краткое описание вакансии.

    Методы:
    -------
    title():
        Возвращает название вакансии.
    url():
        Возвращает ссылку на вакансию.
    salary_from():
        Возвращает нижний предел зарплаты.
    salary_to():
        Возвращает верхний предел зарплаты.
    description():
        Возвращает описание вакансии.
    __lt__(other):
        Сравнивает вакансии по зарплате (меньше чем).
    __le__(other):
        Сравнивает вакансии по зарплате (меньше или равно).
    __gt__(other):
        Сравнивает вакансии по зарплате (больше чем).
    __ge__(other):
        Сравнивает вакансии по зарплате (больше или равно).
    __repr__():
        Возвращает строковое представление вакансии.
    """

    def __init__(self, title, url, salary_from=None, salary_to=None, description=""):
        """
        Инициализация объекта Vacancy.

        :param title: Название вакансии.
        :param url: Ссылка на вакансию.
        :param salary_from: Нижний предел зарплаты (может быть None).
        :param salary_to: Верхний предел зарплаты (может быть None).
        :param description: Краткое описание вакансии.
        """
        self._title = title
        self._url = url
        self._salary_from = self._validate_salary(salary_from)
        self._salary_to = self._validate_salary(salary_to)
        self._description = description

    @staticmethod
    def _validate_salary(salary):
        """
        Валидация значения зарплаты.

        :param salary: Значение зарплаты (может быть числом или None).
        :return: Возвращает валидированное значение зарплаты, если оно корректно.
        :raises ValueError: Если зарплата отрицательная или не является числом.
        """
        if salary is None:
            return None
        try:
            salary = int(salary)
        except (TypeError, ValueError):
            raise ValueError("Salary must be an integer or None")

        if salary < 0:
            raise ValueError("Salary cannot be negative")
        return salary

    @property
    def title(self):
        """
        Возвращает название вакансии.

        :return: Название вакансии.
        """
        return self._title

    @property
    def url(self):
        """
        Возвращает ссылку на вакансию.

        :return: Ссылка на вакансию.
        """
        return self._url

    @property
    def salary_from(self):
        """
        Возвращает нижний предел зарплаты.

        :return: Нижний предел зарплаты.
        """
        return self._salary_from

    @property
    def salary_to(self):
        """
        Возвращает верхний предел зарплаты.

        :return: Верхний предел зарплаты.
        """
        return self._salary_to

    @property
    def description(self):
        """
        Возвращает описание вакансии.

        :return: Описание вакансии.
        """
        return self._description

    def __lt__(self, other):
        """
        Сравнивает вакансии по зарплате (меньше чем).

        :param other: Другая вакансия для сравнения.
        :return: True, если текущая вакансия имеет меньшую зарплату.
        """
        return (self.salary_to or 0) < (other.salary_to or 0)

    def __le__(self, other):
        """
        Сравнивает вакансии по зарплате (меньше или равно).

        :param other: Другая вакансия для сравнения.
        :return: True, если текущая вакансия имеет меньшую или равную зарплату.
        """
        return (self.salary_to or 0) <= (other.salary_to or 0)

    def __gt__(self, other):
        """
        Сравнивает вакансии по зарплате (больше чем).

        :param other: Другая вакансия для сравнения.
        :return: True, если текущая вакансия имеет большую зарплату.
        """
        return (self.salary_to or 0) > (other.salary_to or 0)

    def __ge__(self, other):
        """
        Сравнивает вакансии по зарплате (больше или равно).

        :param other: Другая вакансия для сравнения.
        :return: True, если текущая вакансия имеет большую или равную зарплату.
        """
        return (self.salary_to or 0) >= (other.salary_to or 0)

    def __repr__(self):
        """
        Возвращает строковое представление вакансии.

        :return: Строковое представление вакансии.
        """
        return f"Vacancy({self.title}, {self.salary_from}-{self.salary_to})"
