# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import time

from odoo import api, models
from odoo.exceptions import UserError
from odoo.tools.misc import formatLang
from odoo.tools.translate import _


class reportProvvigionale(models.AbstractModel):
    _name = "report.abc_contacts_sales_commissions.report_provvigioni_pdf"
    _description = "ReportProvvigionale"

    @api.model
    def _get_report_values(self, docids, data=None):
        # docids required by caller but not used

        date_format = data["form"]["date_format"]

        docargs = {
            "doc_ids": data["ids"],
            "doc_model": self.env["abc.lines_sales_commission"],
            "data": data["form"],
            "docs": self.env["abc.lines_sales_commission"].browse(data["ids"]),
            "company": self.env.company,
            #"get_move": self._get_move,
            #"tax_lines": self._get_tax_lines,
            "format_date": self._format_date,
            "data_da": self._format_date(data["form"]["data_da"], date_format),
            "data_a": self._format_date(data["form"]["data_a"], date_format),
            #"registry_type": data["form"]["registry_type"],
            #"invoice_total": self._get_move_total,
            #"tax_registry_name": data["form"]["tax_registry_name"],
            "env": self.env,
            "formatLang": formatLang,
            #"compute_totals_tax": self._compute_totals_tax,
            #"l10n_it_count_fiscal_page_base": data["form"]["fiscal_page_base"],
            #"only_totals": data["form"]["only_totals"],
            "date_format": date_format,
            #"year_footer": data["form"]["year_footer"],
        }
        return docargs
    
    def _format_date(self, my_date, date_format):
        # supporting both cases, as data['form']['from_date'] is string
        if isinstance(my_date, str):
            formatted_date = time.strftime(
                date_format, time.strptime(my_date, "%Y-%m-%d")
            )
        else:
            formatted_date = my_date.strftime(date_format)
        return formatted_date or ""