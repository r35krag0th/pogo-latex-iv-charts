import json
import math
from pogoiv.constants import CombatPointsMultiplier


def level_to_cpm(level):
    return CombatPointsMultiplier[level_to_level_index(level)]


def level_to_level_index(level):
    return (level - 1) * 2


def level_index_to_level(level_index):
    return (level_index * 0.5) + 1


class Pokemon:
    id = None
    name = None
    base_attack = None
    base_defense = None
    base_stamina = None

    def __init__(self, id, name, attack, defense, stamina):
        self.id = id
        self.name = name
        self.base_attack = attack
        self.base_defense = defense
        self.base_stamina = stamina

    def iv_from_stats(self, level, attack, defense, stamina):
        multiplier = level_to_cpm(level)
        cp = math.floor((self.base_attack + attack) * math.sqrt(self.base_defense + defense) * math.sqrt(self.base_stamina + stamina) * math.pow(multiplier, 2) * 0.1)

        return IndividualValue(level, cp, attack, defense, stamina)

    @staticmethod
    def from_json(json_data):
        return Pokemon(
            id=int(json_data['dex']),
            name=json_data['name'],
            attack=json_data['stats']['baseAttack'],
            defense=json_data['stats']['baseDefense'],
            stamina=json_data['stats']['baseStamina'],
        )


class IndividualValue:
    _level = None
    _cp = None

    _attack = None
    _defense = None
    _stamina = None

    _percent = None

    def __init__(self, level, cp, attack, defense, stamina):
        self._level = level
        self._cp = cp
        self._attack = attack
        self._defense = defense
        self._stamina = stamina

        self._percent = ((attack + defense + stamina) / 45.0) * 100

    @property
    def level(self):
        return self._level

    @property
    def cp(self):
        return self._cp

    @property
    def attack(self):
        return self._attack

    @property
    def defense(self):
        return self._defense

    @property
    def stamina(self):
        return self._stamina

    @property
    def perfection_percent(self):
        return self._percent

    @property
    def perfection_percent_rounded(self):
        return round(self._percent)

    def __repr__(self):
        return f'L{self.level} {self.attack}/{self.defense}/{self.stamina} ({self.perfection_percent:0.2f}%)'