'''
Created on Aug 5, 2013

@author: atmelino
'''

import mysql.connector


    
def measureStore(nowdatetime, lV1, cmA1, pw1, lV2, cmA2, pw2, lV3, cmA3, pw3):
    
    # print 'measureStore called'
    # print 'measureStore %s' %nowdatetime
    tableName = 'D' + nowdatetime[:4] + '_' + nowdatetime[5:7] + '_' + nowdatetime[8:10]
    
    makeTable(tableName)
    # makeTable('D2016')

    myString = "'%s',%4.2f,%4.2f,%6.0f,%4.2f,%4.2f,%6.0f,%4.2f,%4.2f,%6.0f " % (nowdatetime, lV1, cmA1, pw1, lV2, cmA2, pw2,lV3, cmA3, pw3)
    # print 'date lV3 cmA3 pw3 %s ' % myString
    # print myString
    query = "INSERT INTO " + tableName + "(date,lV1, cmA1, pw1, lV2, cmA2, pw2,lV3,cmA3,pw3) VALUES (%s); " % myString
    # print query
 

    later = 1
    if later > 0:
        config = {
          'user': 'solarPanel',
          'password': 'solarPanel',
          'host': '127.0.0.1',
          'database': 'solarPanel',
          'raise_on_warnings': False,
        }
        cnx = mysql.connector.connect(**config)
        cursor = cnx.cursor()
    
   
        # print query
    
        cursor.execute(query)
            
        cnx.commit()
        cursor.close()
        cnx.close()
        

def makeTable(name):
    
    query = "CREATE  TABLE IF NOT EXISTS  "
    query += name
    query += " ( `id` INT NOT NULL AUTO_INCREMENT "
    query += ",  PRIMARY KEY (`id`) "
    query += ", username VARCHAR(45) NOT NULL"
    query += ", date DATETIME  "
    query += ", lV1 float  "
    query += ", cmA1 float  "
    query += ", pw1 float  "
    query += ", lV2 float  "
    query += ", cmA2 float  "
    query += ", pw2 float  "
    query += ", lV3 float  "
    query += ", cmA3 float  "
    query += ", pw3 float  "
    query += "  ) ENGINE=InnoDB"
    
    # print query
    
    config = {
      'user': 'solarPanel',
      'password': 'solarPanel',
      'host': '127.0.0.1',
      'database': 'solarPanel',
      'raise_on_warnings': False,
    }
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    # print query

    cursor.execute(query)
        
    cnx.commit()
    cursor.close()
    cnx.close()
   
   
   
