import httpx
from config import BASE_URL

def test_get_root():
    
    response = httpx.get(BASE_URL)

    assert response.status_code == httpx.codes.OK, f"Код ответа ожидался 200, по факту пришел {response.status_code}"
    #response_json = response.json
  
