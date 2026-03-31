import httpx
from secondary_func import create_task, get_task_id, template_check_task_id

def test_get_check_task_id_uuid():
    response = create_task(
        content = "check  get uuid",
        user_id = str, 
        is_done = False
    )
    create_data = response.json()
    create_data_task_id = create_data['task']['task_id']
    
    #получаем task_id методом get
    task_id_response = get_task_id(create_data_task_id)
    get_task_id_d = task_id_response.json()
    get_task_id_data = get_task_id_d["task_id"]

    # проверка формата task_id с регуляркой
    temp_check_task_id = template_check_task_id(get_task_id_data)

    # сравниваем task_id методом get c регуляркой
    assert get_task_id_data == temp_check_task_id, "uuid check different"