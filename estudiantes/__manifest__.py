{
    'name': "estudiantes",

    'summary': "modulo para prueba tecnica",

    'description': """
Este modulo de estudiantes esta creado para una prueba tecnica. Se encarga de crear alumnos, programas e inscripciones. Y ademas tiene un endpoint para la consulta de inscripciones.
    """,

    'author': "mauro fernandez",
    'website': "https://www.yourcompany.com",



    'category': 'Uncategorized',
    'version': '0.1',


    'depends': ['base'],

    # always loaded
    'data': [

        'views/alumno.xml',  # vista alumno
        'views/programa.xml',  # vista programa
        'views/inscripcion.xml',  # vista inscripcion
        'security/security.xml',  # El archivo de seguridad, para definir permisos
        'security/ir.model.access.csv',  # El archivo de accesos
    ],
    'installable': True, #permite instalar el modulo
    'application': True,  #considera aplicacion al modulo


    'demo': [
        'demo/demo.xml',
    ],
}

