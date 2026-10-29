import pytest

from museum_admission import gallery_entry, group_discount, ticket_price


def test_ticket_price_rejects_unknown_category():
    with pytest.raises(ValueError, match="unknown category"):
        ticket_price("visitor", 30, "tuesday", False)


def test_ticket_price_rejects_negative_age():
    with pytest.raises(ValueError, match="invalid age"):
        ticket_price("adult", -1, "tuesday", False)


@pytest.mark.parametrize("age", [0, 4])
def test_ticket_price_is_free_for_children_under_five(age):
    assert ticket_price("adult", age, "saturday", True) == 0


def test_ticket_price_regular_weekday():
    assert ticket_price("adult", 30, "tuesday", False) == 300


def test_ticket_price_monday_discount_uses_integer_division():
    assert ticket_price("student", 20, "monday", False) == 75


@pytest.mark.parametrize("day", ["saturday", "sunday"])
def test_ticket_price_weekend_surcharge(day):
    assert ticket_price("child", 10, day, False) == 150


def test_ticket_price_student_guided_tour_surcharge():
    assert ticket_price("student", 20, "tuesday", True) == 200


def test_ticket_price_nonstudent_guided_tour_surcharge():
    assert ticket_price("senior", 70, "tuesday", True) == 300


def test_ticket_price_combines_weekend_and_tour_surcharges():
    assert ticket_price("adult", 30, "sunday", True) == 450


def test_group_discount_rejects_group_size_below_one():
    with pytest.raises(ValueError, match="invalid group size"):
        group_discount(0, False)


def test_school_group_discount_at_twenty_visitors():
    assert group_discount(20, True) == 40


def test_school_group_discount_below_twenty_visitors():
    assert group_discount(19, True) == 25


def test_non_school_discount_at_fifteen_visitors():
    assert group_discount(15, False) == 20


def test_non_school_discount_at_eight_visitors():
    assert group_discount(8, False) == 10


def test_small_non_school_group_has_no_discount():
    assert group_discount(7, False) == 0


def test_gallery_waits_when_capacity_is_reached():
    assert gallery_entry(10, 10, True) == "wait"


def test_gallery_waits_when_over_capacity():
    assert gallery_entry(11, 10, False) == "wait"


def test_gallery_queues_at_ninety_percent_without_timed_slot():
    assert gallery_entry(9, 10, False) == "queue"


def test_gallery_allows_timed_slot_at_ninety_percent_capacity():
    assert gallery_entry(9, 10, True) == "enter"


def test_gallery_allows_entry_below_ninety_percent_capacity():
    assert gallery_entry(8, 10, False) == "enter"
