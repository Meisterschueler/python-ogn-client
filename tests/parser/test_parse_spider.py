from ogn.parser.aprs_comment.spider_parser import SpiderParser


def test_position_comment():
    message = SpiderParser().parse_position("id300234060668560 +30dB K23W 3D")

    assert message['spider_id'] == "300234060668560"
    assert message['signal_power'] == 30
    assert message['spider_registration'] == "K23W"
    assert message['gps_quality'] == "3D"
