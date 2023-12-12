import pytest


def test_insert_one(cosmetics_repo):
    db = cosmetics_repo
    start = db.get_all()
    db.insert_one('Moisturizer', 'Skincare', 120, 'Nivea', 1)
    updated = db.get_all()
    assert len(start) + 1 == len(updated)


def test_update_one(cosmetics_repo):
    db = cosmetics_repo
    test_id = db.get_the_last_row_id()
    db.update_one_by_id(test_id, 'UpdatedMoisturizer', 'UpdatedType', 60.0, 'UpdatedManufacturer', 0)
    updated = db.get_one_by_id(test_id)
    assert updated is not None
    assert updated[1] == 'UpdatedMoisturizer'


def test_delete_one_by_id(cosmetics_repo):
    db = cosmetics_repo
    db.insert_one('Moisturizer', 'Skincare', 120, 'Nivea', 1)
    test_id = db.get_the_last_row_id()
    db.delete_one_by_id(test_id)
    cosmetics = db.get_one_by_id(test_id)
    assert cosmetics is None


def test_delete_last_row(cosmetics_repo):
    db = cosmetics_repo
    db.insert_one('Moisturizer', 'Skincare', 120, 'Nivea', 1)
    test_id = db.get_the_last_row_id()
    db.delete_last_row()
    cosmetics = db.get_one_by_id(test_id)
    assert cosmetics is None


def test_get_one_by_id(cosmetics_repo):
    db = cosmetics_repo
    db.insert_one('Moisturizer', 'Skincare', 120, 'Nivea', 1)
    test_id = db.get_the_last_row_id()
    cosmetic = db.get_one_by_id(test_id)
    assert cosmetic is not None
    assert cosmetic[1] == 'Moisturizer'


@pytest.mark.negative
def test_failing_of_adding_forbidden_availability(cosmetics_repo):
    db = cosmetics_repo
    try:
        db.insert_one('Moisturizer', 'Skincare', 120, 'Nivea', 3)
        assert False, "Expected an exception for inserting a row with forbidden availability"
    except Exception as error:
        assert "CHECK constraint failed" in str(error), f"Unexpected exception: {error}"


@pytest.mark.negative
def test_failing_of_deleting_not_existing_id(cosmetics_repo):
    db = cosmetics_repo
    try:
        test_id = db.get_the_last_row_id()
        not_existing = test_id + 1
        db.delete_one_by_id(not_existing)
        assert False, "Expected an exception for deleting not existing ID"
    except Exception as error:
        assert isinstance(error, Exception), f"Unexpected exception: {error}"
        assert "not exist" in str(error), f"Unexpected exception message: {error}"



