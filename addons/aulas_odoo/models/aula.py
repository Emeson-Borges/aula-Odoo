from odoo import api, exceptions, fields, models


class AulasOdoo(models.Model):
    _name = "aula.odoo"
    _description = "Modelo Aula"

    nome_aula = fields.Char(string="Nome Aula", required=True)
    descricao_aula = fields.Text(string="Descrição da aula")
    minutos_aula = fields.Selection(
        [("um_minuto", "1 min"), ("cinco_minutos", "5 min"), ("dez_minutos", "10 min")],
        required=True,
        default="dez_minutos",
    )
    professor = fields.Char(string="Professor", required=True)
    data_aula = fields.Date(string="Data", required=True)
    state = fields.Selection(
        [("scheduled", "Agendada"), ("done", "Realizada"), ("lost", "Perdida")],
        string="Estado",
        default="scheduled",
    )

    # @api.multi
    # @api.model
    def mark_as_lost(self):
        for aula in self:
            if aula.state != "lost":
                aula.write({"state": "lost"})
        return True

    # @api.model
    def mark_as_done(self):
        for aula in self:
            if aula.state != "done":
                aula.write({"state": "done"})
        return True

    # @api.multi
    def save_data(self):
        for aula in self:
            # Verifica se todos os campos obrigatórios estão preenchidos
            if not (aula.nome_aula and aula.professor and aula.data_aula):
                raise exceptions.ValidationError(
                    "Por favor, preencha todos os campos obrigatórios."
                )

            if aula.id:  # Verifica se o registro já existe
                aula.write(
                    {  # Atualiza os campos do registro existente
                        "descricao_aula": aula.descricao_aula,
                        "minutos_aula": aula.minutos_aula,
                        "professor": aula.professor,
                        "data_aula": aula.data_aula,
                    }
                )
            else:
                self.env["aula.odoo"].create(
                    {  # Cria um novo registro
                        "nome_aula": aula.nome_aula,
                        "descricao_aula": aula.descricao_aula,
                        "minutos_aula": aula.minutos_aula,
                        "professor": aula.professor,
                        "data_aula": aula.data_aula,
                    }
                )
        return True
