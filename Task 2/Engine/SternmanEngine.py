from engine.engine import Engine

class SternmanEngine(Engine):
    def __init__(self, warning_light_on: bool):
        self.warning_light_on = warning_light_on

    def needs_service(self) -> bool:
       if self.warning_light_is_on:
            return True
       else:
            return False