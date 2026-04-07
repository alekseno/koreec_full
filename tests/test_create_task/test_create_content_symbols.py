import httpx
from secondary_func import create_task

def test_create_content_symbols():
    response = create_task(
        content = "!#$%&()*+-/;:<=>@[]^`{}~{}|/",
        user_id = "str",
        is_done = False
    )
    data = response.json()

    assert response.status_code == httpx.codes.OK, f"Ожидался код 200, пришел {response.status_code}"

    assert data['task']['content'] == "!#$%&()*+-/;:<=>@[]^`{}~{}|/", "данные в поле content отличаются от запроса"

    assert data['task']['is_done'] == False, "данные в поле is_done отличаются от запроса"