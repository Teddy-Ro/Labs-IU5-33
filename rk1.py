class Department:
    def __init__(self, dept_id: int, name: str):
        self.dept_id = dept_id
        self.name = name

    def __repr__(self) -> str:
        return f"Department(id={self.dept_id}, name='{self.name}')"


class Employee:
    def __init__(self, emp_id: int, last_name: str, salary: int, dept_id: int):
        self.emp_id = emp_id
        self.last_name = last_name
        self.salary = salary
        self.dept_id = dept_id

    def __repr__(self) -> str:
        return (f"Employee(id={self.emp_id}, last_name='{self.last_name}', "
                f"salary={self.salary}, dept_id={self.dept_id})")


# класс-связка для многие-ко-многим
class EmpDept:
    def __init__(self, emp_id: int, dept_id: int):
        self.emp_id = emp_id
        self.dept_id = dept_id

    def __repr__(self) -> str:
        return f"EmpDept(emp_id={self.emp_id}, dept_id={self.dept_id})"


# Тестовые данные
departments = [
    Department(1, "Отдел кадров"),
    Department(2, "Бухгалтерия"),
    Department(3, "IT отдел"),
]

employees = [
    Employee(1, "Стариков", 80000, 1),
    Employee(2, "Гуськов", 60000, 1),
    Employee(3, "Андреев", 90000, 2),
    Employee(4, "Попов", 70000, 2),
    Employee(5, "Косарев", 120000, 3),
]

# связи многие-ко-многим (один сотрудник может быть в нескольких отделах)
emp_dept_links = [
    EmpDept(1, 1),
    EmpDept(2, 1),
    EmpDept(3, 2),
    EmpDept(4, 2),
    EmpDept(5, 3),
    EmpDept(3, 3),
]

print("Запрос 1:")
result1 = [
    (e.last_name, next(d.name for d in departments if d.dept_id == e.dept_id))
    for e in employees
    if e.last_name.startswith("А")
]
print(result1)
print()

print("Запрос 2:")
# группируем зарплаты по отделам
dept_to_salaries = {d.dept_id: [] for d in departments}
for e in employees:
    dept_to_salaries[e.dept_id].append(e.salary)

# формируем (название отдела, минимальная зарплата)
dept_min_salary = [
    (next(d.name for d in departments if d.dept_id == dept_id), min(sals))
    for dept_id, sals in dept_to_salaries.items()
    if sals  # в отделе есть сотрудники
]

# сортировка по минимальной зарплате
dept_min_salary.sort(key=lambda x: x[1])
print(dept_min_salary)
print()

print("Запрос 3:")
# словари для быстрого доступа
emp_by_id = {e.emp_id: e for e in employees}
dept_by_id = {d.dept_id: d for d in departments}

pairs = [
    (emp_by_id[link.emp_id].last_name, dept_by_id[link.dept_id].name)
    for link in emp_dept_links
]

# сортируем по фамилии сотрудника
pairs.sort(key=lambda x: x[0])
print(pairs)
