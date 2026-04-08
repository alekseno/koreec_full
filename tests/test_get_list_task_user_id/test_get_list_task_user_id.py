import httpx
from secondary_func import create_task, get_user_id, create_many_tasks

def test_get_list_task_user_id():
    create_response = create_task(
        content = "test #1",
        user_id = "str",
        is_done = False
    )
    task_one_response = create_response.json()
    task_one_user_id = task_one_response['task']['user_id']
    task_one_data = task_one_response
    
    assert create_response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {create_response.status_code}"
    
    # 2 задача
    task_two = create_many_tasks(
        content = "test #2",
        user_id = task_one_user_id,
        is_done = False
    )
    task_two_response = task_two.json()
    task_two_user_id = task_two_response['task']['user_id']
    task_two_data = task_two_response

    # 3-я задача, 
    task_three = create_many_tasks(
        content = "test #3",
        user_id = task_one_user_id,
        is_done = False
    )
    task_three_response = task_three.json()
    task_three_user_id = task_three_response['task']['user_id']
    task_three_data = task_three_response

    get_tasks = get_user_id(
        user_id = task_one_user_id
    ) 
    get_tasks_response = get_tasks.json()
    get_tasks_data = get_tasks_response['tasks'] 

    assert get_tasks.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {get_tasks.status_code}"

    #              проверка, что юзер один и тот же
    user_ids = [
        get_tasks_data[0]['user_id'],
        get_tasks_data[1]['user_id'],
        get_tasks_data[2]['user_id'],
        task_one_user_id,
        task_two_user_id,
        task_three_user_id
    ]
    # set удаляет дубликаты, len считает, сколько уникалыных user_id
    assert len(set(user_ids)) == 1, f"Найдены разные user_id:{set(user_ids)}. Список всех id: {user_ids}"

    #                 сравнение content
    # ===========1 вариант сравнения 
    #ожидаемый результат
    expected_contents = ["test #3", "test #2", "test #1"] 

    # фактический результат
    actual_content = [
        get_tasks_data[0]['content'],
        get_tasks_data[1]['content'],
        get_tasks_data[2]['content']
    ]
    assert actual_content == expected_contents

    # ==============2 вариант  сравнения
    assert [task['content'] for task in get_tasks_data] == ["test #3", "test #2", "test #1"]

    # ========3 вариант сравнения
    expected_contents_2 = [
        task_one_data['task']['content'],
        task_two_data['task']['content'],
        task_three_data['task']['content']
    ]
    assert expected_contents_2[::-1] == actual_content


    #             проверка, что task_id разные
    task_ids = [
        get_tasks_data[0]['task_id'],
        get_tasks_data[1]['task_id'],
        get_tasks_data[2]['task_id']
    ]
    assert len(set(task_ids)) == 3, f"Найдены одинаковые task_id: {set(task_ids)}. Список task_id: {task_ids}"





"""
for task in get_tasks_data:
        if task['task_id'] == task_one_data['task']['task_id']:
            assert task['content'] == "test №1"
            assert task['user_id'] == task_one_user_id
        elif task['task_id'] == task_two_data['task']['task_id']:
            assert task['content'] == "test #2"
        elif task['task_id'] == task_three_data['task']['task_id']:
            assert task['content'] == "test #3"

assert [task['content'] for task in get_tasks_data[:3]] == ["test #3", "test #2", "test №1"]

    #сранение task_id каждой задачи, должны быть разные
    assert get_tasks_data[2]['task_id'] == task_one_data['task']['task_id']
    assert get_tasks_data[1]['task_id'] == task_two_data['task']['task_id']
    assert get_tasks_data[0]['task_id'] == task_three_data['task']['task_id']  

    assert get_tasks_data[0]['task_id'] != task_two_data['task']['task_id'] 
    assert get_tasks_data[0]['task_id'] != task_one_data['task']['task_id'] 
    
     # 1 вариант сравнения контента
    assert get_tasks_data[0]['content'] == "test #3"
    assert get_tasks_data[1]['content'] == "test #2"
    assert get_tasks_data[2]['content'] == "test №1"  

    # 2 вариант сравнения контента
    assert get_tasks_data[2]['content'] == task_one_data['task']['content']
    assert get_tasks_data[1]['content'] == task_two_data['task']['content']
    assert get_tasks_data[0]['content'] == task_three_data['task']['content']  """