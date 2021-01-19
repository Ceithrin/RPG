from unittest import TestCase
from unittest.mock import patch
from fight import Fight
from character import Player, Enemy
from spells import Spell


class TestFight(TestCase):

    @patch('fight.input', return_value=1)
    def test_fight_win(self, input):
        player = Player("Player")
        default = Spell('Default', player.atk, 0)
        player.available_spells = [default]
        enemy = Enemy("Enemy", 50, 20, 10)
        fight = Fight(player, enemy)
        fight.fight()
        self.assertEqual(fight.enemy.hp, 0)

    @patch('fight.input', return_value=1)
    def test_fight_lose(self, input):
        player = Player("Player")
        default = Spell('Default', player.atk, 0)
        player.available_spells = [default]
        enemy = Enemy("Enemy", 500, 50, 10)
        fight = Fight(player, enemy)
        with self.assertRaises(SystemExit) as cm:
            fight.fight()
        self.assertEqual(cm.exception.code, None)
