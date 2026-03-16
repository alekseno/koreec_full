import httpx
from secondary_func import create_task

def test_create_is_done_true():
    response = create_task(
        content = "my task",
        user_id = str,
        is_done = True
        
    )
    data = response.json()

    assert response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {response.status_code}"

    assert data['task']['content'] == "my task", "[content] is differetn"
    assert data['task']['is_done'] == False, "[is_done] is different"