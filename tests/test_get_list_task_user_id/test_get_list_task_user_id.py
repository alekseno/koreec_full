import httpx
from secondary_func import create_task, get_user_id, create_many_tasks

def test_get_list_task_user_id():
    create_response = create_task(
        content = "test №1",
        user_id = "str",
        is_done = False
    )
    create_response_data = create_response.json()
    create_user_id = create_response_data['task']['user_id']
    create_data = create_response_data
    
    assert create_response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {create_response.status_code}"
    
    # 2 задача, юзер из create
    task_two = create_many_tasks(
        content = "test #2",
        user_id = create_user_id,
        is_done = False
    )
    task_two_response = task_two.json()
    task_two_user_id = task_two_response['task']['user_id']
    task_two_data = task_two_response

    # 3-я задача, юзер из create
    task_three = create_many_tasks(
        content = "test #3",
        user_id = create_user_id,
        is_done = False
    )
    task_three_response = task_three.json()
    task_three_user_id = task_three_response['task']['user_id']
    task_three_data = task_three_response

    get_tasks = get_user_id(
        user_id = create_user_id
    ) 
    get_tasks_response = get_tasks.json()
    get_tasks_data = get_tasks_response['tasks'] 
    
    assert get_tasks.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {get_tasks.status_code}"

    # проверка, что юзер один и тот же
    assert get_tasks_data[0]['user_id'] == get_tasks_data[1]['user_id'] == get_tasks_data[2]['user_id'] == create_user_id == task_three_user_id == task_two_user_id 

    # 1 вариант сравнения контента
    assert get_tasks_data[0]['content'] == "test #3"
    assert get_tasks_data[1]['content'] == "test #2"
    assert get_tasks_data[2]['content'] == "test №1"  

    # 2 вариант сравнения контента
    assert get_tasks_data[2]['content'] == create_data['task']['content']
    assert get_tasks_data[1]['content'] == task_two_data['task']['content']
    assert get_tasks_data[0]['content'] == task_three_data['task']['content']  

    #сранение task_id каждой задачи, должны быть разные
    assert get_tasks_data[2]['task_id'] == create_data['task']['task_id']
    assert get_tasks_data[1]['task_id'] == task_two_data['task']['task_id']
    assert get_tasks_data[0]['task_id'] == task_three_data['task']['task_id']  

    assert get_tasks_data[0]['task_id'] != task_two_data['task']['task_id'] 
    assert get_tasks_data[0]['task_id'] != create_data['task']['task_id'] 
    
    
    





"""    assert get_user_data['tasks'][0]['user_id'] == post_user_id, "[get_user_id] and [post_user_id] is different"

    assert get_user_data['tasks'][0]['content'] == data['task']['content'] 
    assert get_user_data['tasks'][0]['task_id'] == data['task']['task_id'] """
    
"""#ЗАДАНИЕ: нужно првоерить, что апи возвращает действительно список всех тасок. Для этого нужно у одного пользователя создать несколько тасок, и может быть пару у другого, После чего получить таски для одного и для другого и проверить, что все таски которые ты создавала ушли правильным пользователям. 
у тебя оба теста из этой директории делают не то. нужно не только user_id сравнить а в целом количество тасок которые подгружаются у данного пользователя."""