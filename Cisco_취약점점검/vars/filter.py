import os
import json
import re


# 변수 가져오기 -------------------------------------------------------

hostname = os.environ.get('hostname',' ')
host = os.environ.get('host',' ')
content = os.environ.get('content',' ')
message = os.environ.get('message',' ')
iid = os.environ.get('id',' ')
value = os.environ.get('value',' ')




#필터 함수 -----------------------------------------------------------


def filter(content,value):

    if content:
        is_successsed = '0'
    else:
        return {
            "is_passed" : None,
            "is_successed" : None,
            "fail_message" : None,

        }

    
    match value:

        case 'int':

            content_list = content.split('\n')
            chunk_list = list()

            for result in content_list:
                chunk = result.split(" ")
                chunk_list.append(chunk)

            for chunk in chunk_list:
                number = chunk[3]
                is_passed = '0' if float(number) < 7 else '1'
            
    
    return  {
            "is_passed" : is_passed,
            "is_successed" : is_successsed,
        }

       

    




#---------------------------------------------------------------------

result_dict = {

"hostname" :hostname,
"host": host,
"message": message,
"id" : iid,

}
            
result_dict = result_dict.update(filter(content,value))
            
print(json.dumps(result_dict))
            
            