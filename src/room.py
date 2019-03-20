# Implement a class to hold room information. This should have name and
# description attributes.

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items= items
        self.n_to = none
        self.s_to = none
        self.e_to = none
        self.w_to = none
    def get_room_in_direction(self, direction):
      if direction == "n":
          return self.n_to
      if direction == "s":
          return self.s_to
      if direction == "e":
          return self.e_to
      if direction == "w":
          return self.w_to
      else:
          return None