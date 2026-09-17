class Tier:
    def __init__(self, name, max_speed):
        self.name = name
        self.max_speed = max_speed

    def get_max_speed(self):
        return self.max_speed

    def fortbewegung(self):
        return "unbekannt"

    def speed(self):
        print(f"{self.name}: max. {self.max_speed} m/s")
        print(f"{self.name} bewegt sich durch {self.fortbewegung()}.")
        print(f"Maximale Geschwindigkeit: {self.get_max_speed()} m/s")


class Schlange(Tier):
    def fortbewegung(self):
        return "kriechen"


class Hund(Tier):
    def fortbewegung(self):
        return "rennen"


R = Schlange("Python", 16)
R.speed()

R = Hund("Bello", 11)
R.speed()