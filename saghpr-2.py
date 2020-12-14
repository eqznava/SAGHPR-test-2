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
    def MostartHerramienta(self):
        print('══════════════════════════════════════════════════════════════════\n')
        print('Nombre de herramienta:',self.GetNombreHerramienta())
        print('Medida de la herramienta:',self.GetMedida())
        print('Uso de la herramienta:',self.GetUso())
        print('Estado de la herramienta:',self.GetEstado())
        print('Numero de herramientasa usar:',self.GetNumeroHerramientas(),'\n')
        print('══════════════════════════════════════════════════════════════════\n')

class CajaHerramientas(Herramienta):
    def __init__(self,path):
        self.__ListaHerramientas =[]
        self.__Path = path
    def CargarHerramientas(self):
        try:
            fichero = open(self.__Path,'r')
        except:
            print('\n')
            print('╔═══════════════════════════════════════════════════════════════╗')
            print('║   ERROR: No existe el archivo de la caja de herramientas.     ║')
            print('╚═══════════════════════════════════════════════════════════════╝\n')
        else:
            cajaHerramientas = fichero.readlines()
            fichero.close()
            if(len(cajaHerramientas)>0):
                for herramienta in cajaHerramientas:
                    datos = herramienta.split('|')
                    if(len(datos)==5):
                        nuevaCajaHerramientas = CajaHerramientas()
                        nuevaCajaHerramientas.SetNombreHerramienta(datos[0])
                        nuevaCajaHerramientas.SetMedida(datos[1])
                        nuevaCajaHerramientas.SetUso(datos[2])
                        nuevaCajaHerramientas.SetEstado(datos[3])
                        nuevaCajaHerramientas.SetNumeroHerramientas(datos[4])
                        self.__ListaHerramientas = self.__ListaHerramientas + [nuevaCajaHerramientas]
                print('INFO: Tenemos',len(self.__ListaHerramientas),'herramientas en la caja.')
    def buildNewBoxTool(self,nuevacajaherramientas):
        self.__ListaHerramientas = self.__ListaHerramientas + [nuevaCajaHerramientas]
    def GuardarNuevaCaja(self):
        try:
            fichero = open(self.__Path,'w')
        except:
            print('\n')
            print('╔═══════════════════════════════════════════════════════════════╗')
            print('║   ERROR: No se pueden guardar los datos.                      ║')
            print('╚═══════════════════════════════════════════════════════════════╝\n')
        else:
            for herramientas in self.__ListaHerramientas:
                texto = herramienta.GetNombreHerramienta()+'|'
                texto = texto + herramienta.GetMedida()+'|'
                texto = texto + herramienta.GetUso()+'|'
                texto = texto + herramienta.GetEstado()+'|'
                texto = texto + herramienta.GetNumeroHerramientas()+'\n'
                fichero.write(texto)
            fichero.close()
            print('\n')
            print('╔═══════════════════════════════════════════════════════════════╗')
            print('║   SUCCES: Datos almacenados exitosamente.                     ║')
            print('╚═══════════════════════════════════════════════════════════════╝\n')
    def MostrarCaja(self):
        if(len(self.__ListaHerramientas)==0):
            print('NO HAY HERRAMIENTAS EN LA CAJA')
        elif(len(self.__ListaHerramientas)==1):
            print('NUMERO DE HERRAMIENTAS EN LA CAJA:',len(self.__ListaHerramientas),'herramienta')
        elif(len(self.__ListaHerramientas)>1):
            print('NUMERO DE HERRAMIENTAS EN LA CAJA:',len(self.__ListaHerramientas),'herramientas')
        for herramienta in self.__ListaHerramientas:
            herramienta.MostartHerramienta()
    def BuscarHerramientaPorNombre(self,nombreherramienta):
        listaencontrados = []
        for herramienta in self.__ListaHerramientas:
            if herramienta.GetNombreHerramienta() == nombreherramienta:
                listaencontrados = listaencontrados + [herramienta]
    def BorrarHerramientaPorNombre(self, nombreherramienta):
        listafinal = []
        for herramienta in self.__ListaHerramientas:
            if herramienta.GetNombreHerramienta() != nombreherramienta:
                listafinal = listafinal + [herramienta]
                print('INFO: ',len(self.__ListaHerramientas)-len(listafinal),'herramienta retirada de la caja.')
                #══════════════════FALTAN LA CLASE ALMACEN DE PARTES DE REPUESTOS Y SUS METODOS.

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
        print('\t\t\tE Q U I P O')
        print('══════════════════════════════════════════════════════════════════\n')
        print('ID de Equipo:',self.GetID())
        print('Nombre de Equipo:',self.GetNombreEquipo())
        print('Especificaciones tecnicas:',self.GetDataSheet())
        print('Consejos de experiencias pasadas:',self.GetTips(),'\n')
        print('══════════════════════════════════════════════════════════════════\n')
        print('\tH E R R A M I E N T A S  Y  P A R T E S  D E  R E P U E S T O')
        print('N')

class MaintenanceInformationalBot()
