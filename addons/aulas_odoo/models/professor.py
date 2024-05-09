from odoo import models, fields


class CadastroProfessor(models.Model):
    _name = "cadastro.professor"
    _description = "Cadastro de professores"
    
    nome = fields.Char(string="Nome do Professor", required=True)
    idade = fields.Integer(string="Idade")
    email = fields.Char(string="Email")
    admissao = fields.Date(string="Data da admissão")
    materia_lec = fields.Selection([
        ('logica', 'Lógica'),
        ('matematica', 'Matemática'),
        ('python', 'Python')
    ]) 
    titulacao = fields.Selection([
    ('graduacao', 'Graduação'),
    ('mestrado', 'Mestrado'),
    ('doutorado', 'Doutorado')
    ], string="Titulação Acadêmica")
    