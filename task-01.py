from abc import ABC, abstractmethod
import logging

logging.basicConfig(
    format="%(asctime)s %(message)s",
    level=logging.INFO,
    handlers=[logging.StreamHandler()],
)


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self):
        raise NotImplementedError()


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        raise NotImplementedError()

    @abstractmethod
    def create_motorcycle(self, make, model):
        raise NotImplementedError()


class Car(Vehicle):
    def start_engine(self):
        logging.info(f"{self.make} {self.model} {self.spec}: Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        logging.info(f"{self.make} {self.model} {self.spec}: Мотор заведено")


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US Spec")


if __name__ == "__main__":
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    us_vehicle_1 = us_factory.create_car("Ford", "Mustang")
    us_vehicle_1.start_engine()

    us_vehicle_2 = us_factory.create_motorcycle("Harley-Davidson", "Sportster")
    us_vehicle_2.start_engine()

    eu_vehicle_1 = eu_factory.create_car("Toyota", "Corolla")
    eu_vehicle_1.start_engine()
