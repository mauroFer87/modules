from odoo import http
from odoo.http import request
import json

class EstudiantesController(http.Controller):

    @http.route('/estudiantes/programa_alumnos', type='http', auth='public', methods=['GET'], csrf=False)
    def get_alumnos_por_programa(self, programa_id=None):
        if not programa_id:
            return request.make_response(
                json.dumps({'error': 'Programa ID es requerido'}),
                status=400,  # Código de error 400 Bad Request
                headers={'Content-Type': 'application/json'}
            )
        
        try:
            # Validar que el programa_id sea un número entero
            programa_id = int(programa_id)
        except ValueError:
            return request.make_response(
                json.dumps({'error': 'Programa ID debe ser un número entero válido'}),
                status=400,  # Código de error 400 Bad Request
                headers={'Content-Type': 'application/json'}
            )

        # Buscar el programa con el ID proporcionado
        programa = request.env['estudiantes.programa'].sudo().browse(programa_id)
        if not programa.exists():
            return request.make_response(
                json.dumps({'error': 'Programa no encontrado'}),
                status=404,  # Código de error 404 Not Found
                headers={'Content-Type': 'application/json'}
            )

        # Buscar las inscripciones relacionadas con el programa
        inscripciones = request.env['estudiantes.inscripcion'].sudo().search([('programa_id', '=', programa.id)])
        if not inscripciones:
            return request.make_response(
                json.dumps({'error': 'No se encontraron inscripciones para este programa'}),
                status=404,  # Código de error 404 Not Found
                headers={'Content-Type': 'application/json'}
            )

        # Construir la lista de alumnos
        alumnos = [{
            'nombre': inscripcion.alumno_id.nombre,
            'apellido': inscripcion.alumno_id.apellido,
            'legajo': inscripcion.alumno_id.nro_legajo,
            'fecha_nacimiento': str(inscripcion.alumno_id.fecha_nacimiento),
            'email': inscripcion.alumno_id.email,
            'telefono': inscripcion.alumno_id.telefono,
            'pais': {
                'id': inscripcion.alumno_id.pais_id.id,
                'nombre': inscripcion.alumno_id.pais_id.name,
            },
        } for inscripcion in inscripciones]

        return request.make_response(
            json.dumps(alumnos),
            status=200,  # Código de éxito 200 OK
            headers={'Content-Type': 'application/json'}
        )
