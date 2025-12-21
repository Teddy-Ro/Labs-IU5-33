import unittest
from main import (Department, Employee, EmpDept,
                    query_employees_with_a,
                    query_min_salary_by_department,
                    query_many_to_many_pairs)


class TestQueries(unittest.TestCase):
    def setUp(self):
        self.departments = [
            Department(1, "Отдел кадров"),
            Department(2, "Бухгалтерия"),
            Department(3, "IT отдел"),
        ]
        self.employees = [
            Employee(1, "Александров", 80000, 1),
            Employee(2, "Иванов",      60000, 1),
            Employee(3, "Андреев",     90000, 2),
            Employee(4, "Петров",      70000, 2),
            Employee(5, "Архипов",     120000, 3),
        ]
        self.links = [
            EmpDept(1, 1),
            EmpDept(2, 1),
            EmpDept(3, 2),
            EmpDept(4, 2),
            EmpDept(5, 3),
            EmpDept(3, 3),
        ]

    def test_employees_with_a(self):
        result = query_employees_with_a(self.employees, self.departments)
        last_names = [ln for ln, _ in result]
        self.assertEqual(sorted(last_names),
                         sorted(["Александров", "Андреев", "Архипов"]))

    def test_min_salary_by_department(self):
        result = query_min_salary_by_department(self.employees,
                                                self.departments)
        # результат отсортирован по минимальной зарплате
        self.assertEqual(result[0][1], 60000)   # самый маленький минимум
        self.assertTrue(all(isinstance(s, int) for _, s in result))

    def test_many_to_many_pairs(self):
        result = query_many_to_many_pairs(self.employees,
                                          self.departments,
                                          self.links)
        # пары отсортированы по фамилии
        last_names = [ln for ln, _ in result]
        self.assertEqual(last_names, sorted(last_names))


if __name__ == "__main__":
    unittest.main()
