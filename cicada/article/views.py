"""文章视图"""
from copy import deepcopy
from pprint import pprint

from cicada import mongodb
from cicada.article import article_bp
from flask import request, jsonify

from bson import ObjectId

from tools.elastic_tool import cicadaES


# 文章搜索
@article_bp.route('/', methods=['GET'])
def article():
    """
    # 文章的
    查：能够搜查数据苦衷的所有
    :return:

    """
    data_dic = request.args
    print('===>', data_dic)
    data_dic = dict(data_dic)
    print('--->', data_dic)
    query = {
        "query": {
            "bool": {
                "should": [
                    {
                        "match": {
                            "title": data_dic.get('query_keyword')
                        }
                    },
                    {
                        "match": {
                            "content": data_dic.get('query_keyword')
                        }
                    }

                ]
            }
        },
        "highlight": {
            "pre_tags": "<b style='color:red' class='ct'>",
            "post_tags": "</b>",
            "fields": {
                "content": {}
            }
        }
    }
    # print(query)
    es = cicadaES('cicada', 'article_image')
    result = es.search(query)
    # from pprint import pprint
    # pprint(result)
    # print(result.get('hits').get('hits')[0].get('highlight').get('content'))
    if not result:
        return {'retCode': '000', 'retMsg': '查询成功', 'info': []}
    info_list = []
    for item in result.get('hits').get('hits'):
        # print('--->', item.get('_id'))
        # print('--->', type(item.get('_id')))
        author_dic = mongodb.db.users.find_one({'_id': ObjectId(item.get('_source').get('user_id'))})
        # print(author_dic)
        info_list.append({
                    "title": item.get('_source').get('title'),
                    "content": item.get('_source').get('content'),
                    "highlight": item.get('highlight').get('content'),
                    "author": author_dic.get('username'),
                    "update_time": item.get('_source').get('update_time'),
                    "_image": item.get('_source').get('_image'),
                    "avatar": author_dic.get('avatar')
                    })
    print(info_list)
    return {'retCode': '000', 'retMsg': '查询成功', 'info': info_list}


# 推荐
@article_bp.route('/commend', methods=['GET'])
def article_commend():
    if request.method == "GET":
        article_list = []
        article_dic = mongodb.db.article.find()
        for item in article_dic:
            # print(item)
            # print(item.get('user_id'))
            try:
                author_dic = mongodb.db.users.find_one({"_id": ObjectId(item.get('user_id'))})
            except BaseException as err:
                print(str(err))
            # print(author_dic)
            article_list.append({
                "title": item.get('title'),
                "content": item.get('content'),
                "author": author_dic.get('username'),
                "highlight": [item.get('introduce')],
                "update_time": item.get('update_time'),
                "_image": item.get('_image'),
                "avatar": author_dic.get('avatar')
            })
        return {'retCode': '000', 'retMsg': '查询成功', 'info': article_list}


@article_bp.route('/hot', methods=['GET'])
def article_hot():
    if request.method == 'GET':
        # 通过浏览数量排序展示热度前20 的文章
        article_obj = mongodb.db.article.find()
        article_list = []
        for article_dic in article_obj:
            # print(article_dic.get('_id'))
            # print(type(article_dic.get('_id')))
            user_dic = mongodb.db.users.find_one({"_id": article_dic.get('user_id')})
            # print(user_dic)
            hot_heat = mongodb.db.glance.count({'article_id': article_dic.get('_id')})
            # print('--->', hot_heat)
            article_list.append({
                "title": article_dic.get("title"),
                "content": article_dic.get("content"),
                "introduce": article_dic.get("introduce"),
                "_image": article_dic.get("_image"),
                "hot_heat": hot_heat,
                "avatar": user_dic.get('avatar'),
                "author": user_dic.get('username')
            })
        article_list = sorted(article_list, key=lambda article_list:article_list['hot_heat'], reverse=True)
        from pprint import pprint
        # pprint(article_list)

        return {'retCode': '000', 'retMsg': '查询成功', 'info': article_list}

# like


@article_bp.route('/<article_id>/like_relation', methods=['GET', 'POST', 'DELETE'])
def article_like(article_id):
    if request.method == 'GET':
        "通过user_id 和 article_id 查询 like_status, 如果没有查询到，则返回 like_status 为 0"
        pass
    elif request.method == 'POST':
        "判断like_status   若存在 修改mongodb中like_status状态      若不存在 将关系添加到数据库中 "
        pass


@article_bp.route('/<article_id>/',methods=['GET'])
def article_comment(article_id):
    pass