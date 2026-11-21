import copy
import unittest

import pandas as pd

localidades = {
    "Ayacucho": {
        "localidades": ["Ayacucho", "Udaquiola", "Solanet"],
        "countries_barrios_cerrados": []
    },
    "Castelli": {
        "localidades": ["Castelli"],
        "countries_barrios_cerrados": []
    },
    "Chascomús": {
        "localidades": ["Chascomús", "Adela"],
        "countries_barrios_cerrados": []
    },
    "Dolores": {
        "localidades": ["Dolores", "Sevigné"],
        "countries_barrios_cerrados": []
    },
    "General Belgrano": {
        "localidades": ["General Belgrano", "Gorchs"],
        "countries_barrios_cerrados": []
    },
    "General Guido": {
        "localidades": ["General Guido", "Labardén"],
        "countries_barrios_cerrados": []
    },
    "General Lavalle": {
        "localidades": ["General Lavalle", "Pavón"],
        "countries_barrios_cerrados": []
    },
    "General Madariaga": {
        "localidades": ["General Juan Madariaga", "Macedo", "Juancho"],
        "countries_barrios_cerrados": []
    },
    "La Costa": {
        "localidades": [
            "San Clemente del Tuyú", "Las Toninas", "Santa Teresita",
            "Mar del Tuyú", "Costa del Este", "Aguas Verdes",
            "Lucila del Mar", "San Bernardo del Tuyú", "Mar de Ajó", "Nueva Atlantis"
        ],
        "countries_barrios_cerrados": ["Costa Esmeralda", "KM 314", "Cuasiarenas", "Punta Médanos","North Beach"]
    },
    "Lezama": {
        "localidades": ["Lezama"],
        "countries_barrios_cerrados": []
    },
    "Maipú": {
        "localidades": ["Maipú", "Las Armas"],
        "countries_barrios_cerrados": []
    },
    "Pila": {
        "localidades": ["Pila", "Casalins"],
        "countries_barrios_cerrados": []
    },
    "Pinamar": {
        "localidades": ["Pinamar", "Ostende", "Valeria del Mar", "Cariló"],
        "countries_barrios_cerrados": ["La Herradura"]
    },
    "Tordillo": {
        "localidades": ["General Conesa", "Villa Roch"],
        "countries_barrios_cerrados": []
    },
    "Villa Gesell": {
        "localidades": ["Villa Gesell", "Mar de las Pampas", "Las Gaviotas", "Mar Azul"],
        "countries_barrios_cerrados": []
    }
}

class Localidad:
    def __init__(self, nombre, partido):
        self.nombre = nombre
        self.partido = partido

    def __repr__(self):
        return f"Localidad(nombre={self.nombre}, partido={self.partido})"

    @classmethod
    def crear(cls, datos, nombre, partido):
        if partido not in datos:
            raise KeyError(f"El partido {partido!r} no existe.")
        if nombre in datos[partido]["localidades"]:
            raise ValueError(f"La localidad {nombre!r} ya existe en {partido!r}.")

        datos[partido]["localidades"].append(nombre)
        return cls(nombre, partido)

    @classmethod
    def leer(cls, datos, partido=None):
        if partido is not None and partido not in datos:
            raise KeyError(f"El partido {partido!r} no existe.")

        partidos = [partido] if partido is not None else datos
        return [
            cls(nombre, nombre_partido)
            for nombre_partido in partidos
            for nombre in datos[nombre_partido]["localidades"]
        ]

    @classmethod
    def actualizar(
        cls, datos, nombre, partido, nuevo_nombre=None, nuevo_partido=None
    ):
        if partido not in datos:
            raise KeyError(f"El partido {partido!r} no existe.")
        if nombre not in datos[partido]["localidades"]:
            raise KeyError(f"La localidad {nombre!r} no existe en {partido!r}.")

        destino = nuevo_partido if nuevo_partido is not None else partido
        nombre_actualizado = nuevo_nombre if nuevo_nombre is not None else nombre
        if destino not in datos:
            raise KeyError(f"El partido {destino!r} no existe.")
        if (
            (destino != partido or nombre_actualizado != nombre)
            and nombre_actualizado in datos[destino]["localidades"]
        ):
            raise ValueError(
                f"La localidad {nombre_actualizado!r} ya existe en {destino!r}."
            )

        localidades_origen = datos[partido]["localidades"]
        if destino == partido:
            indice = localidades_origen.index(nombre)
            localidades_origen[indice] = nombre_actualizado
        else:
            localidades_origen.remove(nombre)
            datos[destino]["localidades"].append(nombre_actualizado)

        return cls(nombre_actualizado, destino)

    @classmethod
    def eliminar(cls, datos, nombre, partido):
        if partido not in datos:
            raise KeyError(f"El partido {partido!r} no existe.")
        if nombre not in datos[partido]["localidades"]:
            raise KeyError(f"La localidad {nombre!r} no existe en {partido!r}.")

        datos[partido]["localidades"].remove(nombre)
        return cls(nombre, partido)


