'''
Created on Aug 5, 2013

@author: atmelino
'''

import mysql.connector


    
def measureStore(lV3,cmA3,pw3):

    # print 'measureStore called'

    myString='%4.2f,%d,%6.0f ' %(lV3,cmA3,pw3)
    print 'lV3 cmA3 pw3 %s ' %myString
    #print myString
    query = "INSERT INTO myvalues (lV3,cmA3,pw3) VALUES (%s); " % myString
    print query
 

    later=0
    if later>0:
        config = {
          'user': 'solarPanel',
          'password': 'solarPanel',
          'host': '127.0.0.1',
          'database': 'solarPanel',
          'raise_on_warnings': False,
        }
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
    
   
        #print query
    
        cursor.execute(query)
            
        cnx.commit()
        cursor.close()
        cnx.close()
        


