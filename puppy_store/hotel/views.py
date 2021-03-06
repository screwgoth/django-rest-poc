from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
import json

# Create your views here.
@api_view(['GET','POST'])
def get_hotel_categories(request):
    # get all Hotel Categories
    if request.method == 'GET':
        zomato_url="https://developers.zomato.com/api/v2.1/categories"
        headers={"Accept":"applicaiton/json",
        "user-key": "b0fcc8e574f96ad3e80be23d898aa861"}
        resp=requests.get(zomato_url,headers=headers)
        print (resp.content)
        print (resp.status_code)
        jresp=json.loads(resp.text)
        print (resp.text)
        print (jresp)
        return Response(jresp)
    if request.method == 'POST':
        print (request.body)
        zomato_url="https://developers.zomato.com/api/v2.1/categories"
        headers={"Accept":"applicaiton/json",
        "user-key": "b0fcc8e574f96ad3e80be23d898aa861"}
        resp=requests.get(zomato_url,headers=headers)
        resp_dict=json.loads(resp.text)
        print (resp_dict)
        for item in resp_dict:
            cat_list = resp_dict[item]
            print (cat_list)
            disp_cat = ""
            for cats in cat_list:
                categ = (cats['categories']['name'])
                disp_cat += categ + ' '
                print (disp_cat)
        tempresp= {
            "speech" : disp_cat,
            "displayText" : disp_cat,
            "source" : "Zomato"
        }
        return Response(tempresp)

@api_view(['GET'])
def get_hotel_collections(request):
    # get all Hotel Categories
    if request.method == 'GET':
        cityid = request.GET["city_id"]
        count = request.GET["count"]
        print (cityid)
        print (count)
        #print ('City ID = ' + cityid + ' and count = ' + count)
        zomato_url="https://developers.zomato.com/api/v2.1/collections"
        headers={"Accept":"applicaiton/json",
        "user-key": "b0fcc8e574f96ad3e80be23d898aa861"}
        params={'city_id':cityid,'count':count}
        resp=requests.get(zomato_url,params=params,headers=headers)
        jresp=json.loads(resp.text)
        return Response(jresp)
