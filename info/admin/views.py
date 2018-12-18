from flask import current_app
from flask import g
from flask import session, jsonify

from info import constants
from info.models import User, Webs
from info.utils.image_storage import storage
from info import db
from info.utils.common import user_login_data

from info.utils.response_code import RET
from . import admin_blue
from flask import render_template, request, redirect, url_for
import time
from datetime import datetime, timedelta


# @admin_blue.route('/add_category', methods=["POST"])
# def add_category():
#     """修改或者添加分类"""
#     category_id = request.json.get("id")
#     name = request.json.get("name")
#
#
#     if category_id:
#         category = Category.query.get(category_id)
#         category.name = name
#     else:
#         category = Category()
#         category.name = name
#
#         db.session.add(category)
#
#     db.session.commit()
#
#     return jsonify(errno = RET.OK,errmsg = "OK")

# @admin_blue.route("/news_type")
# def news_type():
#     # category_list = Webs.query.all()
#     # categories = []
#     # for category in category_list:
#     #     categories.append(category.to_dict())
#     # categories.pop(0)
#     # data = {
#     #     "categories": categories
#     # }
#     return render_template("admin/news_type.html")


@admin_blue.route("/news_remove_detail", methods=["GET", "POST"])
def news_remove_detail():
    if request.method == "GET":
        webs_id = request.args.get("news_id")
        webs = Webs.query.get(webs_id)
        # category_list = Webs.query.all()
        categories = [{'type': '0'}, {'type': '1'}, {'type': '2'}, {'type': '3'}, {'type': '4'}, {'type': '5'}]
        methods = [{'value': 'json'}, {'value': 'xml'}, {'value': 'dir'}]
        # for category in category_list:
        #     categories.append(category.to_like_dict())
        # categories.pop(0)
        data = {
            "news": webs.to_like_dict(),
            "categories": categories,
            'methods': methods
        }
        return render_template("admin/news_remove_detail.html", data=data)
    webs_id = request.form.get("news_id")
    webs = Webs.query.get(webs_id)
    webs.flag = '0'
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
    return jsonify(errno=RET.OK, errmsg="删除成功")


    # webs.ad_url = ad_url
    # webs.back_url = back_url
    # webs.login_url = login_url
    # webs.spider_type = spider_type
    # webs.parse_method = parse_method
    # webs.rule = rule
    # webs.login_header = login_header
    # webs.form_data = form_data
    # webs.post_url = post_url
    # webs.post_header = post_header
    # webs.post_data = post_data
    # webs.img_url = img_url
    # try:
    #     db.session.commit()
    # except Exception as e:
    #     current_app.logger.error(e)
    #     db.session.rollback()
    # return jsonify(errno=RET.OK, errmsg="编辑成功")

