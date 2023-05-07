class Universidad:
    def __init__(self, name, n_carreras, n_facultades):
        self.nombre = name
        self.carreras = n_carreras
        self.facultades = n_facultades

    def establecer_nombre(self, n):
         self.nombre = n

    def establecer_carreras(self, n):
        self.carreras = n

    def establecer_facultades(self, n):
        self.facultades = n

    def obtener_nombre(self):
        return self.nombre

    def obtener_carreras(self):
        return self.carreras
    
    def obtener_facultades(self):
         return self.facultades
    
    def __str__(self):
        return "Universidad: %s, Número de carreras: %d, Número de facultades: %d\n" \
            %( self.nombre, self.carreras, self.facultades)
                