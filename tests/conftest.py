import functools
import json

import pytest
from dotenv import load_dotenv
from horsona.index import indices, load_indices
from horsona.llm import engines as llm_engines
from horsona.llm import load_engines as load_llm_engines

load_dotenv()


# Add LLMs from llm_config.json
# with open("llm_config.json") as f:
#     config = json.load(f)
#     engines = engines_from_config(config)


class FixtureFunctionWrapper:
    def __init__(self, name, obj):
        self.__name__ = name
        self.obj = obj

    def __call__(self):
        return self.obj


load_llm_engines()
for key, engine in llm_engines.items():
    globals()[key] = pytest.fixture(scope="session", autouse=False)(
        FixtureFunctionWrapper(key, engine)
    )


load_indices()
for key, index in indices.items():
    globals()[key] = pytest.fixture(scope="session", autouse=False)(
        FixtureFunctionWrapper(key, index)
    )
