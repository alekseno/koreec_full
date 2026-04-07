import httpx
from secondary_func import create_task

def test_create_content_null():
    response = create_task(
        content = None,
        user_id = str,
        is_done = False

    )
    expected_result = {
        "detail": [
            {
            "loc": [
                "body",
                "content"
      ],
            "msg": "none is not an allowed value",
            "type": "type_error.none.not_allowed"
    }
  ]
}
    data = response.json()

    assert response.status_code == httpx.codes.UNPROCESSABLE_ENTITY, f"Ожидался код 422, пришел {response.status_code}"

    assert data == expected_result, "данные ответа отличаются от шаблона сервера"

 