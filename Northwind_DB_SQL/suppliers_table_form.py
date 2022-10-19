import requests
import json


def make_suppliers_dicts() -> list:
    """
    Выгружает данные о поставщиках по ссылке и сохраняет в списке словарей
    """

    response = requests.get("https://s3.us-west-2.amazonaws.com/secure.notion-static.com/2dbad09f-30ef-4728-a0e0-bd6842ed6858/suppliers.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20221019%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20221019T075619Z&X-Amz-Expires=86400&X-Amz-Signature=0a104ca5732958a3f8e22f86e3ac0945e4ae0111a19fda337a878381f9b6973f&X-Amz-SignedHeaders=host&response-content-disposition=filename%20%3D%22suppliers.json%22&x-id=GetObject")
    with open('suppliers.json', 'w', encoding='utf-8') as file:
        content = file.write(response.text)

    with open('suppliers.json', 'r', encoding='utf-8') as file:
        suppliers_dict_list = json.load(file)

    return suppliers_dict_list


