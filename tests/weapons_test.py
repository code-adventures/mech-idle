#
#    Mech Idle - an idle mech game
#    Copyright (C) 2024 Code Adventures
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from src.mech_idle.vec import Vec2
from src.mech_idle import weapons
from src.mech_idle import weapon_effects
from src.mech_idle.hull import MountPoints

class source_target_mock():
    def __init__(self):
        self.speed = 10

    def get_pos(self):
        return Vec2(0, 0)

    def get_pos_at(self, time):
        return Vec2(0, 0)

    def dist_to_mech(self):
        return 10

def test_create_effect():
    source = source_target_mock()
    target = source_target_mock()
    time = 0
    duration = 100
    effect = weapon_effects.create_effect(weapon_effects.WeaponEffects.ROCKET, source, MountPoints.LEFT_ARM, target, time, duration)
    assert isinstance(effect, weapon_effects.Rocket)

    effect = weapon_effects.create_effect(weapon_effects.WeaponEffects.BEAM, source, MountPoints.LEFT_ARM, target, time, duration)
    assert isinstance(effect, weapon_effects.Beam)

    effect = weapon_effects.create_effect(weapon_effects.WeaponEffects.BULLET, source, MountPoints.LEFT_ARM, target, time, duration)
    assert isinstance(effect, weapon_effects.Bullet)

def test_weapon_find_enemy():
    target = source_target_mock()
    weapon = weapons.AutoCannon()
    enemy = weapon.find_enemy([(target, 10)])
    assert enemy == target

def test_weapon_find_enemy_enemy_to_far():
    target = source_target_mock()
    weapon = weapons.AutoCannon()
    enemy = weapon.find_enemy([(target, 2000)])
    assert enemy is None

def test_weapon_find_enemy_no_enemies():
    target = source_target_mock()
    weapon = weapons.BeamLaser()
    enemy = weapon.find_enemy([])
    assert enemy is None
    
def test_weapon_shoot(mocker):
    source = source_target_mock()
    target = source_target_mock()
    weapon = weapons.AutoCannon()
    mocker.patch('src.mech_idle.weapons.Weapon.find_enemy', return_value=target)
    m = mocker.patch('src.mech_idle.weapons.create_effect')
    weapon.shoot(source, MountPoints.LEFT_ARM, 1000, [target])
    assert weapon.last_shot == 1000
    m.assert_called_once()

def test_weapon_shoot_no_enemy_in_range(mocker):
    source = source_target_mock()
    target = source_target_mock()
    weapon = weapons.AutoCannon()
    mocker.patch('src.mech_idle.weapons.Weapon.find_enemy', return_value=None)
    m = mocker.patch('src.mech_idle.weapons.create_effect')
    weapon.shoot(source, MountPoints.LEFT_ARM, 1000, [target])
    assert weapon.last_shot == 0
    m.assert_not_called()

def test_weapon_shoot_no_enemy(mocker):
    source = source_target_mock()
    weapon = weapons.AutoCannon()
    m = mocker.patch('src.mech_idle.weapons.create_effect')
    weapon.shoot(source, MountPoints.LEFT_ARM, 1000, [])
    assert weapon.last_shot == 0
    m.assert_not_called()
