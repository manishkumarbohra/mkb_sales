# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

from odoo import api, fields, models


class BulkSalesOrderCancel(models.Model):
    _inherit = 'sale.order'

    def bulk_sales_order_cancel(self):
        """this method used to sales order confirmation in bulk."""
        for sales in self:
            sales.update({'state':'cancel'})
