import httpx
from secondary_func import create_task

def test_create_content_int():
    response = create_task(
        content = "1023456789",
        user_id = str,
        is_done = False
)
    data = response.json()

    assert response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {response.status_code}"

    assert data['task']['content'] == "1023456789", "[content] is different"

    assert data['task']['is_done'] == False, "[is_done] is different"