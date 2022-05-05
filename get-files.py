from pickle import TRUE
import psycopg2
import requests
import pathlib
from os import path
import os.path
import paramiko
from typing import NamedTuple

# class Index(enum.Enum):
#     file_id = 0,
#     file_infraction_description = 1
#     file_url = 2

def connectToDatabase(params):
    conn = psycopg2.connect(
        host = params.host,
        database = params.database,
        user = params.user,
        port = params.port,
        password = params.password
    )
    return conn.cursor()


def executeQuery(psql, sqlQuery):
    psql.execute(sqlQuery)
    
    return list(psql.fetchall())

def createDirTree():
    
    os.system('mkdir infracoes_ftp')
    os.system('mkdir infracoes_fevereiro/FALHA_DE_ENQUADRAMENTO/')
    os.system('mkdir infracoes_fevereiro/FALTA_DE_LUMINOSIDADE/')
    os.system('mkdir infracoes_fevereiro/FORA_DE_FOCO/')

def getFileFromServer(server, username, record):

    # todo: 'else' statement
    if(isFtp):
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(server, username = username, pkey = key)
        sftp = ssh.open_sftp()

        imgPath = "path" + str(record[2])
        
        if record[1] == 'FALHA DE ENQUADRAMENTO':
            print("Writing file '" + record[1] + ".jpg'...")
            sftp.get(remotepath = str(imgPath), localpath ='path'+ str(record[0]) + '.jpg')
        elif record[1] == 'FALTA DE LUMINOSIDADE':
            print("Writing file '" + record[1] + ".jpg'...")
            sftp.get(remotepath = str(imgPath), localpath='path'+ str(record[0]) + '.jpg')
        elif record[1] == 'FORA DE FOCO':
            print("Writing file '" + record[1] + ".jpg'...")
            sftp.get(remotepath = str(imgPath), localpath='path')
        sftp.close()
        ssh.close()


def writeFiles(fileRecords):
    for record in fileRecords:
        getFileFromServer(
            HOST_PATH,
            'very nice and cool intern that gave me his key',
            record   
        )

class Credential(NamedTuple):
    host: str
    database: str
    port: str
    user: str
    password: str

credential = Credential(
    "very cool credential"
)

# todo
isFtp = TRUE
sftpPort = 0
KEY_PATH = 'very cool path'
key = 'very cool path'
HOST_PATH= 'very cool path'


query = ('very professional sql right here')

databaseManager = connectToDatabase(credential)
records = executeQuery(databaseManager,query)
createDirTree()
writeFiles(records)



