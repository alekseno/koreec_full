import httpx
from secondary_func import minus_user_id

def test_minus_user_id():
    minus_user_ids = minus_user_id(
        content = "del user_id",
        is_done = False
    )
    expected_result = 'Internal Server Error'
    assert minus_user_ids.status_code == httpx.codes.INTERNAL_SERVER_ERROR, f'Ожидался код 500, пришел {minus_user_ids.status_code}'

    assert minus_user_ids.text == expected_result, f"Изменился код ошибки(был 500)"


    

     