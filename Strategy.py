from API import Game


class Strategy(Game):
    """
        FILL THIS METHOD OUT FOR YOUR BOT:
        Method to set unit initializations. Run at the beginning of a game, after assigning player numbers.
        We have given you a default implementation for this method.
        OUTPUT:
            An array of 3 dictionaries, where each dictionary details a unit. The dictionaries should have the following fields
                "health": An integer indicating the desired health for that unit
                "speed": An integer indicating the desired speed for that unit
                "unitId": An integer indicating the desired id for that unit. In this provided example, we assign Ids 1,2,3 if you are player1, or 4,5,6 if you are player2
                "attackPattern": a 7x7 2d integer list indicating the desired attack pattern for that unit
                "terrainPattern": a 7x7 2d boolean list indicating the desired terrain pattern for that unit.
        Note: terrainPattern and attackPattern should be indexed x,y. with (0,0) being the bottom left
        If player_id is 1, UnitIds for the bots should be 1,2,3. If player_id is 2, UnitIds should be 4,5,6
    """
    def get_setup(self):
        units = []
        # if you are player1, unitIds will be 1,2,3. If you are player2, they will be 4,5,6

        # Setup for Bot 1
        unit1 = dict()
        unit1["unitId"] = 1
        if self.player_id == 2:
            unit1["unitId"] += 3

        unit1["health"] = 5
        unit1["speed"] = 5
        # creation of 2d lists
        unit1["attackPattern"] = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        unit1["terrainPattern"] = [
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, True,  False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False]]
        units.append(unit1)

        # Setup for Bot 2
        unit2 = dict()
        unit2["unitId"] = 2
        if self.player_id == 2:
            unit2["unitId"] += 3

        unit2["health"] = 5
        unit2["speed"] = 5
        # creation of 2d lists
        unit2["attackPattern"] = [
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 2, 2, 2, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        unit2["terrainPattern"] = [
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, True, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False]]
        units.append(unit2)

        # Setup for Bot 3
        unit3 = dict()
        unit3["unitId"] = 3
        if self.player_id == 2:
            unit3["unitId"] += 3

        unit3["health"] = 5
        unit3["speed"] = 5
        # creation of 2d lists
        unit3["attackPattern"] = [
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        unit3["terrainPattern"] = [
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, True, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False]]
        units.append(unit3)
                
        return units

    """
        FILL THIS METHOD OUT FOR YOUR BOT:
        Method to implement the competitors strategy in the next turn of the game.
        We have given you a default implementation here.
        OUTPUT:
            A list of 3 dictionaries, each of which indicates what to do on a given turn with that specific unit. Each dictionary should have the following keys:
                "unitId": The Id of the unit this dictionary will detail the action for
                "movement": an array of directions ("UP", "DOWN", "LEFT", or "RIGHT") details how you want that unit to move on this turn
                "attack": the direction in which to attack ("UP", "DOWN", "LEFT", or "RIGHT")
                "priority": The bots move one at a time, so give the priority which you want them to act in (1,2, or 3)
    """
    def do_turn(self):
        my_units = self.get_my_units()
        decision = []

        for unit in my_units:
            if unit.id in [1, 4]:
                decision.append(self.unit_one_actions)
            elif unit.id in [2, 5]:
                decision.append(self.unit_two_actions)
            elif unit.id in [3, 6]:
                decision.append(self.unit_three_actions)

        return decision

    def clamp_movement(self, unit, directions=[]):
        if len(directions) < unit.speed:
            directions += (unit.speed - len(directions)) * ["STAY"]
        if len(directions) > unit.speed:
            directions = directions[:unit.speed]
        return directions

    def unit_one_actions(self):
        results = {
                "priority": 3,
                "movement": self.clamp_movement(unit, []),
                "attack": "STAY",
                "unitId": 1 if self.player_id == 1 else 4
                }
        return results

    def unit_two_actions(self):
        results = {
                "priority": 3,
                "movement": self.clamp_movement(unit, []),
                "attack": "STAY",
                "unitId": 2 if self.player_id == 1 else 5
                }
        return results

    def unit_three_actions(self):
        results = {
                "priority": 3,
                "movement": self.clamp_movement(unit, []),
                "attack": "STAY",
                "unitId": 3 if self.player_id == 1 else 6
                }
        return results
