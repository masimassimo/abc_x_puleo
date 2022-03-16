# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class saleOrder(models.Model):
    _inherit = "sale.order"
    _name = "sale.order"
    
    provvigioni_sline_ids = fields.One2many(comodel_name = "abc.lines_sales_commission", inverse_name="riferimento_ordine", string = "Righe provvigioni", help = "Specchietto righe provvigioni.", tracking = True)
    

                
class saleOrderLine(models.Model):
    _inherit = "sale.order.line"
    _name = "sale.order.line"
    
    def write(self, vals):
        result = super(saleOrderLine, self).write(vals)
        
        for record in self:
            if record.order_id.partner_id.agenti_ids:
                agenti = record.order_id.partner_id.agenti_ids
                
                for agente in agenti:
                    provvigioni_agente = agente.provvigioni_ids
                    
                    for provvigione_agente in provvigioni_agente:
                                        tipo = provvigione_agente.tipo
                                        importo = provvigione_agente.importo
                                        percentuale = provvigione_agente.percentuale
                                        contatto = provvigione_agente.contatto
                                        prodotto = None
                                        categoria_prodotto = None
                                        prodotto_attuale = None
                                        categoria_prodotto_attuale = None

                                        if tipo == "regola_prodotto":
                                            prodotto = provvigione_agente.prodotto

                                        if tipo == "regola_categoria_prodotto":
                                            categoria_prodotto = provvigione_agente.categoria_prodotto

                                        if record.product_id:
                                            prodotto_attuale = record.product_id

                                        if record.product_id.categ_id:
                                            categoria_prodotto_attuale = record.product_id.categ_id

                                     
                                        if (prodotto_attuale != None and ((prodotto == prodotto_attuale) or (categoria_prodotto == categoria_prodotto_attuale))):
                                                    _logger.info("-------- IF VERO ------- ")
                                                    record.order_id.provvigioni_sline_ids = [(0, 0, {
                                                                                            "tipo": tipo,
                                                                                            "prodotto": prodotto.id,
                                                                                            "categoria_prodotto": categoria_prodotto,
                                                                                            "importo": importo,
                                                                                            "percentuale": percentuale,
                                                                                            "contatto": contatto.id,
                                                                                            "riferimento_riga_ordine": record.id
                                                                                            })]
        return result