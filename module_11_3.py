import inspect


def introspection_info(obj):
    obj_type = type(obj) # Получаем тип объекта

    obj_attrs = dir(obj) # Получаем атрибуты объекта

    obj_methods = [method for method in obj_attrs if callable(getattr(obj, method))] # Получаем методы объекта

    obj_module = inspect.getmodule(obj) # Получаем модуль, к которому принадлежит объект

    obj_properties = {
        'type': obj_type,
        'attributes': obj_attrs,
        'methods': obj_methods,
        'module': obj_module
    }

    return obj_properties


number_info = introspection_info(42)
print(number_info)
