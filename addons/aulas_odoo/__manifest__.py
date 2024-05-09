# Esse arquivo ele aponta para os Arquivos XML, CSV e outras fontes de arquivos

{
    "name": "Gestão de Professores",
    "version": "1.0.1",
    "sequence": 1,
    "author": "Emeson Borges",
    "category": "Marketing",
    "summary": "Aulas sobre Desenvolvimento com Odoo",
    "description": "Essa aula ensina criar um App.",
    # No array Depends deve-se apontar para os modelos que esta sendo herdado
    "depends": [],
    "data": [
        "views/aula.xml",
        "views/cad_professor.xml",
        "security/ir.model.access.csv",
    ],
    "images": ["static/description/emesonicone.png"],
    "installable": True,
    "auto_install": False,
    "application": True,
    "license": "LGPL-3",
}
