class Distance:
    _conversions = {
        "mm": 0.001,
        "cm": 0.01,
        "m": 1,
        "km": 1000,
    }

    def __init__(self, volue, unit):
        self.volue = volue
        self.unit = unit
        if unit not in self._conversions:
            raise ValueError(f"Неподдерживаемая единица: {unit}")


    def __str__(self):
      return f"эксземпляр Distance: {self.volue}{self.unit}"

    def convert(self, to_unit="m"):
        """Конвертируем в любую единицу"""
        if to_unit not in self._conversions:
            raise ValueError(f"Неподдерживаемая единица: {to_unit}")
        meters = self.volue * self._conversions[self.unit]
        return meters / self._conversions[to_unit]

    def __add__(self, other):
        total = self.convert("m") + other.convert("m")
        return Distance(total / self._conversions[self.unit], self.unit)

    def __sub__(self, other):
        total = self.convert("m") - other.convert("m")
        return Distance(total / self._conversions[self.unit], self.unit)