class TestLocalidadCRUD(unittest.TestCase):
    def setUp(self):
        self.datos = {
            "La Costa": {
                "localidades": ["San Clemente", "Santa Teresita"],
                "countries_barrios_cerrados": []
            },
            "Pinamar": {
                "localidades": ["Ostende"],
                "countries_barrios_cerrados": []
            }
        }

    def test_crear_y_leer_localidad(self):
        creada = Localidad.crear(self.datos, "Mar de Ajó", "La Costa")

        self.assertEqual(creada.nombre, "Mar de Ajó")
        leidas = Localidad.leer(self.datos, "La Costa")
        self.assertEqual(
            [localidad.nombre for localidad in leidas],
            ["San Clemente", "Santa Teresita", "Mar de Ajó"]
        )

    def test_crear_localidad_rechaza_partido_inexistente(self):
        with self.assertRaises(KeyError):
            Localidad.crear(self.datos, "Localidad nueva", "Partido nuevo")

    def test_crear_localidad_rechaza_duplicados(self):
        with self.assertRaises(ValueError):
            Localidad.crear(self.datos, "San Clemente", "La Costa")

    def test_leer_todas_las_localidades(self):
        leidas = Localidad.leer(self.datos)

        self.assertEqual(
            [(localidad.nombre, localidad.partido) for localidad in leidas],
            [
                ("San Clemente", "La Costa"),
                ("Santa Teresita", "La Costa"),
                ("Ostende", "Pinamar")
            ]
        )

    def test_actualizar_nombre_y_partido(self):
        actualizada = Localidad.actualizar(
            self.datos,
            "San Clemente",
            "La Costa",
            nuevo_nombre="San Clemente del Tuyú",
            nuevo_partido="Pinamar"
        )

        self.assertEqual(actualizada.nombre, "San Clemente del Tuyú")
        self.assertEqual(actualizada.partido, "Pinamar")
        self.assertEqual(
            self.datos["La Costa"]["localidades"],
            ["Santa Teresita"]
        )
        self.assertEqual(
            self.datos["Pinamar"]["localidades"],
            ["Ostende", "San Clemente del Tuyú"]
        )

    def test_actualizar_rechaza_duplicados(self):
        with self.assertRaises(ValueError):
            Localidad.actualizar(
                self.datos,
                "San Clemente",
                "La Costa",
                nuevo_nombre="Santa Teresita"
            )

    def test_eliminar_localidad(self):
        eliminada = Localidad.eliminar(self.datos, "San Clemente", "La Costa")

        self.assertEqual(eliminada.nombre, "San Clemente")
        self.assertEqual(
            self.datos["La Costa"]["localidades"],
            ["Santa Teresita"]
        )

    def test_eliminar_localidad_inexistente(self):
        with self.assertRaises(KeyError):
            Localidad.eliminar(self.datos, "No existe", "La Costa")


def mostrar_localidades():
    datos = copy.deepcopy(localidades)
    Localidad.crear(datos, "Pinar del Sol", "La Costa")

    # DataFrame de trabajo: una fila por partido/municipio
    localidades_df = pd.DataFrame.from_dict(datos, orient="index")
    localidades_df.index.name = "partido"

    objetos_localidades = []
    for partido, row in localidades_df.iterrows():
        objetos_localidades.extend(
            Localidad(nombre, partido) for nombre in row["localidades"]
        )
    print(objetos_localidades)


if __name__ == "__main__":
    mostrar_localidades()
    unittest.main()
