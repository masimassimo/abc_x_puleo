from odoo import models, fields, api, _
from odoo.exceptions import UserError
import logging
_logger = logging.getLogger(__name__)

#GUARDA IL MODULO REGISTRO_IVA DI OCA PER COMPRENDERE IL FUNZIONAMENTO DI QUESTO E DEL FILE CSC_REPORT_PROVVIGIONALE IN MODELS E DEL REPORT.

class abc_report_provvigioni(models.TransientModel):
    _name = "abc.report_provvigioni"
    _description = "Wizard stampa report provvigioni"
    
    data_da = fields.Date(string = "Dalla data", help = "Data dalla quale si vuole stampare il report.")
    data_a = fields.Date(string = "Alla data", help = "Data fino alla quale si vuole stampare il report.")
    
    #Campo che indica lo stato di liquidazione della riga di provvigione.
    stato_provvigione = fields.Selection( [
                                            ("non_maturata", "Non maturata"),
                                            ("da_liquidare", "Da liquidare"), 
                                            ("liquidata", "Liquidata")], 
                            help = "Stato di liquidazione della riga di provvigione.", tracking = True, default = "da_liquidare", required = True)
    
    
    contatto = fields.Many2one("res.partner", string = "Contatto", help = "Contatto al quale si desidera dare la provvigione.", tracking = True, store = True, domain = "[('contatti_ids', '!=', False)]")
    
    def stampaReportProvvigioni(self):
        wizard = self
        ccsl_ids = self._get_cscl_ids(wizard)
        _logger.info("CCSL: %s", ccsl_ids)

        datas_form = {}
        datas_form["data_da"] = wizard.data_da
        datas_form["data_a"] = wizard.data_a
        _logger.info(" -------------------- DATA DA: %s", datas_form["data_da"])
        _logger.info(" -------------------- DATA A: %s", datas_form["data_a"])
        datas_form["stato_provvigione"] = wizard.stato_provvigione

        lang_code = self.env.company.partner_id.lang
        lang = self.env["res.lang"]
        lang_id = lang._lang_get(lang_code)
        date_format = lang_id.date_format
        datas_form["date_format"] = date_format
        
        report_name = "abc_contacts_sales_commissions.action_report_provvigioni"
        datas = {"ids": ccsl_ids, "model": "abc.lines_sales_commission", "form": datas_form}
        return self.env.ref(report_name).report_action(self, data=datas)
            
    

    def _get_cscl_ids(self, wizard):
        if(self.contatto and self.data_da and self.data_a):
            _logger.info("TIPO 1")
            cscl = self.env["abc.lines_sales_commission"].search(
                [
                    ("data_creazione", ">=", self.data_da),
                    ("data_creazione", "<=", self.data_a),
                    ("stato_provvigione", "=", self.stato_provvigione),
                    ("contatto", "=", self.contatto.id),
                ],
                order="data_creazione, name",
            )
        elif(self.data_da and self.data_a):
            _logger.info("TIPO 2")
            cscl = self.env["abc.lines_sales_commission"].search(
                [
                    ("data_creazione", ">=", self.data_da),
                    ("data_creazione", "<=", self.data_a),
                    ("stato_provvigione", "=", self.stato_provvigione),
                ],
                order="data_creazione, name",
            )
        elif(self.contatto):
            _logger.info("TIPO 3")
            cscl = self.env["abc.lines_sales_commission"].search(
                [
                    ("stato_provvigione", "=", self.stato_provvigione),
                    ("contatto", "=", self.contatto.id),
                ],
                order="data_creazione, name",
            )
        else:
            _logger.info("TIPO 4")
            cscl = self.env["abc.lines_sales_commission"].search(
                [
                    ("stato_provvigione", "=", self.stato_provvigione),
                ],
                order="data_creazione, name",
            )
            
        if( (self.data_da and not self.data_a) or (self.data_a and not self.data_da) ):
            raise UserError(_("Per comporre il report ho bisogno che tu non selezioni nessuna data o che le selezioni entrambe. (Data da, Data a)"))
        if(len(cscl.ids) == 0):
            raise UserError(_("Non posso comporre il report perchè non trovo nessuna provvigione. Assicurati che esista almeno una provvigione per le condizioni selezionate."))
        return cscl.ids
