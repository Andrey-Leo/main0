import inspect


def introspection_info(obj):
    obj_type = type(obj) # Получаем тип объекта

    obj_attrs = [attr for attr in dir(obj) if not callable(getattr(obj, attr))] # Получаем атрибуты объекта

    obj_methods = [method for method in dir(obj) if callable(getattr(obj, method))] # Получаем методы объекта

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
