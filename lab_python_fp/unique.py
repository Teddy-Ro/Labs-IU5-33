class Unique:
    def __init__(self, items, **kwargs):
        self.items = iter(items)  # поддержка генераторов и списков
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.items)  # получаем следующий элемент
            # нормализуем для сравнения с учётом ignore_case, если строка
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item
