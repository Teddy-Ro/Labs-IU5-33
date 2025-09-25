def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        key = args[0]
        for item in items:
            # значения None пропускаются
            value = item.get(key)
            if value is not None:
                yield value
    else:
        for item in items:
            # соберём словарь только из указанных ключей с не-None значениями
            filtered = {k: v for k in args for v in [item.get(k)] if v is not None}
            # если все указанные поля None, элемент пропускается
            if filtered:
                yield filtered
