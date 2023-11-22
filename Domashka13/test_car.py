import pytest
import random


@pytest.mark.smoke
def test_change_model(get_new_car):
    new_car = get_new_car
    tesla_models = ['X', "3", "Y"]
    expected_model = f'Tesla Model {random.choice(tesla_models)}'
    new_car.model = expected_model
    assert new_car.model == expected_model


@pytest.mark.smoke
def test_check_default_limit(get_new_car):
    new_car = get_new_car
    fresh_car_limit = new_car.miles_limit
    assert fresh_car_limit == 0



@pytest.mark.sanity
def test_start_engine(get_new_car):
    new_car = get_new_car
    assert new_car.start_engine() == "Engine started."


@pytest.mark.sanity
def test_started_engine(get_new_car):
    new_car = get_new_car
    new_car.start_engine()
    assert new_car.start_engine() == "Engine is already running."


@pytest.mark.sanity
def test_stop_engine(get_new_car):
    new_car = get_new_car
    assert new_car.stop_engine() == "Engine stopped."


@pytest.mark.sanity
def test_stopped_engine(get_new_car):
    new_car = get_new_car
    new_car.stop_engine()
    assert new_car.stop_engine() == "Engine is already off."


@pytest.mark.sanity
def test_driving_without_started_engine(get_new_limit_car):
    new_car = get_new_limit_car
    assert new_car.drive(130) == "Cannot drive. Engine is off."


@pytest.mark.sanity
def test_driving(get_new_limit_car):
    new_car = get_new_limit_car
    miles_to_drive = 130
    new_car.start_engine()
    assert new_car.drive(miles_to_drive) == f"Driving {miles_to_drive} miles."


@pytest.mark.sanity
def test_exceeded_driving(get_new_limit_car):
    new_car = get_new_limit_car
    miles_to_drive = 500
    new_car.start_engine()
    assert new_car.drive(miles_to_drive) == "The miles limit has been exceeded"


@pytest.mark.sanity
def test_driving_until_limit(get_new_limit_car):
    new_car = get_new_limit_car
    miles_to_drive = 300
    new_car.start_engine()
    new_car.drive(miles_to_drive)
    new_car.drive(miles_to_drive)
    assert new_car.drive(miles_to_drive) == "The miles limit has been exceeded"


@pytest.mark.negative
def test_not_existing_model(get_new_car):
    new_car = get_new_car
    existing_models = ['Model X', "Model 3", "Model Y", "Model S"]
    test_model = 'Model M'
    new_car.model = test_model
    if test_model not in existing_models:
        raise ValueError(f"{test_model} is not a valid model")
