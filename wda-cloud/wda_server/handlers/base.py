#!/usr/bin/env python3
# coding:utf-8
import json
from flask.views import MethodView
from flask import make_response, request


class BaseHandler(MethodView):
    formdata = {}
    error_403 = {
        'status': 403,
        'msg': 'permission denied',
    }

    def __init__(self, *args, **kwargs):
        super(BaseHandler, self).__init__()

    def get_formdata(self):
        try:
            self.formdata = request.get_json()
        except:
            self.formdata = {}

    def get_arg(self, q, default=None):
        return request.args.get(q, default)

    def json_response(self, data: dict):
        '''
        data = {
                status: 1,
                msg: 'ok',
                data: {name: test},
                kwargs: {info: {data: test}},
            }
        '''
        setkeys = ['cookie', 'headers']
        res = {
            'status': data.get('status', 0),
            'msg': data.get('msg', ''),
            'data': data.get('data', {})
        }
        res.update(data)
        res = json.dumps(res)
        resp = make_response(res)
        for _key in setkeys:
            if data.get(_key):
                set_data = data[_key]
                for k, v in set_data.items():
                    if _key == 'cookie':
                        resp.set_cookie(k, v)
                    elif _key == 'headers':
                        resp.headers[k] = v
        resp.headers['Content-Type'] = 'application/json'
        resp.headers['Access-Control-Allow-Headers'] = 'origin, x-csrftoken, content-type, accept'
        resp.headers['Access-Control-Allow-Origin'] = '*'
        resp.headers['Access-Control-Max-Age'] = 1678000
        return resp

    def _get(self, **kwargs):
        return {}

    def get(self, **kwargs):
        data = self._get()
        return self.json_response(data)

    def _post(self):
        return {}

    def post(self):
        data = self._post()
        return self.json_response(data)

    def _put(self):
        return {}

    def put(self):
        data = self._put()
        return self.json_response(data)

    def _delete(self):
        return {}

    def delete(self):
        data = self._delete()
        return self.json_response(data)
