import httpx
from secondary_func import create_task, del_task, get_task_id, get_user_id

def test_DEL_task_id():
    response = create_task(
        content = "delete_task",
        user_id = str,
        is_done = False
    )

    create_data = response.json()
    create_task_id = create_data['task']['task_id']
    create_user_id = create_data['task']['user_id']

    #удаление задачи
    del_response = del_task(create_task_id)
    del_data = del_response.json()

    assert del_response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {del_response.status_code}"

    assert del_data['deleted_task_id'] == create_task_id

    #проверка удаления задачи через task_id
    get_response = get_task_id(
        task_id = create_task_id
    )
    
    get_task_id_data = get_response.json()

    assert get_response.status_code == httpx.codes.NOT_FOUND, f"Ожидался код 404, пришел{get_response.status_code}"

    #проверка удаления задачи через user_id

    get_user_response = get_user_id(
        user_id = create_user_id
    )

    get_user_data = get_user_response.json

    assert get_user_response.status_code ==httpx.codes.OK, f"Ожидался код 200, пришел {get_user_response.status_code}"

    assert get_user_data, f"{'tasks'}" == [] 

    


