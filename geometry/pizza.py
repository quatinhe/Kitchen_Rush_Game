from geometry.geometry import Geometry
from core.obj_reader2 import my_obj_reader


class PizzaGeometry(Geometry):
    def __init__(self, width=1, height=1, depth=1):
        super().__init__()

        base_position_data = my_obj_reader('parteDentro.obj')
        queijo_position_data = my_obj_reader('parteExterior.obj')
        azeitonas_position_data = my_obj_reader('pega.obj')
        #chourico_position_data = my_obj_reader('pizzaChourico.obj')

        position_data = base_position_data + queijo_position_data + azeitonas_position_data 

        color_data = [0, 0, 0] * len(base_position_data)
        color_data += [0.5, 0, 0] * len(queijo_position_data)
        color_data += [0, 0, 0] * len(azeitonas_position_data)
        #color_data += [1, 0, 0] * len(chourico_position_data)

        self.add_attribute("vec3", "vertexPosition", position_data)
        self.add_attribute("vec3", "vertexColor", color_data)
        self.count_vertices()
