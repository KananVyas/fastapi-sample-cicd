from app.main import read_item


def test_index():
    assert read_item(item_id=1) == {"item_id":1,"q":"hello_kanan"}