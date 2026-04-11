import httpx
from secondary_func import minus_is_done

def test_create_minus_is_done():
    minus_is_dones = minus_is_done(
        content = "minus is_done",
        user_id = "str"
    )
    minus_is_done_response = minus_is_dones.json()
    minus_is_done_data = minus_is_done_response

    assert minus_is_dones.status_code == httpx.codes.OK, f'Ожидался код 200, пришел {minus_is_dones.status_code}'

    assert minus_is_done_data['task']['content'] == "minus is_done", "Поле content не соответствует ожидаемому результату"
    