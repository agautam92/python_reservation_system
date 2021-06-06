from abc import abstractmethod, ABCMeta


class Hotel(ABCMeta):
    name = None
    rooms = {"rate": 500, "total": 10, "available": 10}
    suites = {"rate": 700, "total": 5, "available": 5}
    penthouse = {"rate": 900, "total": 3, "available": 3}
    avail_rooms = {"rate": rooms.get("rate"), "available": rooms.get("total")}
    avail_suites = {"rate": suites.get("rate"), "available": suites.get("total")}
    avail_penthouse = {"rate": penthouse.get("rate"), "available": penthouse.get("total")}

    @abstractmethod
    def get_room_rate(cls):
        return cls.rooms.get('rate')

    @abstractmethod
    def get_suite_rate(cls):
        return cls.suites.get('rate')

    @abstractmethod
    def get_penthouse_rate(cls):
        return cls.penthouse.get('rate')

    def get_available_rooms(cls):
        return cls.rooms.get("available")

    def get_available_suites(cls):
        return cls.suites.get("available")

    def get_available_penthouse(cls):
        return cls.penthouse.get("available")

