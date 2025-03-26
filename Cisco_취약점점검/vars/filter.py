import os
import json
import re


# 변수 가져오기 -------------------------------------------------------

hostname = os.environ.get('hostname',' ')
host = os.environ.get('host',' ')
total_item = os.environ.get('total_item',' ')
message = os.environ.get('message',' ')
iid = os.environ.get('id',' ')
value = os.environ.get('value',' ')
name = os.environ.get('name',' ')
command = os.environ.get('command',' ')
system = os.environ.get('system',' ')
report_type = os.environ.get('report_type',' ')


# merged_dict --------------------------------------------------------

result_dict = {

    'hostname': hostname,
    'host': host,
    'command': command,
    'name': name,
    'report_type': report_type,
    'system': system,
    'id': iid,
    'message': message
}




#필터 함수 -----------------------------------------------------------


def filter(total_item,value):

    if total_item:
        total_item = f'{total_item}'
    
    else:
        return {

            is_passed: "None",
            is_successed: 0, 
            message: '명령에 실패했습니다'

        }
    
    fail_items = []
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
                fail_item = 'fail' if is_passed == '1' else ' '
            
            is_successed = '0' if is_passed == '0' else '1'
    
    message = f'  결과| name : {name}  \n total_item: {total_item}'

    if fail_item:
        fail_items.append(fail_item)

    return  {
            "is_passed" : is_passed,
            "is_successed" : is_successed,
            "message": message
        }

       

    




#---------------------------------------------------------------------

         
result_dict = result_dict.update(filter(total_item,value))
            
print(json.dumps(result_dict , ensure_ascii=False))
            
            