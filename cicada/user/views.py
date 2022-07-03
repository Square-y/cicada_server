import base64
import hashlib
import os
from copy import deepcopy

from bson import ObjectId
from flask import request
from bs4 import BeautifulSoup
from tools.elastic_tool import cicadaES
from . import user_bp


# 用户列表
from .. import mongodb


@user_bp.route('/', methods=['GET', 'POST', 'PUT', 'DELETE'])
def users():
    pass


# 某一用户信息
@user_bp.route('/<user_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user(user_id):
    pass


# 某一用户的文章列表
@user_bp.route('/<user_id>/articles', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_articles(user_id):
    """
            {
        'title': title,
        'content':  content,
        'create_time': create_time,
        'update_time': update_time,
        'categories': categories,
        'public': 1,
        'status': status
    }
    :param user_id:
    :return:
    """
    if request.method == 'POST':
        mongo_data = request.get_json()
        # print('===>', mongo_data)
        mongo_data['create_time'] = str(mongo_data['create_time'])
        mongo_data['update_time'] = str(mongo_data['update_time'])
        simple_info = BeautifulSoup(mongo_data['content'], 'html.parser')
        mongo_data['introduce'] = simple_info.get_text()[:100] + '...'
        es_data = deepcopy(mongo_data)
        # print(data)
        # print(type(data))

        # user_dic = mongodb.db.users.find_one({"username": username})
        es_data['user_id'] = user_id
        mongo_data['user_id'] = ObjectId(user_id)
        # 存入 mongodb
        _id = mongodb.db.article.insert(mongo_data)
        # 存入elasticsearch
        # pprint(es_data)
        es = cicadaES('cicada', 'article_image')
        es.insert_one(_id, es_data)
        return {'retCode': '000', 'retMsg': '保存成功', 'info': ''}

    elif request.method == 'GET':
        print('-----')
        data_obj = mongodb.db.article.find({"user_id": ObjectId(user_id), "public": 1}, {"title": 1, "introduce": 1,
                                                                                         "content": 1,
                                                                                         "update_time": 1})
        data_list = []
        if data_obj:
            for item in data_obj:
                # print(item)
                item['_id'] = str(item.get("_id"))
                data_list.append(item)
        return {'retCode': '000', 'retMsg': '查询成功', 'info': data_list}


# 某一用户的具体文章
@user_bp.route('/<user_id>/articles/<article_id>', methods=['GET', 'POST', 'PUT', 'DELETE'])
def user_article(user_id, article_id):
    if request.method == 'GET':
        # print('--->', user_id)
        user_dic = mongodb.db.users.find_one({'_id': ObjectId(user_id)})
        # print(user_dic)
        # print(type(user_dic))
        username = user_dic.get('username')
        res = mongodb.db.article.find({'user_id': ObjectId(user_id)})
        # print(res)
        list_info = []
        for item in res:
            # pprint(item)
            # print(item.get('user_id'))
            list_info.append({'author': username,
                                'title': item['title'],
                                'content':  item['content'],
                                'introduce':  item['introduce'],
                                'create_time': item['create_time'],
                                'update_time': item['update_time'],
                                'categories': item['categories'],
                                'public': item['public'],
                                'status': item['status']})

        return {'retCode': '000', 'retMsg': '查询成功', 'info': list_info}

    elif request.method == 'DELETE':
        # 获取json数据  {'_id':''}
        data_dic = request.get_json()
        data_dic['_id'] = ObjectId(data_dic['_id'])
        if not mongodb.db.article.find_one(data_dic):
            return {'retCode': '111', 'retMsg': '删除失败', 'info': '文章不存在'}
        res = mongodb.db.article.remove(data_dic)
        if res.get('n') == 0:
            return {'retCode': '111', 'retMsg': '删除失败', 'info': '文章不存在'}
        # print(res)
        # print(type(res))
        else:
            return {'retCode': '000', 'retMsg': '删除成功', 'info': ''}

    elif request.method == 'PUT':
        data_dic = request.get_json()
        print(data_dic)



    """
    # 文章的
    查：若username为已登录的username，则返回所有文章
       若username为未登录的，或与已登录的username不一致，则只显示公开的文章
    增加：若username为已登录的username，则有此功能
    修改：若username为已登录的username，则有此功能
    删： 若username为已登录的username，则有此功能、
    传入的数据格式

    :return:
    """


@user_bp.route('/commend', methods=['GET'])
def user_commend():
    if request.method == 'GET':
        users_obj = mongodb.db.users.find()
        commend_user = []
        for user in users_obj:
            # print(user)
            commend_user.append({
                "_id": str(user.get('_id')),
                "username": user.get("username"),
                "sign": user.get("sign"),
                "avatar": user.get("avatar")
            })
        return {'retCode': '000', 'retMsg': '查询成功', 'info': commend_user}

