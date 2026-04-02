#import uuid
import re

#id_int01= uuid.uuid4()
#print(id_int01)

a = "task_98fc304bd6c94b73a0839081b006863b"
b = "task_dddll"
c = "task_545"
 
def template_check_task_id(value: str):
    temp_task_id = re.findall(r"task_[0-9a-z]{32}", value)
    result_temp = ' '.join(map(str, temp_task_id))
    return result_temp

def test_user():
   
    response = template_check_task_id(a)
    assert response == a, "не соответствует шаблону регулярки"
    print(response)
