import configuration
import data
import requests

def post_create_order(body):
    return requests.post(url=configuration.URL + configuration.CREATE_ORDER,
                         json=body)

def save_track():
    order_track = post_create_order(data.create_orders)
    order_track_number= order_track.json()["track"]
    return order_track_number

def get_order ():
    track = save_track()
    return requests.get(configuration.URL + configuration.GET_ORDER_TRACK + str(track))