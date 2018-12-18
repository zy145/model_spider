from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from . import db


class BaseModel(object):
    """模型基类，为每个模型补充创建时间与更新时间"""
    create_time = db.Column(db.DateTime, default=datetime.now)  # 记录的创建时间
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)  # 记录的更新时间

class User(BaseModel, db.Model):
    """用户"""
    __tablename__ = "t_info_user"

    id = db.Column(db.Integer, primary_key=True)  # 用户编号
    nick_name = db.Column(db.String(32), unique=True, nullable=False)  # 用户昵称
    password_hash = db.Column(db.String(128), nullable=False)  # 加密的密码
    last_login = db.Column(db.DateTime, default=datetime.now)  # 最后一次登录时间
    is_admin = db.Column(db.Boolean, default=False)


    @property
    def password(self):
        raise AttributeError("当前属性不可读")

    @password.setter
    def password(self, value):
        self.password_hash = generate_password_hash(value)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


    def to_dict(self):
        resp_dict = {
            "id": self.id,
            "nick_name": self.nick_name,
        }
        return resp_dict


    def to_admin_dict(self):
        resp_dict = {
            "id": self.id,
            "nick_name": self.nick_name,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "last_login": self.last_login.strftime("%Y-%m-%d %H:%M:%S"),
        }
        return resp_dict


class Webs(BaseModel, db.Model):
    """网站"""
    # 需提供信息 id, adurl, backurl, login_url, type, parse_method, rule, header, form_data, post_url, headers, post_data, img_url, create_time, update_time
    __tablename__ = "t_base_info"
    id = db.Column(db.Integer, primary_key=True)
    ad_url = db.Column(db.String(250), unique=True, nullable=False)  # 广告链接
    back_url = db.Column(db.String(250), nullable=False)
    login_url = db.Column(db.String(250), nullable=False)
    spider_type = db.Column(
        db.Enum(
            "0",
            "1",
            "2",
            "3",
            "4",
            "5"
        ),
        default="0")
    parse_method = db.Column(
        db.Enum(
            "json",
            "xml",
            "dir",
        ),
        default="json")
    rule = db.Column(db.String(100), nullable=False)
    login_header = db.Column(db.String(512))
    form_data = db.Column(db.String(512))
    post_url = db.Column(db.String(250))
    post_header = db.Column(db.String(512))
    post_data = db.Column(db.String(512))
    img_url = db.Column(db.String(250))
    status = db.Column(
        db.Enum(
            "0",
            "1"
        ),
        default="1")
    flag = db.Column(
        db.Enum(
            "0",
            "1"
        ),
        default="1")

    def to_like_dict(self):
        resp_dict = {
            "id": self.id,
            "ad_url": self.ad_url,
            "back_url":  self.back_url,
            "login_url": self.login_url,
            "spider_type": self.spider_type if self.spider_type else "0",
            "parse_method": self.parse_method if self.parse_method else "json",
            "rule": self.rule,
            "login_header": self.login_header if self.login_header else None,
            "form_data": self.form_data if self.form_data else None,
            "post_url": self.post_url if self.post_url else None,
            "post_header": self.post_header if self.post_header else None,
            "post_data": self.post_data if self.post_data else None,
            "img_url": self.img_url if self.img_url else None,
            "create_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "update_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "status": self.status,
            "flag": self.flag
        }
        return resp_dict

    def to_admin_dict(self):
        resp_dict = {
                "id": self.id,
                "ad_url": self.ad_url,
                "back_url": self.back_url,
                "login_url": self.login_url,
                "status": self.status,
                "flag": self.flag
            }
        return resp_dict


class Datas(db.Model):
    """数据"""
    __tablename__ = "t_basic_data"

    id = db.Column(db.Integer, primary_key=True)  # 编号
    ad_url = db.Column(db.String(250), unique=True, nullable=False)  # 广告链接
    spider_time = db.Column(db.String(32), nullable=False)
    date_time = db.Column(db.String(32), nullable=False)
    register = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(10), nullable=False)
    msg = db.Column(db.String(256))

    def to_basic_dict(self):
        resp_dict = {
            "id": self.id,
            "ad_url": self.ad_url,
            "register": self.login_header if self.login_header else "",
            "code": self.code,
            "result": self.result,
            "spider_time": self.spider_time.strftime("%Y-%m-%d %H:%M:%S"),
            "date_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "msg": self.msg if self.msg else ""
        }
        return resp_dict


class MarketData(db.Model):
    __tablename__ = "t_market_data"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    product_id = db.Column(db.String(250), unique=True, nullable=False)  # 广告链接
    spider_time = db.Column(db.String(32), nullable=False)
    date_time = db.Column(db.String(32), nullable=False)
    register = db.Column(db.String(64), nullable=False)
    code = db.Column(db.String(10), nullable=False)
    result = db.Column(db.String(10), nullable=False)
    msg = db.Column(db.String(256))

    def to_basic_dict(self):
        resp_dict = {
            "id": self.id,
            "ad_url": self.ad_url,
            "register": self.login_header if self.login_header else "",
            "code": self.code,
            "result": self.result,
            "spider_time": self.spider_time.strftime("%Y-%m-%d %H:%M:%S"),
            "date_time": self.create_time.strftime("%Y-%m-%d %H:%M:%S"),
            "msg": self.msg if self.msg else ""
        }
        return resp_dict
