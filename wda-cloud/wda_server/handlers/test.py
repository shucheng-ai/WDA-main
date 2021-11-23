#!/usr/bin/env python3
# coding:utf-8
from .base import BaseHandler
from app.auth import wdaauth
from app.db import wdamodel

import random
import datetime

companys = ['test', '', 'shucheng', 'dhl']

users = {
    "1": "shucheng",
}

class TestHandler(BaseHandler):

    def all1000(self):
        for i in range(1, 1000):
            project = wdamodel.project.get(id=i, engine=wdamodel.db_engine)
            if not project:
                # add new project
                uid = f'{random.randint(1, 10)}'
                company = random.choice(companys)
                username = users.get(uid, "hehe")
                new = wdamodel.project(
                    id=i,
                    uid=uid,
                    note=f"project-{i}",
                    company=company,
                    name=f"project-{i}",
                    username=username
                )
                wdamodel.project.add(new, wdamodel.db_engine)
            else:
                if f"{project.uid}" == "1":
                    print(project.username)
                    wdamodel.project.update(
                        engine=wdamodel.db_engine,
                        id=project.id,
                        data={
                            "username": "shucheng",
                        }
                    )

    @wdaauth.wda_auth
    @wdaauth.wda_login_required
    @wdaauth.wda_group_required()
    @wdaauth.wda_permission_required()
    def _get(self, **kwargs):
        data = {}
        data["user"] = kwargs.get("wda_user")
        data["groups"] = kwargs.get("wda_user_groups")

        p1 = wdamodel.project.get(id=1, engine=wdamodel.db_engine)
        if p1:
            data['p1'] = wdamodel.project.json(p1)

        p999 = wdamodel.project.get(id=-999, engine=wdamodel.db_engine)
        if not p999:
            # add new project
            new = wdamodel.project(
                id=-999,
                note=f"project-999"
            )
            wdamodel.project.add(new, wdamodel.db_engine)
        else:
            data["p999"] = wdamodel.project.json(p999)

        p2 = wdamodel.project.get(id=-1, engine=wdamodel.db_engine)
        if not p2:
            data['p2'] = "no p2"

        # update
        # wdamodel.project.update(
        #     engine=wdamodel.db_engine,
        #     id=3,
        #     data={
        #         "username": "hehe",
        #         "company": "shucheng",
        #         "uid": "1",
        #         "note": f"{datetime.datetime.now()}",
        #         "name": f"project-{random.randint(1, 99)}"
        #     }
        # )

        # delete = true
        # wdamodel.project.remove(id=11, engine=wdamodel.db_engine)

        # get list
        projects = wdamodel.project.filter(
            fliters={},
            engine=wdamodel.db_engine,
            reverse=True,
            limit=5,
            offset=5,
            order_by='id')
        data["list"] = []
        for _p in projects:
            data["list"].append({
                "id": _p.id,
                "data": _p.note,
                "name": f"{_p.name}",
                "del": _p.delete,
            })

        self.all1000()

        return data
