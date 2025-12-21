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



def query_employees_with_a(employees, departments):
    return [
        (e.last_name,
         next(d.name for d in departments if d.dept_id == e.dept_id))
        for e in employees
        if e.last_name.startswith("А")
    ]


def query_min_salary_by_department(employees, departments):
    dept_to_salaries = {d.dept_id: [] for d in departments}
    for e in employees:
        dept_to_salaries[e.dept_id].append(e.salary)

    result = [
        (next(d.name for d in departments if d.dept_id == dept_id), min(sals))
        for dept_id, sals in dept_to_salaries.items()
        if sals
    ]
    result.sort(key=lambda x: x[1])
    return result


def query_many_to_many_pairs(employees, departments, links):
    emp_by_id = {e.emp_id: e for e in employees}
    dept_by_id = {d.dept_id: d for d in departments}

    pairs = [
        (emp_by_id[l.emp_id].last_name, dept_by_id[l.dept_id].name)
        for l in links
    ]
    pairs.sort(key=lambda x: x[0])
    return pairs
