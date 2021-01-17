#PRIMERO MAS UTIL 
#DESCOMPRIME Y MUEVE A UN CARPETA ESPECIFICA LOS ARCHIVOS XML PARA SU PROCESAMIENTO 
import zipfile 
import os
import tarfile , gzip, shutil
from datetime import datetime
import xml.etree.ElementTree as ET
import csv
import errno
abc = datetime.now()
try:
    fechamili = datetime.now()
    fecha = fechamili.strftime("%d-%m-%Y (%H-%M-%S.%f)")
    car = ("Fecha {}").format(fecha)
    os.mkdir(car)
    
except OSError as e:
    if e.errno != errno.EEXIST:
        raise
ruta_zip = "Gestores.zip"
ruta_extraccion = "C:\\Users\\Andree\\Desktop\\Nueva carpeta"
password = None
archivo_zip = zipfile.ZipFile(ruta_zip, "r")
try:
    #print(archivo_zip.namelist())
    archivo_zip.extractall(pwd=password, path=ruta_extraccion)
except:
    pass
archivo_zip.close()
#reconociendo archivos y sus tipos 
os.getcwd()
obj = os.scandir('C:\\Users\\Andree\\Desktop\\Nueva carpeta\\Gestores') 
a = []
for entry in obj :
  if entry.is_dir() or entry.is_file(): 
    a.append(entry.name)
#print(a) 
obj.close() 
ruta = 'C:\\Users\\Andree\\Desktop\\Nueva carpeta\\Gestores'
#print(len(a))
for h in a:
  nombre, extension = os.path.splitext(h)
  if extension == '.7z' :
    #print(".7z")
    n = ( '7z x {} -C:\\Users\\Andree\\Desktop\\Nueva carpeta\\Gestores' ).format(h)
    os.system(n)
  elif extension == '.gz':
    continue
    #print("archivos GZ ",'---->',h)
    #j = ('{}').format(h)
    #print(j, "printer with J ")
    #with gzip.open(j, 'rb') as f_in:
      #o = ('{}').format(nombre)
      #print(o)
      #with open(o, 'wb') as f_out:
        #shutil.copyfileobj(f_in, f_out)
  else:
    continue
for h in a:
    nombre, extension = os.path.splitext(h)
    if extension == '.xml':
        #print("archiuvo xml", extension, h , nombre)
        #print("antes de mover:") 
        #print(os.listdir(ruta)) 
        archivo = ('C:\\Users\\Andree\\Desktop\\Nueva carpeta\\Gestores\\{}').format(h)
        #print(archivo)
        #cap_dest ruta 
        cap_dest = ('C:\\Users\\Andree\\Desktop\\Nueva carpeta\\{}').format(car)
        #print("despues de mover:")
        dest = shutil.move(archivo, cap_dest)  
#print(car, 'impresion --x--x-x-x-x-x-x-x-x')
new_rut = ('C:\\Users\\Andree\\Desktop\\Nueva carpeta\\{}').format(car)
os.getcwd()
obj = os.scandir(new_rut) 
t = []
for entry in obj :
  if entry.is_dir() or entry.is_file(): 
    t.append(entry.name)
#print(t) 
obj.close() 
#ruta = ('C:\\Users\\Andree\\Desktop\\Nueva carpeta\\{}').format(car) 
#print(len(t))
#print("#------#-----#-------#------#----##---#---#_#-")
for v in t:
  #print(v)
  txt = ('C:\\Users\\Andree\\Desktop\\Nueva carpeta\\{}\\{}').format(car,v)
  #archivo = open("data.csv", "a")
  tree = ET.parse(txt)
  root = tree.getroot()
  root.tag
  root.attrib
  l = []
  fechamiliz = datetime.now()
  fechacasa = fechamiliz.strftime("%d-%m-%Y (%H-%M-%S.%f)")
  no_file = ("C:\\Users\\Andree\\Desktop\\Nueva carpeta\\{}\\data{}{}.csv").format(car,fechacasa,v)
  archivo = open(no_file, "a")
  for f in root.iter('TABLE') :
    b = f.attrib
    l.append(b['attrname'])
  j = []
  data = {}
  now = datetime.now()
  l = []
  for f in root.iter('TABLE') :
    b = f.attrib
    l.append(b['attrname'])
  j = []
  data = {}
  for i in l:
    #print(i)
    for g in root.iter('ROW'):
      #print((g.attrib))
      archivo.write(str(i))
      archivo.write(str(","))
      archivo.write(str(b))
      archivo.write(str(","))
      archivo.write(str(j))
      archivo.write(str(","))
      archivo.write(str(f))
      archivo.write(str(","))
      archivo.write(str(l))
      archivo.write("\n")
  archivo.close()
abcd = datetime.now()
