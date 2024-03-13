from typing import get_args, get_origin
import copy


class ApiObject:

    def __init__(self, data):
        self.__deserialize(data)

    def __serialize(self):
        serialize_object = copy.deepcopy(vars(self))

        for key, value in serialize_object.items():
            if type(value) is list and issubclass(get_args(self.__annotations__[key])[0], ApiObject):
                serialize_subclasses = []
                for element in value:
                    serialize_subclasses.append(element.get_serialize_object())

                serialize_object[key] = serialize_subclasses

            elif isinstance(value, ApiObject):
                serialize_object[key] = value.get_serialize_object()

        return serialize_object

    def __deserialize(self, data):
        for key, value in data.items():
            if hasattr(self, key):
                if key in self.__annotations__:
                    origin_type = get_origin(self.__annotations__[key])
                    args = get_args(self.__annotations__[key])

                    if origin_type is list and args:
                        subclass = args[0]

                        deserialized_subclasses = []

                        for element in value:
                            deserialized_subclasses.append(subclass(element))

                        setattr(self, key, deserialized_subclasses)
                    else:
                        setattr(self, key, self.__annotations__[key](value))
                else:
                    setattr(self, key, value)

    def set(self, field, value):
        if hasattr(self, field):
            setattr(self, field, value)
        else:
            raise AttributeError(f'Field {field} not found')

    def get(self, field):
        if hasattr(self, field):
            return getattr(self, field)
        else:
            raise AttributeError(f'Field {field} not found')

    def get_serialize_object(self):
        return self.__serialize()


if __name__ == '__main__':
    pass

