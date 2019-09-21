import sys
import random
from API import Game, Position


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

        unit1["health"] = 4
        unit1["speed"] = 4
        # creation of 2d lists
        unit1["attackPattern"] = [
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 2, 2, 2, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        unit1["terrainPattern"] = [
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False,  False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False]]
        units.append(unit1)

        # Setup for Bot 2
        unit2 = dict()
        unit2["unitId"] = 2
        if self.player_id == 2:
            unit2["unitId"] += 3

        unit2["health"] = 4
        unit2["speed"] = 4
        # creation of 2d lists
        unit2["attackPattern"] = [
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 2, 2, 2, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        unit2["terrainPattern"] = [
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False]]
        units.append(unit2)

        # Setup for Bot 3
        unit3 = dict()
        unit3["unitId"] = 3
        if self.player_id == 2:
            unit3["unitId"] += 3

        unit3["health"] = 4
        unit3["speed"] = 4
        # creation of 2d lists
        unit3["attackPattern"] = [
            [0, 0, 0, 2, 0, 0, 0],
            [0, 0, 2, 2, 2, 0, 0],
            [0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0]]
        unit3["terrainPattern"] = [
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False],
            [False, False, False, False, False, False, False]]
        units.append(unit3)

        self.taken_spots = list()

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
        self.taken_spots = list()
        for i in range(12):
            for j in range(12):
                checked_tile = self.get_tile((i, j))
                if checked_tile.type == 'DESTRUCTIBLE':
                    self.taken_spots.append((i, j))
        for unit in self.get_my_units():
            self.taken_spots.append((unit.pos.x, unit.pos.y))

        print('taken_spots:' + str(self.taken_spots), file=sys.stderr)

        my_units = self.get_my_units()
        decision = []

        for unit in my_units[::-1]:
            print(unit.speed, file=sys.stderr)
            if unit.id in [1, 4]:
                decision.append(self.unit_one_actions(unit))
            elif unit.id in [2, 5]:
                decision.append(self.unit_two_actions(unit))
            elif unit.id in [3, 6]:
                decision.append(self.unit_three_actions(unit))

        print(decision, file=sys.stderr)
        print('taken_spots after apply_route: ' + str(self.taken_spots), file=sys.stderr)
        return decision

    #MOVE THIS GUY LAST
    def unit_one_actions(self, unit):
        results = {
                "priority": 3,
                "movement": "STAY",
                "attack": "STAY",
                "unitId": 1 if self.player_id == 1 else 4
                }

        target = random.choice(self.get_enemy_units())

        res = self.recon(unit.id)
        for key, item in res.items():
            if item[1] > 0 and item[0] == 0:
                results["attack"] = key
                break

        nearest_point = self.get_nearest_point(unit, Position({"x": 5, "y": 5}))
        print('nearest_point: ' + str(nearest_point), file=sys.stderr)
        to_enemy = self.path_to((unit.pos.x, unit.pos.y),
                                (nearest_point[0], nearest_point[1]) if nearest_point is not None else (0, 0),
                                self.taken_spots)
        to_enemy = self.clamp_movement(unit, to_enemy)
        results["movement"] = to_enemy
        end_x, end_y = self.apply_route(unit, to_enemy)
        self.taken_spots.append((end_x, end_y))

        return results

    def unit_two_actions(self, unit):
        results = {
                "priority": 2,
                "movement": "STAY",
                "attack": "STAY",
                "unitId": 2 if self.player_id == 1 else 5
                }

        target = random.choice(self.get_enemy_units())

        res = self.recon(unit.id)
        for key, item in res.items():
            if item[1] > 0 and item[0] == 0:
                results["attack"] = key
                break

        nearest_point = self.get_nearest_point(unit, Position({"x": 11, "y": 11}))
        print('nearest_point: ' + str(nearest_point), file=sys.stderr)
        to_enemy = self.path_to((unit.pos.x, unit.pos.y),
                                (nearest_point[0], nearest_point[1]) if nearest_point is not None else (0, 0),
                                self.taken_spots)
        to_enemy = self.clamp_movement(unit, to_enemy)
        results["movement"] = to_enemy
        end_x, end_y = self.apply_route(unit, to_enemy)
        self.taken_spots.append((end_x, end_y))

        return results

    def unit_three_actions(self, unit):
        results = {
                "priority": 1,
                "movement": "STAY",
                "attack": "STAY",
                "unitId": 3 if self.player_id == 1 else 6
                }

        target = random.choice(self.get_enemy_units())

        res = self.recon(unit.id)
        for key, item in res.items():
            if item[1] > 0 and item[0] == 0:
                results["attack"] = key
                break

        nearest_point = self.get_nearest_point(unit, Position({"x": 0, "y": 0}))
        print('nearest_point: ' + str(nearest_point), file=sys.stderr)
        to_enemy = self.path_to((unit.pos.x, unit.pos.y),
                                (nearest_point[0], nearest_point[1]) if nearest_point is not None else (0, 0),
                                self.taken_spots)
        to_enemy = self.clamp_movement(unit, to_enemy)
        results["movement"] = to_enemy
        end_x, end_y = self.apply_route(unit, to_enemy)
        self.taken_spots.append((end_x, end_y))

        return results

    def clamp_movement(self, unit, directions=None):
        if directions is None:
            directions = ["STAY"] * unit.speed
        elif len(directions) < unit.speed:
            directions += (unit.speed - len(directions)) * ["STAY"]
        elif len(directions) > unit.speed:
            directions = directions[:unit.speed]
        return directions

    def recon(self, unit_id):
        report = {"UP": None, "DOWN": None, "LEFT": None, "RIGHT": None}
        for direction in report.keys():
            hit_locations = self.get_positions_of_attack_pattern(unit_id, direction)
            f, e = 0, 0
            for unit in self.get_my_units():
                if unit.id == unit_id:
                    continue
                for loc in hit_locations:
                    if self.check_same_position(unit.pos, loc[0]):
                        f += 1
            for unit in self.get_enemy_units():
                for loc in hit_locations:
                    if self.check_same_position(unit.pos, loc[0]):
                        e += 1

            report[direction] = [f, e]
        return report

    def check_same_position(self, pos1, pos2):
        if pos1.x == pos2.x and pos1.y == pos2.y:
            return True
        return False

    def closest_spot_around(self, enemy_unit):
        pass

    def apply_route(self, unit, directions=None):
        unit_x = unit.pos.x
        unit_y = unit.pos.y
        if directions is None:
            return unit_x, unit_y
        for i in directions:
            if i == "UP":
                unit_y += 1
            elif i == "DOWN":
                unit_y -= 1
            elif i == "LEFT":
                unit_x -= 1
            elif i == "RIGHT":
                unit_x += 1
            unit_y = self.clamp(unit_y, 0, 11)
            unit_x = self.clamp(unit_x, 0, 11)
        return unit_x, unit_y

    def clamp(self, number, mini, maxi):
        return min(maxi, max(mini, number))

    def get_nearest_point(self, unit, position):
        for n in range(12):
            if self.path_to((unit.pos.x, unit.pos.y), (position.x+n, position.y), self.taken_spots) is not None:
                return [position.x+n, position.y]
            if self.path_to((unit.pos.x, unit.pos.y), (position.x-n, position.y), self.taken_spots) is not None:
                return [position.x-n, position.y]
            if self.path_to((unit.pos.x, unit.pos.y), (position.x, position.y+n), self.taken_spots) is not None:
                return [position.x, position.y+n]
            if self.path_to((unit.pos.x, unit.pos.y), (position.x, position.y-n), self.taken_spots) is not None:
                return [position.x, position.y-n]
        return None
