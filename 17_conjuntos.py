f"""
Tenemos dos cursos:

python = {"Manuel", "Carlos", "Ana", "Pedro", "Lucía"}
sql = {"Carlos", "Ana", "Sofía", "Miguel", "Manuel"}

Tu tarea:
1. Identifica a los estudiantes inscritos en ambos cursos.
2. Identifica a los estudiantes que solamente están en Python.
3. Identifica a los estudiantes que solamente están en SQL.
4. Obtén todos los estudiantes inscritos, sin repetir nombres.
Conceptos: intersection(), difference() y union().
"""

python = {"Manuel", "Carlos", "Ana", "Pedro", "Lucía"}
sql = {"Carlos", "Ana", "Sofía", "Miguel", "Manuel"}

resumen = f"""
Estudiantes incritos en ambos cursos: {python.intersection(sql)}
Estudiantes solamente en Python:      {python.difference(sql)}
Estudiantes solamente en SQL:         {sql.difference(python)}
Todos lo estudiantes:                 {python.union(sql)}
"""

print(resumen)