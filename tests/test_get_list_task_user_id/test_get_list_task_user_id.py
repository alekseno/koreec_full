import httpx
from secondary_func import create_task, get_user_id

def test_get_list_task_user_id():
    put_response = create_task(
        content = "test №50",
        user_id = str,
        is_done = False
    )

    data = put_response.json()
    post_user_id = data['task']['user_id']

    get_user_response = get_user_id(post_user_id)

    assert get_user_response.status_code == httpx.codes.OK, f"ожидался код 200, пришел {get_user_response.status_code}"

    get_user_data = get_user_response.json()

    assert get_user_data['tasks'][0]['user_id'] == post_user_id, "[get_user_id] and [post_user_id] is different"

    assert get_user_data['tasks'][0]['content'] == data['task']['content'], "is different"
    assert get_user_data['tasks'][0]['task_id'] == data['task']['task_id'], "is different"
    
"""#ЗАДАНИЕ: нужно првоерить, что апи возвращает действительно список всех тасок. Для этого нужно у одного пользователя создать несколько тасок, и может быть пару у другого, После чего получить таски для одного и для другого и проверить, что все таски которые ты создавала ушли правильным пользователям. 
у тебя оба теста из этой директории делают не то. нужно не только user_id сравнить а в целом количество тасок которые подгружаются у данного пользователя."""