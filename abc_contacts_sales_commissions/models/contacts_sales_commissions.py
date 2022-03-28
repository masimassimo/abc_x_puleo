# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class abc_contacts_sales_commissions(models.Model):
    _name = "abc.contacts_sales_commissions"    
    _description = "Modulo che gestisce le provvigioni sui contatti."
    
    #Faccio l'override della funzione create per inserire il numero di sequenza per la regola.
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('abc.contacts_sales_commissions.sequence') or _('New')
        result = super(abc_contacts_sales_commissions, self).create(vals)
        return result
        
    #Nome della regola. Questo corrisponde ad un numero di sequenza che viene incrementato automaticamente.
    name = fields.Char(string="Nome regola provvigione", help = "Il nome dato alla regola di provvigione.", store=True, required=True, tracking=True, index = True, copy = False, readonly = True, default=lambda self: _('New'))
    
    #Nome della regola.
    #nome = fields.Char(string = "Nome regola", help = "Il nome dato alla regola.", required = True)
    
    #Tipologia di regola.
    tipo = fields.Selection( [("regola_prodotto", "Prodotto"), 
                              ("regola_categoria_prodotto", "Categoria prodotto"), 
                              ("regola_importo_fisso", "Importo fisso")], 
                            help =  "Prodotto - Regola che vale su un determinato prodotto. \n"
                                    "Categoria prodotto - Regola che vale su una determinata categoria di prodotti. \n"
                                    "Importo fisso - Regola di provvigione ad importo costante. \n",
                            tracking = True, required = True, default = "regola_prodotto",
                           )
    
    #Moneta corrente obbligatoria per il campo importo.
    currency_id = fields.Many2one('res.currency', string='Currency', default=lambda self: self.env.user.company_id.currency_id)
    
    #Importo relativo alla provvigione calcolato sulla percentuale assegnata al contatto.
    importo = fields.Monetary(string = "Importo \N{euro sign} ", help = "Importo di provvigione dettato dalla tipologia di regola selezionata e dalla percentuale.", tracking = True, compute_sudo=True, default = 0)
    
    #Percentuale di provvigione assegnata al contatto.
    percentuale = fields.Float(string = "Percentuale %", help = "Percentuale di provvigione assegnata al contatto.", tracking = True, default = 0)
    
    #Contatto al quale si vuole dare la provvigione.
    contatto = fields.Many2one("res.partner", string = "Contatto", help = "Contatto al quale si desidera dare la provvigione.", tracking = True, required = True)
    
    #Campo prodotto che permette di selezionare qualsiasi prodotto se selezionato il tipo regola_prodotto
    prodotto = fields.Many2one("product.product", string = "Prodotto", help = "Seleziona il prodotto sul quale si riceve la provvigione.", tracking = True)
    
    #Campo categoria_prodotto che permette di selezionare qualsiasi prodotto se selezionato il tipo regola_categoria_prodotto
    categoria_prodotto = fields.Many2one("product.category", string = "Categoria prodotto", help = "Seleziona la categoria di prodotti sulla quale si riceve la provvigione.", tracking = True)
    
    #Campo Direzionale che permette di discriminare una regola Direzionale da una Non Direzionale. Qualora il cliente fosse Direzionale verranno considerate solo le regole Direzionali.
    direzionale = fields.Boolean(string = "Direzionale", help = "Campo Direzionale che permette di discriminare una regola Direzionale da una Non Direzionale. Qualora il cliente fosse Direzionale verranno considerate solo le regole Direzionali.", tracking = True, default = False)