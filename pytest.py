import datetime
import pytest
from main import read_data_from_file, get_price_changes_for_product


@pytest.fixture
def sample_data():
    return [
        ['Product A', '2023-03-01', '10.0'],
        ['Product A', '2023-03-05', '12.0'],
        ['Product B', '2023-03-05', '20.0'],
        ['Product A', '2023-04-01', '15.0'],
        ['Product A', '2023-04-03', '17.0']
    ]


def test_read_data_from_file():
    filename = 'sample_data.txt'
    expected_output = [
        ['Product A', '2023-03-01', '10.0'],
        ['Product A', '2023-03-05', '12.0'],
        ['Product B', '2023-03-05', '20.0'],
        ['Product A', '2023-04-01', '15.0'],
        ['Product A', '2023-04-03', '17.0']
    ]
    assert read_data_from_file(filename) == expected_output


def test_get_price_changes_for_product(sample_data):
    product_name = 'Product A'
    expected_output = [
        (datetime.date(2023, 4, 1), 15.0),
        (datetime.date(2023, 4, 3), 17.0)
    ]
    assert get_price_changes_for_product(product_name, sample_data) == expected_output


def test_get_price_changes_for_product_empty(sample_data):
    product_name = 'Product C'
    expected_output = []
    assert get_price_changes_for_product(product_name, sample_data) == expected_output


@pytest.mark.parametrize("product_name, expected_output", [
    ('Product A', [
        (datetime.date(2023, 4, 1), 15.0),
        (datetime.date(2023, 4, 3), 17.0)
    ]),
    ('Product B', [
        (datetime.date(2023, 3, 5), 20.0)
    ]),
    ('Product C', [])
])
def test_get_price_changes_for_product_parametrized(sample_data, product_name, expected_output):
    assert get_price_changes_for_product(product_name, sample_data) == expected_output
