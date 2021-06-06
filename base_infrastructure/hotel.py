from abc import abstractmethod, ABCMeta

from .constant_var import BOOKING_TYPE
from .location import Location


class HotelAbstract(metaclass=ABCMeta):
    """
     At least 10, 5, 3 rooms, suites, penthouse are required to add a hotel in our portal.
     Rate logic can be implemented by subclassed based on location and demand.
    """
    name = None
    rooms = {"rate": 500, "total": 10, "available": 10}
    suites = {"rate": 700, "total": 5, "available": 5}
    penthouse = {"rate": 900, "total": 3, "available": 3}
    avail_rooms = {"rate": rooms.get("rate"), "available": rooms.get("total")}
    avail_suites = {"rate": suites.get("rate"), "available": suites.get("total")}
    avail_penthouse = {"rate": penthouse.get("rate"), "available": penthouse.get("total")}
    location = Location()

    @classmethod
    def get_room_rate(cls):
        return cls.rooms.get('rate')

    @classmethod
    def get_suite_rate(cls):
        return cls.suites.get('rate')

    @classmethod
    def get_penthouse_rate(cls):
        return cls.penthouse.get('rate')

    @classmethod
    def get_available_rooms(cls):
        return cls.rooms.get("available")

    @classmethod
    def get_available_suites(cls):
        return cls.suites.get("available")

    @classmethod
    def get_available_penthouse(cls):
        return cls.penthouse.get("available")


class Hotel(HotelAbstract):

    @classmethod
    def check_availability(cls, no_booking, room_type):
        if room_type == BOOKING_TYPE.get(1):
            if cls.rooms.get("available") >= no_booking:
                return True
            else:
                return False
        elif room_type == BOOKING_TYPE.get(2):
            if cls.suites.get("available") >= no_booking:
                return True
            else:
                return False
        elif room_type == BOOKING_TYPE.get(3):
            if cls.penthouse.get("available") >= no_booking:
                return True
            else:
                return False

    @classmethod
    def book(cls, no_booking, room_type):
        validated = cls.check_availability(no_booking, room_type)
        if validated:
            if room_type == BOOKING_TYPE.get(1):
                cls.rooms['availability'] = cls.rooms.get("availability") - no_booking
            elif room_type == BOOKING_TYPE.get(2):
                cls.suites['availability'] = cls.suites.get("availability") - no_booking
            elif room_type == BOOKING_TYPE.get(3):
                cls.penthouse['availability'] = cls.penthouse.get("availability") - no_booking
            cls.set_rate()
            return True

    @classmethod
    def set_rate(cls):
        """
        Room, Suite and Penthouse rates will be updated based on demand, location and some business logic.
        :return: None
        """
        cls.rooms['rate'] = cls.rooms.get("rate")
        cls.suites['rate'] = cls.suites.get("rate")
        cls.penthouse['rate'] = cls.penthouse.get("rate")
        return
