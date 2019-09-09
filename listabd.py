#!/usr/bin/python3
# -*- coding: utf-8 -*-

import pymysql
import pymysql.cursors

con = pymysql.connect(host='127.0.0.1',
                      user='katriny',
                      password='1234',
                      db='katriny',
                      charset='utf8',
                      cursorclass=pymysql.cursors.DictCursor)

print("Selecione o que voce deseja fazer")
  print ("1: listar")
  print ("2: Cadastrar ")
  print ("3: Concluir ")
  print ("4: excluir ")
x = int(input())

if x ==1:
	rows = cur.fetchall()

    for row in rows:
        print(row["id"], row["nome"], row["data"], row["prioridade"], row["concluida"],)

if x ==2:
	print("Digite o nome da tabela")
	nome = input()
	print("Digite a data")
	data = input()
	print("Digite a prioridade")
	prioridade = input()
	print("Digite a conclusao")
	concluida = input()
	with con:
      cur = con.cursor()
      sql = "INSERT INTO `katriny` (`nome`, `data`, `prioridade`, `concluida`) VALUES ("+nome+", "+data+", "+prioridade+", "+concluida+")"
      cur.execute(sql)

if x ==3:
	x= input()
	with con:
    	sql = "UPDATE katriny SET conclusao='[V]' WHERE id = "+x+";"
    	cur.execute(sql)

if x ==4:

	x=input()
	with con:
      sql = "DELETE FROM katriny WHERE id = "+x+";"
      cur.execute(sql)
