from abc import ABC

class Battery(ABC):
    
    def needs_service(self) -> bool:
        # Custom logic to determine if the battery needs service
        pass