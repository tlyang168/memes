from typing import List
from .outputs import (
    Response,
    Formats,
    ValueStates
)

class Renderer:
    def __init__(self) -> None:
        pass
    def render(self,responses: List[Response]):
        for res in responses:
            self._renderOne(res)

    def _renderOne(self, response: Response):
        line = ""
        for (enc, letter) in zip(response.encoding, response.guess):
            line += Formats[enc.name].value%letter
        print(line)
        

