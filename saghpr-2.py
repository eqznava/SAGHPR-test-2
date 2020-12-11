class Herramienta:
    def __init__(self):
        self.__NombreHerramienta = ''
        self.__Medida = ''
        self.__Uso = ' '
        self.__Estado = ''
        self.__NumeroHerramientas = 0
    def GetNombreHerramienta(self):
        return self.__NombreHerramienta
    def GetMedida(self):
        return self.__Medida
    def GetUso(self):
        return self.__Uso
    def GetEstado(self):
        return self.__Estado
    def GetNumeroHerramientas(self):
        return self.__NumeroHerramientas
    def SetNombreHerramienta(self,nomHerramienta):
        self.__NombreHerramienta = nomHerramienta
    def SetMedida(self,medida):
        self.__Medida = medida
    def SetUso(self,uso):
        self.__Uso = uso
    def SetEstado(self,estado):
        self.__Estado = esatdo
    def SetNumeroHerramientas(self, numeroHerramientas):
        self.__NumeroHerramientas = numeroHerramientas

class PartesDeRepuesto:
    def __init__(self):
        self.__NombreParte = ''
        self.__Descripcion = ''
        self.__CantidadPartes = 0

class Equipo(Herramienta,PartesDeRepuesto):
    def __init__(self):
        self.__ID = ''
        self.__NombreEquipo = ''
        self.__Datasheets = ''
        self.__Tips = ''
    def GetID(self):
        return self.__ID
    def GetNombreEquipo(self):
        return self.__NombreEquipo
    def GetDataSheet(self):
        return self.__Datasheets
    def GetTips(self):
        return self.__Tips
    def SetID(self,id):
        self.__ID = id
    def SetNombreEquipo(self,nombreequipo):
        self.__NombreEquipo = nombreequipo
    def SetDataSheet(self,datasheet):
        self.__Datasheets = datasheet
    def SetTips(self,tips):
        self.__Tips = tips
    def MostrarEquipo(self):
        print('\n')
        print('')

class MaintenanceInformationalBot()
