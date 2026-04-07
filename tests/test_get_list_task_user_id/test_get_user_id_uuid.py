import httpx
from secondary_func import create_task, get_user_id, template_check_user_id

def test_get_user_id_uuid():
    response = create_task(
        content = "check user_id uuid",
        user_id = str,
        is_done = False
    )

    data_response = response.json()
    create_user_id = data_response['task']['user_id']

    # получаем user_id методом get
    get_response = get_user_id(create_user_id)
    get_data = get_response.json()
    get_user_id_data = get_data['tasks'][0]['user_id']

    # проверка формата user_id (get) с регуляркой
    assert template_check_user_id(get_user_id_data)
