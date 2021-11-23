from .base import BaseHandler
from flask import send_file



class PdfHandler(BaseHandler):

    def get(self, **kwargs):
        pdf_name = self.get_arg('pdf_name')
        filepath = f'../static/{pdf_name}.pdf'
        return send_file(filepath, attachment_filename=f'{pdf_name}.pdf', as_attachment=True)