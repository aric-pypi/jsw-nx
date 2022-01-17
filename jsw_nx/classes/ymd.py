# year/month/day
from ..packages.days import days as nx_days

class Ymd:
    @classmethod
    def to_s(cls, ymd):
        return str(ymd).rjust(2, '0')

    @classmethod
    def each_month(cls, year, fn):
        months = range(1, 13)
        for month in months:
            fn(year, cls.to_s(month))

    @classmethod
    def each_day(cls, year, fn):
        def inner_lambda(y, m):
            days = nx_days(y, int(m))
            rdays = range(1, days + 1)
            for day in rdays:
                fn(year, m, cls.to_s(day))
        cls.each_month(year, lambda y, m: inner_lambda(y, m))
