import pytest

from museum_admission import gallery_entry, group_discount, ticket_price


def test_ticket_price_rejects_invalid_category():
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price("visitor", 30, "tuesday", False)


def test_ticket_price_rejects_negative_age():
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)


@pytest.mark.parametrize(("age", "expected"), [(4, 0), (5, 300)])
def test_ticket_price_age_boundary(age, expected):
    assert ticket_price("adult", age, "tuesday", False) == expected


def test_ticket_price_monday():
    assert ticket_price("adult", 30, "monday", False) == 150


def test_ticket_price_non_monday_weekday():
    assert ticket_price("adult", 30, "tuesday", False) == 300


@pytest.mark.parametrize("day", ["saturday", "sunday"])
def test_ticket_price_weekend(day):
    assert ticket_price("adult", 30, day, False) == 350


def test_ticket_price_guided_tour_disabled():
    assert ticket_price("student", 20, "tuesday", False) == 150


def test_ticket_price_student_guided_tour():
    assert ticket_price("student", 20, "tuesday", True) == 200


def test_ticket_price_nonstudent_guided_tour():
    assert ticket_price("adult", 30, "tuesday", True) == 400


def test_group_discount_rejects_invalid_group_size():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, True)


def test_group_discount_school_at_twenty():
    assert group_discount(20, True) == 40


def test_group_discount_school_below_twenty():
    assert group_discount(19, True) == 25


def test_group_discount_non_school_at_fifteen():
    assert group_discount(15, False) == 20


def test_group_discount_non_school_below_fifteen():
    assert group_discount(14, False) == 10


def test_group_discount_non_school_at_eight():
    assert group_discount(8, False) == 10


def test_group_discount_non_school_below_eight():
    assert group_discount(7, False) == 0


def test_gallery_waits_when_visitors_reach_capacity():
    assert gallery_entry(10, 10, False) == "wait"


def test_gallery_queues_at_ninety_percent_without_timed_slot():
    assert gallery_entry(9, 10, False) == "queue"


def test_gallery_enters_at_ninety_percent_with_timed_slot():
    assert gallery_entry(9, 10, True) == "enter"


def test_gallery_enters_below_ninety_percent_without_timed_slot():
    assert gallery_entry(8, 10, False) == "enter"
