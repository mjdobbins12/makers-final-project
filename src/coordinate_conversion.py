class Convert:
    def coordinates(self, turn_from, turn_to):
        converted_coordinates = []
        try:
            columns = {
                "a": 0,
                "b": 1,
                "c": 2,
                "d": 3,
                "e": 4,
                "f": 5,
                "g": 6,
                "h": 7
                }
            converted_coordinates.append(7 - (int(turn_from[1]) - 1))
            converted_coordinates.append(columns[turn_from[0]])
            converted_coordinates.append(7 - (int(turn_to[1]) - 1))
            converted_coordinates.append(columns[turn_to[0]])
        except:
            converted_coordinates = [0,0,7,7]
        return converted_coordinates
