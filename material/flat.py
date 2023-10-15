"""Support for flat shader"""

import OpenGL.GL as GL
from material.material import Material

class FlatMaterial(Material):
    """Flat material"""
    def __init__(self, texture=None, property_dict={}):
        vertex_shader_code = """
        struct Light
        {
            // 1 = AMBIENT, 2 = DIRECTIONAL, 3 = POINT
            int lightType;
            // used by all lights
            vec3 color;
            // used by directional lights
            vec3 direction;
            // used by point lights
            vec3 position;
            vec3 attenuation;
        };

        uniform Light light0;
        uniform Light light1;
        uniform Light light2;
        uniform Light light3;

        vec3 lightCalc(Light light, vec3 pointPosition, vec3 pointNormal)
        {
            float ambient = 0;
            float diffuse = 0;
            float specular = 0;
            float attenuation = 1;
            vec3 lightDirection = vec3(0,0,0);

            if (light.lightType == 1) // ambient light
            {
                ambient = 1;
            }
            else if (light.lightType == 2) // directional light
            {
                lightDirection = normalize(light.direction);
            }
            else if(light.lightType == 3) // point light
            {
                lightDirection = normalize(pointPosition - light.position);
                float distance = length(light.position - pointPosition);
                attenuation = 1.0 /(light.attenuation[0] + light.attenuation[1]*distance + light.attenuation[2]*distance);
            }

            if (light.lightType > 1) //directional or point light
            {
                pointNormal = normalize(pointNormal);
                diffuse = max(dot(pointNormal, -lightDirection), 0.0);
                diffuse *= attenuation;
            }

            return light.color * (ambient+diffuse+specular);
        }

        uniform mat4 projectionMatrix;
        uniform mat4 viewMatrix;
        uniform mat4 modelMatrix;
        in vec3 vertexPosition;
        in vec2 vertexUV;
        in vec3 faceNormal;
        out vec2 UV;
        out vec3 light;

        void main()
        {
            gl_Position = projectionMatrix * viewMatrix * modelMatrix * vec4(vertexPosition, 1);
            UV = vertexUV;
            // calculate total effect of lights on color
            vec3 position = vec3(modelMatrix * vec4(vertexPosition, 1));
            vec3 normal = normalize( mat3(modelMatrix) * faceNormal );
            light = vec3(0,0,0);
            light += lightCalc(light0, position, normal);
            light += lightCalc(light1, position, normal);
            light += lightCalc(light2, position, normal);
            light += lightCalc(light3, position, normal);
        }
        """
        fragment_shader_code = """
        uniform vec3 baseColor;
        uniform bool useTexture;
        uniform sampler2D texture;
        in vec2 UV;
        in vec3 light;
        out vec4 fragColor;

        void main()
        {
            vec4 color = vec4(baseColor, 1.0);
            if (useTexture)
                color *= texture2D(texture, UV);
            color *= vec4(light, 1);
            fragColor = color;
        }
        """
        super().__init__(vertex_shader_code, fragment_shader_code)

        self.add_uniform("vec3", "baseColor", [1.0, 1.0, 1.0])
        self.add_uniform("Light", "light0", None)
        self.add_uniform("Light", "light1", None)
        self.add_uniform("Light", "light2", None)
        self.add_uniform("Light", "light3", None)
        self.add_uniform("bool", "useTexture", 0)
        if texture == None:
            self.add_uniform("bool", "useTexture", False)
        else:
            self.add_uniform("bool", "useTexture", True)
            self.add_uniform("sampler2D", "texture", [texture.texture_ref, 1])


        self.locate_uniforms()

        # render both sides?
        self._setting_dict["doubleSide"]=True
        # render triangles as wireframe?
        self._setting_dict["wireframe"]=False
        # line thichness for wireframe rendering
        self._setting_dict["lineWidth"]=1

        self.set_properties(property_dict)

    def update_render_settings(self):
        if self.setting_dict["doubleSide"]:
            GL.glDisable(GL.GL_CULL_FACE)
        else:
            GL.glEnable(GL.GL_CULL_FACE)

        if self._setting_dict["wireframe"]:
            GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_LINE)
        else:
            GL.glPolygonMode(GL.GL_FRONT_AND_BACK, GL.GL_FILL)

        GL.glLineWidth(self.setting_dict["lineWidth"])
