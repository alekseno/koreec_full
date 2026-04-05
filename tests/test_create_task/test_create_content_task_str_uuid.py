import httpx
from secondary_func import create_task, template_check_task_id

def test_create_content_task_str():
    response = create_task(
        content = "task_None",
        user_id = str,
        is_done = False
    )

    data_response = response.json()
    create_task_id = data_response['task']['task_id']

    temp_check_task_id = template_check_task_id(create_task_id)
    
    #проверка формата, длины task_id
    assert create_task_id == temp_check_task_id, "формат task_id не соответствует шаблону"
    assert isinstance(create_task_id, str), "формат task_id не строка"
    assert create_task_id is not None
    assert len(create_task_id) == 37, "task_id не 37 символов"
    assert create_task_id.startswith('task_'), "строка начинается не с task_"
