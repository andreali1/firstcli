#https://docs.python.org/3.8/library/xml.etree.elementtree.html#pull-api-for-non-blocking-parsing
#https://docs.python.org/3/library/xml.dom.minidom.html



#codigo para descompresion 
#import zipfile
#ruta_zip = "Gestores.zip"
#ruta_extraccion = ""
#password = None
#archivo_zip = zipfile.ZipFile(ruta_zip, "r")
#try:
    #print(archivo_zip.namelist())
    #archivo_zip.extractall(pwd=password, path=ruta_extraccion)
#except:
    #pass
#archivo_zip.close()

#codigo parea listar archivos 
#import os 
#obj = os.scandir('Gestores') 
#for entry in obj : 
#	if entry.is_dir() or entry.is_file(): 
#		print(entry.name) 
#obj.close() 






#import xml.etree.ElementTree as ET
#tree = ET.parse('datos.xml')
#root = tree.getroot()
#print(root)

#root.tag
#root.attrib
#print(root.tag, root.attrib)

#for f in root.iter('TABLE') :
  #print(f.attrib)
  #print("")
  

  
  #for u in root.iter('ROWDATA'):
    #print(u.attrib)
    #for g in root.iter('ROW'):
      #print(g.attrib)
    #for y in root.iter('ROW'):
      #print(y.attrib)
  #print(g.attrib)
#print("\n holi ")


import xml.etree.ElementTree as ET
tree = ET.parse('datos.xml')
root = tree.getroot()
#print(root)

root.tag
root.attrib
#for h in root:
  #print(h.attrib )


for f in root.iter('TABLE'):
  print(f.attrib['attrname'])
  print(len(f.attrib['attrname']))

  #for j in root.iter('ROWDATA'):
    #print(j.attrib)



#### nueva descompresion con identificacion de extension 

#####--x-x-x-x-x-x-x-x-x--xx-x-x-x-xx-x-xx-
#codigo parea listar archivos e identificar el tipo de extension y que se hace 
#import os 
#import os.path
#os.getcwd()
#obj = os.scandir('Gestores') 
#a = []
#for entry in obj :
#  if entry.is_dir() or entry.is_file(): 
#    a.append(entry.name)
#print(a) 
#obj.close() 
#for h in a:
#  nombre, extension = os.path.splitext(h)
#  #print("El archivo '{}' se llama '{}' y tiene la extensión '{}'".format(h, nombre, extension))
#  if extension == '.gz' or extension == '.7z' :
#    print("archivo comprimido", extension)
#  elif extension == '.xml':
#    print("archiuvo xml", extension)
#  elif extension == '.csv':
#    print("archivo csv", extension)
#  elif extension == '.DOCX':
#    print("archivo word", extension)
#  else:
#    print("Extension sin determinar ", extension)


