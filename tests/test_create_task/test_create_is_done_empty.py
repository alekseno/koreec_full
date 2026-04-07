import httpx
from secondary_func import create_task

def test_create_is_done_empty():
    response = create_task(
        content = "green",
        user_id = "str",
        is_done = ""
    )

    expected_result = {
        "detail": [
            {
            "loc": [
                "body",
                "is_done"
      ],
            "msg": "value could not be parsed to a boolean",
            "type": "type_error.bool"
    }
  ]
}
    data = response.json()

    assert response.status_code == httpx.codes.UNPROCESSABLE_ENTITY, f"Ожидался код 422, пришел {response.status_code}"

    assert data == expected_result, "ожидаемый ответ не совпадает"

    #ЗАДАНИЕ: вытащить тело ответа