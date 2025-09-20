# Copyright 2020-22 Manish Kumar Bohra <manishkumarbohra@outlook.com>
# License LGPL-3 - See http://www.gnu.org/licenses/Lgpl-3.0.html

from odoo import api, fields, models


class BulkSalesOrderCancel(models.Model):
    _inherit = 'sale.order'

    def merge_duplicate_so_lines(self):
        for sales in self:
            sales_lines = {}
            for line in sales.order_line:
                key = (line.product_id.id, line.price_unit, tuple(sorted((tax.id for tax in line.tax_ids))))
                if key in sales_lines:
                    sales_lines[key].product_uom_qty += line.product_uom_qty
                    line.unlink()
                else:
                    sales_lines[key] = line
        return True

