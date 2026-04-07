import httpx
from secondary_func import create_task, get_task_id, update_task

def test_put_content_is_done_true():
    response = create_task(
        content = "5055",
        user_id = str,
        is_done = False
    )

    create_data = response.json()

    create_task_id = create_data['task']['task_id']
    create_user_id = create_data['task']['user_id']

    put_response = update_task(
        content = "100",
        user_id = create_user_id,
        task_id = create_task_id,
        is_done = True
    )

    update_data = put_response.json()
    put_task_id = update_data['updated_task_id']

    assert put_response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {put_response.status_code}"

    get_task_response = get_task_id(
        task_id = put_task_id
    )

    get_task_id_data = get_task_response.json()

    assert get_task_response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {get_task_response.status_code}"

    assert get_task_id_data['user_id'] == create_user_id, "is different"
    assert get_task_id_data['task_id'] == create_task_id, "is different"
    assert get_task_id_data['is_done'] == True, "is different"
