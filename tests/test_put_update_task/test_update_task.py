import httpx
from secondary_func import create_task, update_task, get_task_id

def test_put_update_task(): #создаем задачу
    response = create_task(
        content = "список покупок на субботу",
        user_id = str,
        is_done = False
    )

    create_data = response.json()#вытаскиваем данные
     
    task_id = create_data['task']['task_id']
    user_id = create_data['task']['user_id']

    put_response = update_task(
        content = "покупки на вторник",#обновляем задачу
        user_id = user_id,
        task_id = task_id,
        is_done = False
    )
    update_data = put_response.json()#получаем данные
    put_task_id = update_data['updated_task_id']#получаем task_id
    
    assert put_response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {put_response.status_code}"

    get_task = get_task_id(
        task_id = put_task_id#отправялем task_id, чтоб получить body
    )

    get_task_id_data = get_task.json()

    assert get_task_id_data['user_id'] == user_id, "is different"
    assert get_task_id_data['task_id'] == task_id, "is different"