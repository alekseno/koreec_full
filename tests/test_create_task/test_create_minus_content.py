import httpx
from secondary_func import minus_content
 

def test_create_minus_content():
    minus_contents = minus_content(
        user_id = "str",
        is_done = False
    )
    minus_content_data = minus_contents.json()
     

    expected_result = { 
        "detail": [
            {   
            "loc": [
            "body",
            "content"
        ],
            "msg": "field required",
            "type": "value_error.missing"
    }
  ]
}
    
    assert minus_contents.status_code == httpx.codes.UNPROCESSABLE_ENTITY, f"Ожидался код 422, пришел {minus_contents.status_code}"

    assert expected_result == minus_content_data, "данные ответа отличаются от ожидаемого"
