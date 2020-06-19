# author: 227Mahaman

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class Filiere(models.Model):
    
    _name='filiere'
    _description='la classe filiere'

    code = fields.Char(string="le code de la filiere")
    name = fields.Char(string="nom de la filiere", required=True)



class Etudiant(models.Model):

    _name="etudiant"
    _description="la classe etudiant"

    matricule = fields.Char(string="le matricule de l'etudiant", required=True)
    name = fields.Char("Nom etudiant")
    prenom = fields.Char("Prénom etudiant")
    adresse = fields.Char("Adresse etudiant")
    telephone = fields.Char("Telephone")
    datenais = fields.Date("Date de Naissance")
    idfiliere = fields.Many2one('filiere', string="FIliere de l'etudiant")