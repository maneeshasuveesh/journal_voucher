from odoo import models,fields,api,_

class ResCompany(models.Model):
    _inherit = 'res.company'


    fax = fields.Char('Fax')
