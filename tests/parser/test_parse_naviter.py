import pytest

from ogn.parser.utils import FPM_TO_MS, HPM_TO_DEGS
from ogn.parser.aprs_comment.naviter_parser import NaviterParser


def test_OGNAVI_1():
    message = NaviterParser().parse_position("id0440042121 +123fpm +0.5rot")

    # id0440042121 == 0b0000 0100 0100 0000 0000 0100 0010 0001 0010 0001
    # bit 0: stealth mode
    # bit 1: do not track mode
    # bits 2-5: aircraft type
    # bits 6-11: address type (namespace is extended from 2 to 6 bits to avoid collisions with other tracking providers)
    # bits 12-15: reserved for use at a later time
    # bits 16-39: device id (24-bit device identifier, same as in APRS header)
    assert message['stealth'] is False
    assert message['do_not_track'] is False
    assert message['aircraft_type'] == 1
    assert message['address_type'] == 4
    assert message['reserved'] == 0
    assert message['address'] == "042121"

    assert message['climb_rate'] == pytest.approx(123 * FPM_TO_MS, 2)
    assert message['turn_rate'] == 0.5 * HPM_TO_DEGS
