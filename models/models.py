# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ssgjose_empresas_contratadoras(models.Model):
     _name = 'ssgjose.hiring_company'
     _description = 'ssgjose.hiring_company'

     name = fields.Char(string="Company")
     email = fields.Char(string="Email")
     phone = fields.Integer(string="Phone")
     project = fields.One2many("project.project","company",string="Projects")
     employees = fields.Integer(string="Employees")
     company_size = fields.Char(string="Company size",compute="_companysize",store=True)

     @api.depends('employees')
     def _tamempresa(self):
          for r in self:
               if r.employees > 0:
                    r.company_size = 'Small'
               if r.employees > 50:
                    r.company_size = 'Medium'
               if r.employees > 100:
                    r.company_size = 'Large'
class ssgjose_proyectos(models.Model):
     _name = 'project.project'
     _inherit = "project.project"

     company = fields.Many2one("ssgjose.hiring_company",string="Comapmy Name",required=True,ondelete="cascade")

class ssgjose_tareas(models.Model):
     _name = 'project.task'
     _inherit = "project.task"