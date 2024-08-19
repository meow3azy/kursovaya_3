class Vacancy:
    def __init__(self, title, url, salary_from=None, salary_to=None, description=""):
        self._title = title
        self._url = url
        self._salary_from = self._validate_salary(salary_from)
        self._salary_to = self._validate_salary(salary_to)
        self._description = description

    @staticmethod
    def _validate_salary(salary):
        if salary is not None and salary < 0:
            raise ValueError("Salary cannot be negative")
        return salary

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def salary_from(self):
        return self._salary_from

    @property
    def salary_to(self):
        return self._salary_to

    @property
    def description(self):
        return self._description

    def __lt__(self, other):
        return (self.salary_to or 0) < (other.salary_to or 0)

    def __le__(self, other):
        return (self.salary_to or 0) <= (other.salary_to or 0)

    def __gt__(self, other):
        return (self.salary_to or 0) > (other.salary_to or 0)

    def __ge__(self, other):
        return (self.salary_to or 0) >= (other.salary_to or 0)

    def __repr__(self):
        return f"Vacancy({self.title}, {self.salary_from}-{self.salary_to})"