@admin_blue.route("/news_review_detail", methods=["GET", "POST"])
def news_type():
    if request.method == "GET":
        categories = [{'type': '0'}, {'type': '1'}, {'type': '2'}, {'type': '3'}, {'type': '4'}, {'type': '5'}]
        methods = [{'value': 'json'}, {'value': 'xml'}, {'value': 'dir'}]
        data = {
            "categories": categories,
            'methods': methods
        }
        return render_template("admin/news_review_detail.html", data=data)
    ad_url = request.form.get("ad_url")
    back_url = request.form.get("back_url")
    login_url = request.form.get("login_url")
    spider_type = request.form.get("spider_type")
    parse_method = request.form.get("parse_method")
    rule = request.form.get("rule")
    login_header = request.form.get("login_header")
    form_data = request.form.get("form_data")
    post_url = request.form.get("post_url")
    post_header = request.form.get("post_header")
    post_data = request.form.get("post_data")
    img_url = request.form.get("img_url")

    if not all([ad_url, back_url, login_url, spider_type, parse_method, rule]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数有误")
    webs = Webs()
    webs.ad_url = ad_url
    webs.back_url = back_url
    webs.login_url = login_url
    webs.spider_type = spider_type
    webs.parse_method = parse_method
    webs.rule = rule
    webs.login_header = login_header
    webs.form_data = form_data
    webs.post_url = post_url
    webs.post_header = post_header
    webs.post_data = post_data
    webs.img_url = img_url

    try:
        db.session.add(webs)
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
    return jsonify(errno=RET.OK, errmsg="OK")


@admin_blue.route("/news_edit_detail", methods=["GET", "POST"])
def news_edit_detail():
    if request.method == "GET":
        webs_id = request.args.get("news_id")
        webs = Webs.query.get(webs_id)
        # category_list = Webs.query.all()
        categories = [{'type': '0'}, {'type': '1'}, {'type': '2'}, {'type': '3'}, {'type': '4'}, {'type': '5'}]
        methods = [{'value': 'json'}, {'value': 'xml'}, {'value': 'dir'}]
        # for category in category_list:
        #     categories.append(category.to_like_dict())
        # categories.pop(0)
        data = {
            "news": webs.to_like_dict(),
            "categories": categories,
            'methods': methods
        }
        return render_template("admin/news_edit_detail.html", data=data)
    webs_id = request.form.get("news_id")
    webs = Webs.query.get(webs_id)
    ad_url = request.form.get("ad_url")
    back_url = request.form.get("back_url")
    login_url = request.form.get("login_url")
    spider_type = request.form.get("spider_type")
    parse_method = request.form.get("parse_method")
    rule = request.form.get("rule")
    login_header = request.form.get("login_header")
    form_data = request.form.get("form_data")
    post_url = request.form.get("post_url")
    post_header = request.form.get("post_header")
    post_data = request.form.get("post_data")
    img_url = request.form.get("img_url")


    # 1.1 判断数据是否有值
    if not all([ad_url, back_url, login_url, spider_type, parse_method, rule]):
        return jsonify(errno=RET.PARAMERR, errmsg="参数有误")

    webs.ad_url = ad_url
    webs.back_url = back_url
    webs.login_url = login_url
    webs.spider_type = spider_type
    webs.parse_method = parse_method
    webs.rule = rule
    webs.login_header = login_header
    webs.form_data = form_data
    webs.post_url = post_url
    webs.post_header = post_header
    webs.post_data = post_data
    webs.img_url = img_url
    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()
    return jsonify(errno=RET.OK, errmsg="编辑成功")



@admin_blue.route("/news_collect" ,methods = ["POST"])
@user_login_data
def news_collect():
    # user = g.user
    # if not user:
    #     return jsonify(errno = RET.SESSIONERR,errmsg = "请登陆")

    # 表示获取到爬虫id
    webs_id = request.json.get("news_id")
    action = request.json.get("action")
    webs = Webs.query.get(webs_id)


    if not webs:
        return jsonify(errno = RET.NODATA,errmsg = "没有爬虫数据")

    if action == "collect":
        # 收藏
        webs.status = "1"
    else:
        # 取消收藏
        webs.status = "0"

    try:
        db.session.commit()
    except Exception as e:
        current_app.logger.error(e)
        db.session.rollback()

    return jsonify(errno = RET.OK,errmsg = "收藏成功")


"""
爬虫任务

"""


@admin_blue.route("/news_edit")
def news_edit():
    page = request.args.get("p", 1)
    # 获取到小编搜索的文字
    keywords = request.args.get("keywords")
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1

    paginate = Webs.query.filter(Webs.flag == "1").paginate(page, 10, False)
    items = paginate.items
    current_page = paginate.page
    total_page = paginate.pages

    news_list = []
    for item in items:
        news_list.append(item.to_like_dict())
    data = {
        "news_list": news_list,
        "current_page": current_page,
        "total_page": total_page
    }
    return render_template("admin/news_edit.html", data=data)


"""
新闻审核的详情页面
"""

#
# @admin_blue.route("/news_review_detail", methods=["GET", "POST"])
# def news_review_detail():
#     if request.method == "GET":
#         news_id = request.args.get("news_id")
#         news = News.query.get(news_id)
#         data = {
#             "news": news.to_dict()
#         }
#         return render_template("admin/news_review_detail.html", data=data)
#
#     action = request.json.get("action")
#     news_id = request.json.get("news_id")
#
#     news = News.query.get(news_id)
#
#     if action == "accept":
#         # 审核通过,如果审核通过,那么直接修改当前新闻的状态就可以了
#         news.status = 0
#     else:
#         # 审核不通过,拒绝,拒绝就需要说明原因
#         reason = request.json.get("reason")
#         if not reason:
#             return jsonify(errno=RET.NODATA, errmsg="请说明拒绝原因")
#
#         news.status = -1
#         news.reason = reason
#
#     db.session.commit()
#     return jsonify(errno=RET.OK, errmsng="ok")


"""
新闻审核
"""


# @admin_blue.route("/news_review")
# def news_review():
#     page = request.args.get("p", 1)
#     # 获取到小编搜索的文字
#     keywords = request.args.get("keywords")
#     try:
#         page = int(page)
#     except Exception as e:
#         current_app.logger.error(e)
#         page = 1
#
#     filters = [News.status != 0]
#     # 如果小编用了搜索功能,才需要进行搜索,如果不需要搜索,那么就不需要查询数据库
#     if keywords:
#         filters.append(News.title.contains(keywords))
#     paginate = News.query.filter(*filters).order_by(News.create_time.desc()).paginate(page, 10, False)
#     items = paginate.items
#     current_page = paginate.page
#     total_page = paginate.pages
#
#     news_list = []
#     for item in items:
#         news_list.append(item.to_review_dict())
#
#     data = {
#         "news_list": news_list,
#         "current_page": current_page,
#         "total_page": total_page
#     }
#
#     return render_template("admin/news_review.html", data=data)


"""
获取到爬虫列表
"""

@admin_blue.route("/user_list")
def user_list():
    page = request.args.get("p", 1)
    try:
        page = int(page)
    except Exception as e:
        current_app.logger.error(e)
        page = 1
    paginate = Webs.query.filter(Webs.status == "1", Webs.flag == "1").paginate(page, 10, False)
    items = paginate.items
    current_page = paginate.page
    total_page = paginate.pages

    webs = []
    for web in items:
        webs.append(web.to_like_dict())

    data = {
        "users": webs,
        "current_page": current_page,
        "total_page": total_page
    }

    return render_template("admin/user_list.html", data=data)


"""
统计当前数据库里面的爬虫数量
"""


@admin_blue.route("/user_count")
def spider_count():
    # 爬虫总数量
    total_count = 0
    # 一个月新增加的爬虫数量
    mon_count = 0
    # 一天新增加的爬虫数量
    day_count = 0

    sum_count = Webs.query.filter().count()

    t = time.localtime()
    # 2018-06-01
    mon_begin = "%d-%02d-01" % (t.tm_year, t.tm_mon)
    # 第一个参数表示时间字符串,
    # 第二个参数表示格式化时间
    mon_begin_date = datetime.strptime(mon_begin, "%Y-%m-%d")
    # 查询本月新增加了多少爬虫
    mon_count = Webs.query.filter(Webs.create_time > mon_begin_date).count()
    day_begin = "%d-%02d-%02d" % (t.tm_year, t.tm_mon, t.tm_mday)
    day_begin_date = datetime.strptime(day_begin, "%Y-%m-%d")
    day_count = Webs.query.filter(Webs.create_time > day_begin_date).count()
    today_begin = "%d-%02d-%02d" % (t.tm_year, t.tm_mon, t.tm_mday)
    today_begin_date = datetime.strptime(day_begin, "%Y-%m-%d")
    activate_count = []
    activate_time = []
    for i in range(0, 31):
        begin_date = today_begin_date - timedelta(days=i)
        end_date = today_begin_date - timedelta(days=(i - 1))

        count = Webs.query.filter(Webs.create_time >= begin_date,
                                  Webs.create_time < end_date).count()
        activate_count.append(count)
        activate_time.append(begin_date.strftime("%Y-%m-%d"))

    activate_time.reverse()
    activate_count.reverse()
    data = {
        "total_count": sum_count,
        "mon_count": mon_count,
        "day_count": day_count,
        "activate_count": activate_count,
        "activate_time": activate_time
    }
    return render_template("admin/user_count.html", data=data)


@admin_blue.route("/index")
@user_login_data
def admin_index():
    user = g.user
    return render_template("admin/index.html", user=user.to_admin_dict())


@admin_blue.route("/logout")
def logout():
    # 清除session里面的数据
    session.pop("user_id",None)
    session.pop("nick_name",None)
    session.pop("is_admin",None)
    return redirect(url_for("admin.admin_login"))
    # return jsonify(errno=RET.OK, errmsg="退出成功")

@admin_blue.route("/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "GET":
        user_id = session.get("user_id", None)
        is_admin = session.get("is_admin", False)
        # 如果当前用户已经登陆，并且还是管理员，才能进入到管理员的界面
        if user_id and is_admin:
            return redirect(url_for("admin.admin_index"))
        return render_template("admin/login.html")

    username = request.form.get("username")

    password = request.form.get("password")
    # 如果用户名正确，还必须是管理员才能登陆
    user = User.query.filter(User.nick_name == username, User.is_admin == True).first()
    if not user:
        return render_template("admin/login.html", errmsg="没有这个用户")

    if not user.check_password(password):
        return render_template("admin/login.html", errmsg="密码错误")

    session["user_id"] = user.id
    session["nick_name"] = user.nick_name
    session["is_admin"] = user.is_admin

    return redirect(url_for("admin.admin_index"))
