# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'estudiantes.alumno'
    _description = 'Alumno'
    
    nombre = fields.Char(string='Nombre', required=True)
    apellido = fields.Char(string='Apellido', required=True)
    fecha_nacimiento = fields.Date(string='Fecha de Nacimiento', required=True)
    nro_legajo = fields.Integer(string='Nro de Legajo', required=True)
    email = fields.Char(string='Email', required=True)
    telefono = fields.Char(string='Teléfono', required=True)
    direccion = fields.Char(string='Dirección', required=True)
    pais_id = fields.Many2one('res.country', string='País', required=True)

    _sql_constraints = [
        ('nro_legajo_unique', 'unique(nro_legajo)', 'El número de legajo debe ser único.')
    ]
    
    def __str__(self):

        return f'{self.nombre} {self.apellido}' if self.nombre and self.apellido else 'Nombre No Disponible'





class Programa(models.Model):
    _name = 'estudiantes.programa'
    _description = 'Programa Educativo'

    nombre = fields.Char(string='Nombre', required=True)
    descripcion = fields.Text(string='Descripción')

    @api.model
    def create(self, vals):
        """Método sobrescrito para asegurar que siempre haya un nombre único para el programa."""
        if 'nombre' in vals:
            nombre_existente = self.search([('nombre', '=', vals['nombre'])])
            if nombre_existente:
                raise ValueError("Ya existe un programa con ese nombre.")
        return super(Programa, self).create(vals)





class Inscripcion(models.Model):
    _name = 'estudiantes.inscripcion'
    _description = 'Inscripción de Alumno a Programa'

    alumno_id = fields.Many2one('estudiantes.alumno', string='Alumno', required=True)
    programa_id = fields.Many2one('estudiantes.programa', string='Programa', required=True)

    @api.model
    def create(self, vals):
        """Verifica la inscripción de un alumno en un programa antes de crear la inscripción."""
        alumno = self.env['estudiantes.alumno'].browse(vals['alumno_id'])
        programa = self.env['estudiantes.programa'].browse(vals['programa_id'])
        
        # Validación para comprobar si el alumno ya está inscrito en el programa
        if self.search([('alumno_id', '=', alumno.id), ('programa_id', '=', programa.id)]):
            raise ValueError(f'El alumno {alumno.nombre} ya está inscrito en el programa {programa.nombre}.')
        
        return super(Inscripcion, self).create(vals)
