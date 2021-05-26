class Usuario (models.Model):
    correo = models.CharField(max_length=50, null=False, blank=False, primary_key=True)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    contraseña = models.CharField(max_length=50, null=False, blank=False)


class Administrador (models.Model):
    correo = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    contraseña = models.CharField(max_length=50, null=False, blank=False)


class Profesor (models.Model):
    correo = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)


nombre = models.CharField(max_length=50, null=False, blank=False)
contraseña = models.CharField(max_length=50, null=False, blank=False)
curso = models.CharField(max_length=50, null=False, blank=False)
asignatura = models.CharField(max_length=50, null=False, blank=False)


class Alumno (models.Model):
    correo = models.ForeignKey(Usuario, null=True, on_delete=models.SET_NULL)
    nombre = models.CharField(max_length=50, null=False, blank=False)
    notas = models.CharField(max_length=50, null=False, blank=False)
    asistencia = models.(max_length=50, null=False, blank=False)


class Asignatura(models.Model):
    codigo = models.CharField(max_length=5, null=False, blank=False, primary_key=True)
    nombre = models.CharField(max_length=20, null=False, blank=False)
    cursos = [(“1”, ”1A”), (“2”, ”2A”), (“3”, ”3A”), (“4”, ”4A”),(“5”, ”5A”),(“6”, ”6A”),(“7”, ”7A”), (“8”, ”8A”) ]
    curso = models.CharField(max_length=10, null=True, blank=True, choices=cursos)


class Curso (models.Model):
    curso = models.CharField(max_length=10, null=False, blank=False, primary_key=True)




