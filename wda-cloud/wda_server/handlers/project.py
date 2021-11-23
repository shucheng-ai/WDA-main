#!/usr/bin/env python3
# coding:utf-8
from .base import BaseHandler
from app.auth import wdaauth
from app.db import wdamodel
from app.utils import mkdir
from config import LAYOUT_PROJECT_URL, RESOURCE_MODEL_PROJECT_URL, LAYOUT_PROJECT_PATH, RESOURCE_MODEL_PROJECT_PATH, \
    PROJECT_LIMIT, PAGE_LIMIT, DATA_ANALYTICS_PROJECT_URL, LAYOUT2_PROJECT_URL, CAD_PROJECT_URL

import os
import datetime


class ProjectHandler(BaseHandler):

    def check_project_permission(self, project, user, groups):
        # 非登陆用户
        if user['uid'] == -1:
            return False
        # 该用户数据
        if user['name'] == project['username']:
            return True
        # company admin用户
        admin_group = f'{project["company"]}_admin'
        if admin_group in groups:
            return True
        # 管理员账号
        if "admin" in groups:
            return True
        return False

    def get_project(self, project_id, user, groups):
        data = {
            "status": 0,
            "msg": '',
            "data": None
        }
        project = wdamodel.project.get(id=project_id, engine=wdamodel.db_engine)
        project_data = wdamodel.project.json(project)

        if f'{project_id}' != '1':
            # 判断权限
            # if user['uid'] == -1 or user['name'] != project_data['username']:
            if not self.check_project_permission(project_data, user, groups):
                return self.error_403
            else:
                data["status"] = 1
        else:
            data["status"] = 1

        data["data"] = project_data
        return data

    def mk_project_dir(self, project_id):
        path1 = os.path.abspath(os.path.join(LAYOUT_PROJECT_PATH, str(project_id)))
        path2 = os.path.abspath(os.path.join(RESOURCE_MODEL_PROJECT_PATH, str(project_id)))
        input1 = os.path.abspath(os.path.join(path1, "input"))
        input2 = os.path.abspath(os.path.join(path2, "input"))
        output1 = os.path.abspath(os.path.join(path1, "output"))
        output2 = os.path.abspath(os.path.join(path2, "output"))
        mkdir(path1)
        mkdir(path2)
        mkdir(input1)
        mkdir(output1)
        mkdir(input2)
        mkdir(output2)

    def get_project_list(self, user, groups, project_type, filter_by, company, page=1, limit=PAGE_LIMIT):
        data = []
        if user['uid'] == -1:
            return data

        filters = {
            "username": user["name"]
        }

        if filter_by == "all" and "admin" in groups:
            filters = {}

        if filter_by == "company" and f"{company}_admin" in groups:
            filters = {
                "company": company
            }

        filters['type'] = project_type
        filters['delete'] = 0

        projects = wdamodel.project.filter(
            fliters=filters,
            engine=wdamodel.db_engine,
            reverse=True,
            limit=limit,
            offset=(page - 1) * 10,
            order_by='id')

        count = wdamodel.project.count(
            fliters=filters,
            engine=wdamodel.db_engine,
        )

        for _p in projects:
            project_data = wdamodel.project.json(_p)
            project_data["layout_url"] = f"{LAYOUT_PROJECT_URL}{_p.id}"
            project_data["layout2_url"] = f"{LAYOUT2_PROJECT_URL}{_p.id}"
            project_data["resource_model_url"] = f"{RESOURCE_MODEL_PROJECT_URL}{_p.id}"
            project_data["data_analytics_url"] = f"{DATA_ANALYTICS_PROJECT_URL}{_p.id}"
            project_data["cad_url"] = f"{CAD_PROJECT_URL}{_p.id}"
            data.append(project_data)

        info = {
            "count": count,
            "page": page,
            "limit": limit,
        }

        return {"data": data, "info": info}

    @wdaauth.wda_auth
    @wdaauth.wda_group_required()
    def _get(self, **kwargs):
        # 获取单个project数据
        # /api/project?q=project&project_id=1
        # 获取project list列表
        # /api/project?q=list&
        # all / company / user
        # http://127.0.0.1:38083/api/project?q=list&filter_by=all
        # http://127.0.0.1:38083/api/project?q=list&filter_by=user
        # http://127.0.0.1:38083/api/project?q=list&filter_by=company&limit=20&company=shucheng
        data = {
            "data": {}
        }
        user = kwargs.get("wda_user")
        groups = kwargs.get("wda_user_groups")
        # print(user)

        q = self.get_arg('q', 'list')
        project_id = self.get_arg('project_id', None)
        project_type = self.get_arg('type', 'layout')
        company = self.get_arg('company', '')
        filter_by = self.get_arg('filter_by', 'user')  # user, company, all
        page = int(self.get_arg('page', 1))  # page
        limit = int(self.get_arg('limit', PAGE_LIMIT))  # PAGE_LIMIT - 100
        if limit > 100:
            limit = 100

        if q == 'project':
            #  get project data
            project_data = self.get_project(project_id=project_id, user=user, groups=groups)
            if project_data["status"] == 1:
                data["status"] = 1
                data["data"]["project"] = project_data["data"]
            else:
                data["status"] = project_data["status"]
                data["msg"] = project_data["msg"]
        else:
            # get project list
            project_list = self.get_project_list(user=user,
                                                 groups=groups,
                                                 company=company,
                                                 filter_by=filter_by,
                                                 project_type=project_type,
                                                 page=page,
                                                 limit=limit,
                                                 )
            data["status"] = 1
            data["data"]["project_list"] = project_list

        return data

    @wdaauth.wda_auth
    @wdaauth.wda_group_required()
    def _post(self, **kwargs):
        # add new project
        # http://127.0.0.1:38083/api/project
        # formdata = {
        #     'name': '',
        # }
        project_limit = PROJECT_LIMIT
        # project_limit = 9999

        user = kwargs.get("wda_user")
        userinfo = {}
        if user['uid'] == -1:
            return self.error_403
        if user.get('info'):
            userinfo = user['info']
            if user.get('is_expired') == -1:
                project_limit = user['info']['limit']

        # 检查用户project limit
        count = wdamodel.project.count(
            fliters={
                'uid': f'{user["uid"]}'
            },
            engine=wdamodel.db_engine,
        )
        userinfo["total_project"] = count
        # print(count, project_limit)
        if count > project_limit:
            return {'data': {'count': count}, 'status': -1, 'msg': 'project limit'}

        self.get_formdata()
        name = self.formdata.get('name', '')
        project_type = self.formdata.get('type', '')  # layout layout2 cad resource_model data_analytics

        maxid = wdamodel.project.get_maxid(wdamodel.db_engine)
        if not name:
            name = f"project-{maxid + 1}"

        # 创建project 数据
        new_project = wdamodel.project(
            id=maxid + 1,
            uid=f'{user["uid"]}',
            company=user.get('company', ''),
            name=name,
            username=user["name"],
            type=project_type,
        )
        wdamodel.project.add(new_project, wdamodel.db_engine)

        # mkdir
        self.mk_project_dir(maxid + 1)

        project_info = wdamodel.project.json(new_project)
        project_info["layout_url"] = f"{LAYOUT_PROJECT_URL}{new_project.id}"
        project_info["layout2_url"] = f"{LAYOUT2_PROJECT_URL}{new_project.id}"
        project_info["resource_model_url"] = f"{RESOURCE_MODEL_PROJECT_URL}{new_project.id}"
        project_info["data_analytics_url"] = f"{DATA_ANALYTICS_PROJECT_URL}{new_project.id}"
        project_info["cad_url"] = f"{CAD_PROJECT_URL}{new_project.id}"

        return {
            'data': project_info,
            "maxid": maxid, 'status': 1,
            'f': self.formdata,
            'userinfo': userinfo
        }

    @wdaauth.wda_auth
    @wdaauth.wda_group_required()
    def put(self, **kwargs):
        user = kwargs.get("wda_user")
        groups = kwargs.get("wda_user_groups")

        if user['uid'] == -1:
            return self.error_403

        self.get_formdata()
        project_id = self.formdata["id"]
        name = self.formdata["name"]
        descript = self.formdata.get('descript', '')

        project_data = self.get_project(project_id, user, groups)
        if project_data["status"] == 1:
            # update
            wdamodel.project.update(
                engine=wdamodel.db_engine,
                id=project_id,
                data={
                    "name": name,
                    "descript": descript,
                    "update_date": datetime.datetime.now()
                }
            )

        return {'data': "", "status": 1, }
