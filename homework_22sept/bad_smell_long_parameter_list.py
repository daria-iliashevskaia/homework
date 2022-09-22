
class Unit:
    def __init__(self, field, y, x):
        self.speed = None
        self.state = None
        self.field = field
        self.y = y
        self.x = x

    def move(self, direction):
        speed = self._get_speed()

        if direction == 'UP':
            self.field.set_unit(y=self.y + speed, x=self.x, unit=self)
        elif direction == 'DOWN':
            self.field.set_unit(y=self.y - speed, x=self.x, unit=self)
        elif direction == 'LEFT':
            self.field.set_unit(y=self.y, x=self.x - speed, unit=self)
        elif direction == 'RIGTH':
            self.field.set_unit(y=self.y, x=self.x + speed, unit=self)

    def _get_speed(self):
        if self.state == "fly":
            return self.speed * 1.2
        if self.state == "crawl":
            return self.speed * 0.5
        else:
            ValueError("Рожденный ползать летать не должен!")
