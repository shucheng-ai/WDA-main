#!/usr/bin/env python3
# coding:utf-8
from .base import BaseHandler
from config import DOC_FILES


class HelpHandler(BaseHandler):

    def _get(self, **kwargs):
        """
         Layout_design-product_feature.pdf
         Layout_design-user_manual.pdf
         {
                "key": "1",
                "name": "Layout 说明文档",
                "url": "/api/pdf?pdf_name=Layout_design-user_manual",
                "pdf_url": "/pdf?pdf_name=Layout_design-user_manual"
            },
            {
                "key": "2",
                "name": "Layout 产品手册",
                "url": "/api/pdf?pdf_name=Layout_design-product_feature",
                "pdf_url": "/pdf?pdf_name=Layout_design-product_feature"
            }
        """
        data = []
        index = 0
        for d in DOC_FILES:
            index += 1
            data.append({
                "key": f"{index}",
                "name": d["name"],
                "url": f"/api/pdf?pdf_name={d['path']}",
                "pdf_url": f"/pdf?pdf_name={d['path']}"
            })
        return {"data": data}
