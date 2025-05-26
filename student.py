"""
Módulo para la gestión de estudiantes y sus calificaciones.

Define la clase Student para representar a un estudiante
y sus atributos.
"""
class Student:
    """
    Representa a un estudiante con su ID, nombre, calificaciones y estado académico.
    """
    def __init__(self,student_id,name):
        """_summary_
        Constructor de estudiante
        Args:
            student_id (floar): ID de estudiante
            name (string): nombre del estudiante

        Raises:
            ValueError: Los primeros 2 campos no pueden ser omitidos
        """
        if not student_id or not name:
            raise ValueError("Student ID and Name can't be empy")

        self.id = student_id
        self.name =name
        self.grades = []
        self.letter_grade = 'N/A'
        self.ispassed = ""
        self.honor = False

    def add_grades(self, grade):
        """_summary_
        Funcion para agregar notas a un estudiante
        Args:
            grade (float): Nota a agregar

        Returns:
            void: Se agrega la nota al array de notas de estudiante
        """
        if not isinstance(grade, (int, float)):
            print(f"Error: Grade '{grade}' for {self.name} must be a number.")
            return False
        if not (0 <= grade <= 100):
            print(f"Error: Grade {grade} for {self.name} is out of the 0-100 range.")
            return False
        self.grades.append(grade)
        return True

    def calc_average(self):
        """
        Calcula el promedio de todas las calificaciones del estudiante.

        Returns:
            float: El promedio de las calificaciones, o 0.0 si no hay calificaciones.
        """
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)

    def determine_letter_grade(self):
        """
        Determina la calificación por letra del estudiante basada en su promedio.

        Returns:
            str: La calificación por letra (A, B, C, D, F).
        """
        avg = self.calc_average()
        if 90 <= avg <= 100:
            return 'A'
        if 80 <= avg <= 89:
            return 'B'
        if 70 <= avg <= 79:
            return 'C'
        if 60 <= avg <= 69:
            return 'D'
        else:
            return 'F'

    def determine_pass(self):

        """
        Determina si el estudiante ha aprobado o reprobado.

        Returns:
            str: "Passed" si el promedio es 60 o más, "Failed" en caso contrario.
        """

        if self.calc_average() >=60:
            return "Passed"
        else:
            return "Failed"

    def check_honor(self):
        """
        Verifica si el estudiante califica para honores (promedio > 90).
        Actualiza el atributo 'honor' del estudiante.
        """
        if self.calc_average()>90:
            self.honor = True

    def delete_grade(self, index):
        """
        Elimina una calificación de la lista de calificaciones por su índice.

        Args:
            index (int): El índice de la calificación a eliminar.
        """
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print(f"Error: Índice {index} fuera de rango para las calificaciones de {self.name}.")

    def report(self):
        """
        Imprime un informe detallado del estudiante.
        """
        print("ID: " + self.id)
        print("Name is: " + self.name)
        print("Grades Count: " + str(len(self.grades)))
        print(f"Final Grade = {self.calc_average}")

def startrun():
    """
    Función de prueba para demostrar el uso de la clase Student.
    """
    a = Student("099","Nicolas")
    a.add_grades(100)
    a.add_grades(50) # broken
    a.calc_average()
    a.check_honor()
    a.delete_grade(0) # IndexError
    a.report()

startrun()
