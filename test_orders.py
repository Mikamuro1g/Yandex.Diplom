import create_orders
import data


def test_number_one():
    response_created_orders = create_orders.post_create_order(data.create_orders)
    assert response_created_orders.status_code == 201
def test_number_two():
    response_get_orders = create_orders.get_order()
    assert response_get_orders.status_code == 200