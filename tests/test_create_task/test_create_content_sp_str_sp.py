import httpx
from secondary_func import create_task

def test_create_content_sp_str_sp():
    response = create_task(
        content = " чашка ",
        user_id = str,
        is_done = False
    )

    data = response.json()

    assert response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {response.status_code}"

    assert data['task']['content'] == " чашка ", "[content] is different"
    assert data['task']['is_done'] == False, "[is_done] is different"