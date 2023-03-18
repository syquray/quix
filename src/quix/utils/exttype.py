from typing import Any, Type


class _AttributeRepr:
    def __init__(self, **kwargs: Any) -> None:
        self.__dict__.update(**kwargs)

    def __repr__(self) -> str:
        _attr = [f"{key}={value!r}" for key, value in self.__dict__.items()]

        return f"{type(self).__name__}({', '.join(_attr)})"

    __str__ = __repr__


def define(name: str, **kwargs: Any) -> Type:
    class _Internal(_AttributeRepr):
        def __init__(self, **kwargs: Any) -> None:
            super().__init__(**kwargs)

    _Internal.__name__ = name

    return _Internal(**kwargs)
