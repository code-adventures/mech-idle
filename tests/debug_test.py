
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

import imgui
from src.mech_idle import debug

def test_add_msg():
    debug.add_msg("test")
    assert debug.msgs == ["test"]
    debug.add_msg("test2")
    assert  debug.msgs == ["test", "test2"]
        
    for i in range(11):
         debug.add_msg(f"test{i}")
    assert debug.msgs == ["test1", "test2", "test3", "test4", "test5", "test6", "test7", "test8", "test9", "test10"]

def test_clear_msgs():
    debug.add_msg("test")
    debug.add_msg("test2")
    debug.clear_msgs()
    assert debug.msgs == []

def test_print_msgs(mocker):
    debug.clear_msgs()
    debug.add_msg("test")
    debug.add_msg("test2")
    mocker.patch('imgui.text')
    debug.print_msgs()
    imgui.text.assert_has_calls([mocker.call("test"), mocker.call("test2")])
