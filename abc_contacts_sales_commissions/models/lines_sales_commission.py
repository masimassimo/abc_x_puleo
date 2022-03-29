# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from datetime import datetime
import logging
_logger = logging.getLogger(__name__)

class abc_lines_sales_commission(models.Model):
    _name = "abc.lines_sales_commission"
    _description = "Sotto modulo che gestisce le righe di provvigione relative ai vari ordini di vendita."
    _order = 'riferimento_riga_ordine asc, riferimento_ordine asc, riferimento_fattura asc, contatto asc'
    
    #Faccio l'override della funzione create per inserire il numero di sequenza per la linea di provvigione.
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('abc.lines_sales_commission.sequence') or _('New')
            #vals['data_creazione'] = self.datetime.now()
        result = super(abc_lines_sales_commission, self).create(vals)
        return result
    
    #Campo relativo alla data di creazione.
    data_creazione = fields.Date(string = "Data creazione", help = "La data in cui la riga di provvigione viene creata.", store = True, Tracking = True, index = True, default = lambda self: datetime.now())
    
    #Nome della linea di provvigione. Questo corrisponde ad un numero di sequenza che viene incrementato automaticamente.
    name = fields.Char(string="Nome riga provvigione", help = "Il nome dato alla riga di provvigione.", store=True, required=True, tracking=True, index = True, copy = False, readonly = True, default=lambda self: _('New'))
    
    #Tipologia di regola.
    tipo = fields.Selection( [("regola_prodotto", "Prodotto"), 
                              ("regola_categoria_prodotto", "Categoria prodotto"), 
                              ("regola_importo_fisso", "Importo fisso")], 
                            help =  "Prodotto - Regola che vale su un determinato prodotto. \n"
                                    "Categoria prodotto - Regola che vale su una determinata categoria di prodotti. \n"
                                    "Importo fisso - Regola di provvigione ad importo costante. \n",
                            tracking = True, required = True, default = "regola_importo_fisso", readonly = False
                           )
    
    #Moneta corrente obbligatoria per il campo importo.
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.user.company_id.currency_id)
    
    #Importo relativo alla provvigione calcolato sulla percentuale assegnata al contatto.
    importo = fields.Monetary(string = "Importo \N{euro sign} ", help = "Importo di provvigione dettato dalla tipologia di regola selezionata e dalla percentuale.", tracking = True, compute_sudo=True, default = 0)
    
    #Importo relativo alla percentuale
    importo_percentuale = fields.Float(string = "Importo percentuale", help = "Importo sulla percentuale scelta.", tracking = True, default = 0)
    
    #Percentuale di provvigione assegnata al contatto.
    percentuale = fields.Float(string = "Percentuale %", help = "Percentuale di provvigione assegnata al contatto.", tracking = True, default = 0)
    
    #Contatto al quale si vuole dare la provvigione.
    contatto = fields.Many2one("res.partner", string = "Contatto", help = "Contatto al quale si desidera dare la provvigione.", tracking = True, required = True, store = True)
    
    #Campo prodotto che permette di selezionare qualsiasi prodotto se selezionato il tipo regola_prodotto
    prodotto = fields.Many2one("product.product", string = "Prodotto", help = "Seleziona il prodotto sul quale si riceve la provvigione.", tracking = True, readonly = True)
    
    #Campo categoria_prodotto che permette di selezionare qualsiasi prodotto se selezionato il tipo regola_categoria_prodotto
    categoria_prodotto = fields.Many2one("product.category", string = "Categoria prodotto", help = "Seleziona la categoria di prodotti sulla quale si riceve la provvigione.", tracking = True, readonly = True)
        
    #Campo riferimento_ordine che relazione la riga di provvigione ad un preciso ordine di vendita.
    riferimento_ordine = fields.Many2one("sale.order", string = "Riferimento ordine", help = "Ordine di vendita da cui scaturisce la riga di provvigione.", ondelete="cascade", required = True) 
    
    #Campo che serve per effettuare il filtro sulle righe dell'ordine in modo da poter selezionare una riga relativa all'ordine in corso.
    riferimento_ordine_fittizio = fields.Integer(string = "Riferimento ordine fittizio", help = "Campo che serve per filtrare le righe dell'ordine corrente. ") 
    
    #Campo riferimento_fattura che relazione la riga di provvigione ad una precisa fattura.
    riferimento_fattura = fields.Many2one("account.move", string = "Riferimento fattura", help = "Fattura da cui scaturisce la riga di provvigione.", readonly = True)
    
    #Campo riferimento_riga_ordine che relazione la riga di provvigione ad una precisa riga di ordine.
    riferimento_riga_ordine = fields.Many2one("sale.order.line", string = "Riferimento riga ordine", help = " ID Riga d'ordine da cui scaturisce la provvigione.", ondelete="cascade",)
    
    #Campo che indica lo stato di liquidazione della riga di provvigione.
    stato_provvigione = fields.Selection( [("da_liquidare", "Da liquidare"), 
                              ("liquidata", "Liquidata")], 
                            help = "Stato di liquidazione della riga di provvigione.", tracking = True, default = "da_liquidare", required = True)
    
    #Funzione che al passaggio di stato_provvigione da 
    @api.depends("stato_provvigione")
    def _calcolaDataLiquidazione(self):
        for record in self:
            if(record.stato_provvigione == "liquidata"):
                record.data_liquidazione = datetime.now()
            else:
                record.data_liquidazione = None
                _logger.info("La provvigione ancora non è stata liquidata.")
    
    #Campo che indica la data in cui viene liquidata la provvigione.
    data_liquidazione = fields.Date(string = "Data liquidazione", help = "Data in cui viene liquidata la provvigiione", readonly = False, compute = _calcolaDataLiquidazione)
    
    
    '''
    #Tasto che chiama il Wizard.
    def action_apri_wizard(self):
        return {
            "type": "ir.actions.act_window",
            "name": _('Mark as Done'),
            "view_mode": "form",
            "view_type": "form",
            "target": "new",
            "view_id": self.env.ref("abc_contacts_sales_commissions.report_provvigioni_view_form").id,
            "res_model": "abc.report_provvigioni"
        }
    '''
