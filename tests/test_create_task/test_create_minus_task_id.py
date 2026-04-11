import httpx
from secondary_func import minus_task_id

def test_create_minus_task_id():
    minus_task_ids = minus_task_id(
        content = "del task_id",
        user_id = "str",
        is_done = False
    )
    minus_task_id_response = minus_task_ids.json()
    minus_task_id_data = minus_task_id_response

    assert minus_task_ids.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {minus_task_ids.status_code}"

    assert minus_task_id_data['task']['content'] == "del task_id", "Поле content не соответствует ожидаемому результату"
    assert minus_task_id_data['task']['is_done'] == False, "Поле is_done отличается от запроса"