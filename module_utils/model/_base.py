from typing import Tuple, Dict, Any, Optional
from pydantic import BaseModel
from pydantic._internal._model_construction import ModelMetaclass


class _PartialMeta(ModelMetaclass):
    def __new__(
        self, name: str, bases: Tuple[type], namespaces: Dict[str, Any], **kwargs
    ):
        annotations: dict = namespaces.get("__annotations__", {})

        for base in bases:
            for base_ in base.__mro__:
                if base_ is BaseModel:
                    break

                annotations.update(base_.__annotations__)

        for field in annotations:
            if not field.startswith("__"):
                annotations[field] = Optional[annotations[field]]
                namespaces.setdefault(field, None)

        namespaces["__annotations__"] = annotations

        return super().__new__(self, name, bases, namespaces, **kwargs)


class TPLinkBaseModel(BaseModel, metaclass=_PartialMeta):
    pass
