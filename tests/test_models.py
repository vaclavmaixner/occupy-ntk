from app import app
from app.models import Occupation
from datetime import datetime, timedelta


def new_occupation(id, f6, f5, f4, f3, ts):
    occ = Occupation(id=id,
                     floor_6_perc=f6,
                     floor_5_perc=f5,
                     floor_4_perc=f4,
                     floor_3_perc=f3,
                     timestamp=ts)
    return occ


def test_new_occupation():
    new_occ = new_occupation(id=1234, f6=11, f5=12,
                             f4=13, f3=140, ts=datetime(2001, 1, 1))

    assert new_occ.id == 1234
    assert new_occ.floor_6_perc == 11
    assert new_occ.floor_5_perc == 12
    assert new_occ.floor_4_perc == 13
    assert new_occ.floor_3_perc == 140
    assert new_occ.timestamp == datetime(2001, 1, 1)

    assert repr(new_occ) == '<Occupation {}>'.format(datetime(2001, 1, 1))


def test_zero_occupation():
    new_occ = new_occupation(id=0, f6=0, f5=0, f4=0,
                             f3=0, ts=datetime(2001, 1, 30))

    assert new_occ.id == 0
    assert new_occ.floor_6_perc == 0
    assert new_occ.floor_5_perc == 0
    assert new_occ.floor_4_perc == 0
    assert new_occ.floor_3_perc == 0
    assert new_occ.timestamp == datetime(2001, 1, 30)


def test_getters():
    new_occ = new_occupation(id=1234, f6=11, f5=36,
                             f4=100, f3=140, ts=datetime(2001, 1, 1))

    assert len(new_occ.get_number_of_people()) == 4
    assert new_occ.get_number_of_people().get('floor_6') == 36
    assert new_occ.get_number_of_people().get('floor_5') == 99
    assert new_occ.get_number_of_people().get('floor_4') == 333
    assert new_occ.get_number_of_people().get('floor_3') == 463

    assert len(new_occ.get_floors_as_list()) == 4
    assert new_occ.get_floors_as_list() == [11, 36, 100, 140]

    assert type(new_occ.get_sum_of_people()) == int
    assert new_occ.get_sum_of_people() == 931

    assert new_occ.get_overall_perc() == 74

    assert new_occ.get_tuple_sum_of_people() == (datetime(2001, 1, 1), 931)


def test_getters_zero_vals():
    new_occ = new_occupation(id=1234, f6=0, f5=0, f4=0,
                             f3=0, ts=datetime(2001, 1, 1))

    assert len(new_occ.get_number_of_people()) == 4
    assert new_occ.get_number_of_people().get('floor_6') == 0
    assert new_occ.get_number_of_people().get('floor_5') == 0
    assert new_occ.get_number_of_people().get('floor_4') == 0
    assert new_occ.get_number_of_people().get('floor_3') == 0

    assert len(new_occ.get_floors_as_list()) == 4
    assert new_occ.get_floors_as_list() == [0, 0, 0, 0]

    assert type(new_occ.get_sum_of_people()) == int
    assert new_occ.get_sum_of_people() == 0

    assert new_occ.get_overall_perc() == 0

    assert new_occ.get_tuple_sum_of_people() == (datetime(2001, 1, 1), 0)


def test_getters_overload():
    new_occ = new_occupation(id=1234, f6=110, f5=120,
                             f4=130, f3=140, ts=datetime(2001, 1, 1))

    assert len(new_occ.get_number_of_people()) == 4
    assert new_occ.get_number_of_people().get('floor_6') == 355
    assert new_occ.get_number_of_people().get('floor_5') == 330
    assert new_occ.get_number_of_people().get('floor_4') == 433
    assert new_occ.get_number_of_people().get('floor_3') == 463

    assert len(new_occ.get_floors_as_list()) == 4
    assert new_occ.get_floors_as_list() == [110, 120, 130, 140]

    assert type(new_occ.get_sum_of_people()) == int
    assert new_occ.get_sum_of_people() == 1581

    assert new_occ.get_overall_perc() == 125

    assert new_occ.get_tuple_sum_of_people() == (datetime(2001, 1, 1), 1581)
