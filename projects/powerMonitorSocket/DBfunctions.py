'''
Created on Aug 5, 2013

@author: atmelino
'''

import mysql.connector


    
def measureStore(lV3,cmA3,pw3):

    # print 'measureStore called'

    myString='%d,%d,%d ' %(lV3,cmA3,pw3)
    print 'lV3 cmA3 pw3 %s ' %myString
    #print myString
    query = "INSERT INTO myvalues (lV3,cmA3,pw3) VALUES (%s); " % myString
    print query
 

    later=0
    if later>1:
        config = {
          'user': 'solarPanel',
          'password': 'solarPanel',
          'host': '127.0.0.1',
          'database': 'solarPanel',
          'raise_on_warnings': False,
        }
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
    
        query = "UPDATE myvalues SET '%s'" % myString
    
        #print query
    
        cursor.execute(query)
            
        cnx.commit()
        cursor.close()
        cnx.close()
        


