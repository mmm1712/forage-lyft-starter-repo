from engine.engine import Engine 

class WilloughbyEngine(Engine):
    def __init__(self, last_service_mileage: int, current_mileage: int):
     self.current_mileage = current_mileage;
     self.last_service_mileage = last_service_mileage;

    def needs_service(self) -> bool:
       return self.current_mileage - self.last_service_mileage > 60000