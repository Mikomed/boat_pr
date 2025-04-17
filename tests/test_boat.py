import pytest
from src.boat import Boat

@pytest.fixture
def boat():
    return Boat()

def test_row_increases_speed(boat):
    boat.row()
    assert boat.get_speed() == 2

def test_stop_resets_speed(boat):
    boat.row()
    boat.stop()
    assert boat.get_speed() == 0

def test_turn_left_changes_direction(boat):
    boat.row()
    boat.turn_left()
    assert boat.get_direction() == 330

def test_turn_right_changes_direction(boat):
    boat.row()
    boat.turn_right()
    assert boat.get_direction() == 30

def test_cannot_turn_when_stopped(boat):
    boat.turn_left()
    assert boat.get_direction() == 0