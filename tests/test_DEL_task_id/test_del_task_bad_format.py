import httpx
from secondary_func import create_task, del_task

def test_del_task_bad_format():
    
    negativ_task_id = "task_21547"
    
    #отправляем negativ_task_id на удаление
    del_response = del_task(negativ_task_id)
    del_data = del_response.json()

    assert del_response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {del_response.status_code}"

    assert del_data['deleted_task_id'] == negativ_task_id





