import yaml
from pydantic import BaseModel

from .param import Parameter


class FrontMatter(BaseModel):
    name: str
    params: dict[str, Parameter]

    @classmethod
    def from_yaml(cls, yaml_content: str) -> "FrontMatter":
        data = yaml.safe_load(yaml_content)
        name = data['name']
        params: dict[str, Parameter] = {}

        for key, value in data['params'].items():
            if isinstance(value, dict):
                params[key] = Parameter(name=key, **value)
            else:
                params[key] = Parameter(name=key)

        return cls(name=name, params=params)
