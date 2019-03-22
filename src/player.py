# Write a class to hold player information, e.g. what room they are in
# currently.
class Player():
    def __init__(self, name=Noob, current_room):
        self.name = name
        self.current_room = current_room
    def travel(self, direction):
        if direction in ["n", "s", "e", "w"]:
            next_room = self.current_room.get_room_in_direction(direction)
            if next_room is not None:
                self.current_room = next_room
            else:
                print('Ouch!!!\nYou just bumped you head against the wall,\n because tyou can\'t mve in that direction.')

    def __str__(self):
        return (f'{self.name} is now in {self.current_room}.')