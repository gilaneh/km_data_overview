# -*- coding: utf-8 -*-
from datetime import  datetime, timedelta, date
# import random

from odoo import models, fields, api

from colorama import Fore
import json
import logging
import base64
from PIL import Image
import io
class SdProjectOverviewDiagram(models.Model):
    _name = 'km_data_overview.diagram'
    _description = 'km_data_overview.diagram'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    # _order = 'sequence,id asc'

    name = fields.Char(required=True, )
    # project = fields.Many2one('project.project', required=True, )
    # task = fields.Many2many('project.task', required=False, )
    image = fields.Image(required=True, )
