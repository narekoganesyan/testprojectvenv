class Can:
    def can_cure(self):
        print(None)


class Doctor(Can):
    def can_cure(self):
        print("Doctor can cure")


class Architect(Can):
    def can_cure(self):
        print("Arch can cure")


a = Architect()
d = Doctor()

a.can_cure()
d.can_cure()

