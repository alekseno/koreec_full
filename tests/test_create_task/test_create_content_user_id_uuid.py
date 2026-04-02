import httpx
from secondary_func import create_task, template_check_user_id

def test_create_contetn_user_id_uuid():
    response = create_task(
        content = "check_uuid",
        user_id = str, 
        is_done = False
    )

    data_response = response.json()
    create_user_id = data_response['task']['user_id']

    temp_check_user_id = template_check_user_id(create_user_id)

    #проверка формата поля user_id
    assert create_user_id == temp_check_user_id, "uuid is different"

    assert isinstance(create_user_id, str), "is not str"
    assert isinstance(create_user_id, int) == False, "is int"
    assert isinstance(create_user_id, bool) == False, "is bool"
    assert isinstance(create_user_id, type(None)) == False, "is None"


    #проверки: user_id не пустое значение, не None (в этой API поле не работает)