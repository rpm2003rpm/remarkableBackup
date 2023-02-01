## @package remarkableBackup
#  Read the remarkable metadata files and create the corresponding folder 
#  structure
# 
#  @author  Rodrigo Pedroso Mendes
#  @version V1.0
#  @date    01/02/23 12:10:35
#
#  #LICENSE# 
#    
#  Copyright (c) 2023 Rodrigo Pedroso Mendes
#
#  Permission is hereby granted, free of charge, to any  person   obtaining  a 
#  copy of this software and associated  documentation files (the "Software"), 
#  to deal in the Software without restriction, including  without  limitation 
#  the rights to use, copy, modify,  merge,  publish,  distribute, sublicense, 
#  and/or sell copies of the Software, and  to  permit  persons  to  whom  the 
#  Software is furnished to do so, subject to the following conditions:        
#   
#  The above copyright notice and this permission notice shall be included  in 
#  all copies or substantial portions of the Software.                         
#   
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,  EXPRESS OR 
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE  WARRANTIES  OF  MERCHANTABILITY, 
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
#  AUTHORS OR COPYRIGHT HOLDERS BE  LIABLE FOR ANY  CLAIM,  DAMAGES  OR  OTHER 
#  LIABILITY, WHETHER IN AN ACTION OF  CONTRACT, TORT  OR  OTHERWISE,  ARISING 
#  FROM, OUT OF OR IN CONNECTION  WITH  THE  SOFTWARE  OR  THE  USE  OR  OTHER  
#  DEALINGS IN THE SOFTWARE. 
#    
################################################################################
# importing the library
import os
import json
import sys

#Goes trough the list creating the necessary folders and dowloading the files 
def openUp(parent, lista):
    for item in lista:
        if item["parent"] == parent:
            if item["type"] == "CollectionType":
                os.mkdir(item["visibleName"])
                os.chdir(item["visibleName"])
                openUp(item["name"], lista)
                os.chdir("..")
            elif item["type"] == "DocumentType":
                os.system('curl -o "' + item["visibleName"]     + \
                          '.pdf" http://remarkable/download/'   + \
                          item["name"]                          + \
                          '/placeholder')

#Read the metadata and call the openUp function
if __name__ == "__main__":
    lista = []
    os.chdir(sys.argv[1])
    for files in os.listdir("."):
        if files.endswith("metadata"):
            f = open(files)
            data = json.load(f)
            name = files[:-9]
            if (not data['deleted']):
                lista.append({"name"        : name, \
                              "parent"      : data["parent"], \
                              "type"        : data["type"], \
                              "visibleName" : data["visibleName"]})
            f.close()
    openUp("", lista)
    os.chdir("..")


