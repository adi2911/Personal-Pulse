import os
import requests
from constants import *


def filtered_data(data):
    data={
        k: v
        for k,v in data.items()
        if v not in ([],"","",None)
            and k not in ["people_also_viewed","certifications"]
    }
    if data.get("groups"):
        for group in data.get("groups"):
            group.pop("profile_pic_url")
    return data

def scarpe_linkedIn_profile(profile_url:str):
    # Making request to gist mock profile. For testing purpose . For production purpose we can use proxycurl.
    mock_response=requests.get(mock_gist_profile)
    return filtered_data(mock_response.json())


    # Making actual proxycurl call. Only 10 limits oper account.

    # headers = {'Authorization': 'Bearer ' + os.getenv('PROXY_CURL_KEY')}
    # api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    # params = {
    #     'url': profile_url,
    # }
    # response = requests.get(api_endpoint,
    #                     params=params,
    #                     headers=headers)


print(scarpe_linkedIn_profile("test"))