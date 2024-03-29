# -*- coding: utf-8 -*-
"""
Created on Sat Nov  4 20:46:11 2017

@author: Aaron Kong
#for testing purpose
"""

import sqlite3
def data_create(insertions,table_name,conn):
    
    data_curser = conn.cursor()
    
    if table_name == 'agents':
        data_curser.executemany("INSERT INTO agents VALUES(?,?,?)", insertions)
        conn.commit()
    elif table_name == 'stores':
        data_curser.executemany("INSERT INTO stores VALUES(?,?,?,?)", insertions)
        conn.commit()
    elif table_name == 'categories':
        data_curser.executemany("INSERT INTO categories VALUES(?,?)", insertions)
        conn.commit()
    elif table_name == 'products':
        data_curser.executemany("INSERT INTO products VALUES(?,?,?,?)", insertions)
        conn.commit()
    elif table_name == 'carries':
        data_curser.executemany("INSERT INTO carries VALUES(?,?,?,?)", insertions)
        conn.commit()
    elif table_name == 'customers':
        data_curser.executemany("INSERT INTO customers VALUES(?,?,?,?)", insertions)
        conn.commit()
    elif table_name == 'orders':
        data_curser.executemany("INSERT INTO orders VALUES(?,?,?,?)", insertions)
        conn.commit()
    elif table_name == 'olines':
        data_curser.executemany("INSERT INTO olines VALUES(?,?,?,?,?)", insertions)
        conn.commit()
    elif table_name == 'deliveries':
        data_curser.executemany("INSERT INTO deliveries VALUES(?,?,?,?)", insertions)
        conn.commit()
        
def main():
    #where the databas has been created
    conn = sqlite3.connect('./pronew.db')
    
    table_curser =  conn.cursor()
    table_curser.executescript('''drop table if exists deliveries; 
                              drop table if exists olines; 
                              drop table if exists orders; 
                              drop table if exists customers;
                              drop table if exists carries;
                              drop table if exists products;
                              drop table if exists categories;
                              drop table if exists stores;
                              drop table if exists agents;

                                create table agents (
                                  aid           text,
                                  name          text,
                                  pwd       	text,
                                  primary key (aid));
                                create table stores (
                                  sid		int,
                                  name		text,
                                  phone		text,
                                  address	text,
                                  primary key (sid));
                                create table categories (
                                  cat           char(3),
                                  name          text,
                                  primary key (cat));
                                create table products (
                                  pid		char(6),
                                  name		text,
                                  unit		text,
                                  cat		char(3),
                                  primary key (pid),
                                  foreign key (cat) references categories);
                                create table carries (
                                  sid		int,
                                  pid		char(6),
                                  qty		int,
                                  uprice	real,
                                  primary key (sid,pid),	
                                  foreign key (sid) references stores,
                                  foreign key (pid) references products);
                                create table customers (
                                  cid		text,
                                  name		text,
                                  address	text,
                                  pwd		text,
                                  primary key (cid));
                                create table orders (
                                  oid		int,
                                  cid		text,
                                  odate		date,
                                  address	text,
                                  primary key (oid),
                                  foreign key (cid) references customers);
                                create table olines (
                                  oid		int,
                                  sid		int,
                                  pid		char(6),
                                  qty		int,
                                  uprice	real,
                                  primary key (oid,sid,pid),
                                  foreign key (oid) references orders,
                                  foreign key (sid) references stores,
                                  foreign key (pid) references products);
                                create table deliveries (
                                  trackingNo	int,
                                  oid		int,
                                  pickUpTime	date,
                                  dropOffTime	date,
                                  primary key (trackingNo,oid),
                                  foreign key (oid) references orders);
                                PRAGMA foreign_keys = ON;

                                delete from deliveries;
                                delete from olines;
                                delete from orders;
                                delete from carries;
                                delete from customers;
                                delete from stores;
                                delete from products;
                                delete from categories;
                                delete from agents;
                                
                                
                                --Now, Let's insert some test data:
                                
                                INSERT INTO categories VALUES('dai','dairy');
                                INSERT INTO categories VALUES('bak','Bakery');
                                INSERT INTO categories VALUES('mea','Meat and seafood');
                                INSERT INTO categories VALUES('bev','Beverages ');
                                INSERT INTO categories VALUES('can','Canned Goods ');
                                INSERT INTO categories VALUES('dry','Dry Goods ');
                                INSERT INTO categories VALUES('cle','Cleaners');
                                INSERT INTO categories VALUES('per','Personal Care');
                                
                                
                                INSERT INTO products VALUES('p1','4L milk 1%','ea','dai');
                                INSERT INTO products VALUES('p2','dozen large egg','ea','dai');
                                
                                INSERT INTO products VALUES('p3','cream cheese','ea','dai');
                                INSERT INTO products VALUES('p12','cream heese','ea','dai');
                                INSERT INTO products VALUES('p13','cream eese','ea','dai');
                                INSERT INTO products VALUES('p14','cream ese','ea','dai');
                                INSERT INTO products VALUES('p15','cream se','ea','dai');
                                INSERT INTO products VALUES('p16','cream e','ea','dai');
                                INSERT INTO products VALUES('p17','cream eeeeee','ea','dai');
                                INSERT INTO products VALUES('p4','400g coffee','ea','bev');
                                INSERT INTO products VALUES('p5','1.5L orange juice','ea','bev');
                                INSERT INTO products VALUES('p6','600g lean beef','ea','mea');
                                INSERT INTO products VALUES('p7','500g poultry','ea','mea');
                                INSERT INTO products VALUES('p8','1L detergent','ea','cle');
                                INSERT INTO products VALUES('p9','300ml dishwashing liquid','ea','cle');
                                INSERT INTO products VALUES('p10','400ml canned beef ravioli','ea','can');
                                INSERT INTO products VALUES('p11','500ml canned noodle soup','ea','can');
                                
                                
                                INSERT INTO stores VALUES(1,'Canadian Tire','780-111-2222','Edmonton South Common');
                                INSERT INTO stores VALUES(2,'Canadian Superstore','780-111-3333','Edmonton South Common');
                                INSERT INTO stores VALUES(3,'Walmart','587-111-222','Edmonton Westmount');
                                INSERT INTO stores VALUES(4,'Save-On-Foods','780-333-444','101-109 St NW');
                                INSERT INTO stores VALUES(5,'No Frills','780-444-555','104-80 Ave');
                                INSERT INTO stores VALUES(6,'Safeway','780-555-666','109-82 Ave');
                                INSERT INTO stores VALUES(7,'Organic Market','780-666-777','110-83 Ave');
                                INSERT INTO stores VALUES(8,'lucky 97','780-666-777','56-132 St NW');
                                
                                
                                INSERT INTO customers VALUES('c1','davood','CS Dept,University of Alberta', 00000000);
                                INSERT INTO customers VALUES('c2','john doe','111-222 Ave', 00000001);
                                INSERT INTO customers VALUES('c3','peter','102-83 Ave', 00000002);
                                INSERT INTO customers VALUES('c4','jessica','101-54 St NW', 00000003);
                                INSERT INTO customers VALUES('c5','allen','4520-9569 Vegas Rd NW', 00000004);
                                INSERT INTO customers VALUES('c6','paul','105-74 Ave', 00000005);
                                INSERT INTO customers VALUES('c7','ashley','78-23 Ave', 00000006);
                                INSERT INTO customers VALUES('c8','emma','96-89 St NW', 00000007);
                                INSERT INTO customers VALUES('c9','mia','87 Strathearn Crescent NW', 00000008);
                                INSERT INTO customers VALUES('c10','oliver','91 Saskatchewan Dr', 00000009);
                                
                                INSERT INTO agents VALUES('a1', 'joshua', 10000000);
                                INSERT INTO agents VALUES('a2', 'harry', 10000001);
                                INSERT INTO agents VALUES('a3', 'oliver', 10000002);
                                INSERT INTO agents VALUES('a4', 'emily', 10000003);
                                INSERT INTO agents VALUES('a5', 'peter', 10000004);
                                INSERT INTO agents VALUES('a6', 'jessica', 10000005);
                                
                                INSERT INTO carries VALUES(2,'p1',100,4.7);
                                INSERT INTO carries VALUES(2,'p2',80,2.6);
                                INSERT INTO carries VALUES(1,'p1',60,5.5);
                                INSERT INTO carries VALUES(3,'p1',100,4.5);
                                INSERT INTO carries VALUES(1,'p3',20,3.5);
                                INSERT INTO carries VALUES(4,'p4',50,5);
                                INSERT INTO carries VALUES(4,'p7',70,9);
                                INSERT INTO carries VALUES(6,'p5',65,5);
                                INSERT INTO carries VALUES(5,'p1',100,6.5);
                                INSERT INTO carries VALUES(5,'p9',150,6);
                                INSERT INTO carries VALUES(2,'p8',90,7);
                                INSERT INTO carries VALUES(4,'p3',45,5);
                                
                                
                                INSERT INTO orders VALUES(1,'c1','2017-09-26','Athabasca Hall, University of Alberta');
                                INSERT INTO orders VALUES(2,'c2','2017-09-26','111-222 Ave');
                                INSERT INTO orders VALUES(3,'c3',date('now','-5 day'),'134-53 Ave');
                                INSERT INTO orders VALUES(4,'c3',date('now','-6 day'),'134-53 Ave');
                                INSERT INTO orders VALUES(5,'c4',date('now','-3 day'),'75-103 St');
                                INSERT INTO orders VALUES(6,'c4',date('now','-2 day'),'75-103 St');
                                INSERT INTO orders VALUES(7,'c5',date('now','-12 day'),'102-114 St');
                                INSERT INTO orders VALUES(8,'c6',date('now'),'87-Jasper Ave');
                                INSERT INTO orders VALUES(9,'c2',date('now'),'76-102 St');
                                INSERT INTO orders VALUES(10,'c2',date('now'),'79-101 St');
                                INSERT INTO orders VALUES(11,'c8',date('now'),'105-83 Ave');
                                
                                
                                INSERT INTO olines VALUES(1, 2,'p2',2,2.8);
                                INSERT INTO olines VALUES(2, 2,'p1',1,4.7);
                                INSERT INTO olines VALUES(3, 2,'p2',4,2.6);
                                INSERT INTO olines VALUES(4, 1,'p1',2,3);
                                INSERT INTO olines VALUES(5, 2,'p2',2,2.6);
                                INSERT INTO olines VALUES(5, 3,'p1',6,5.5);
                                INSERT INTO olines VALUES(6, 4,'p4',1,6);
                                INSERT INTO olines VALUES(6, 4,'p7',1,10);
                                INSERT INTO olines VALUES(6, 6,'p5',2,4.3);
                                INSERT INTO olines VALUES(7, 5,'p1',2,6);
                                INSERT INTO olines VALUES(7, 5,'p9',1,6);
                                INSERT INTO olines VALUES(8, 2,'p8',1,7);
                                INSERT INTO olines VALUES(1, 4,'p3',1,5);
                                INSERT INTO olines VALUES(7, 2,'p2',1,6);
                                INSERT INTO olines VALUES(11, 3,'p1',2,4.5);
                                
                                
                                
                                INSERT INTO deliveries VALUES(1, 1,'2017-10-02 23:37:46',NULL);
                                INSERT INTO deliveries VALUES(2, 2,'2017-10-02 19:37:46','2017-10-02 23:37:46');
                                INSERT INTO deliveries VALUES(3, 10,datetime('now'),NULL);
                                INSERT INTO deliveries VALUES(4, 3,datetime('now','-4 day'),datetime('now','-3 day'));
                                INSERT INTO deliveries VALUES(5, 4,datetime('now','-6 day'),datetime('now','-2 day'));
                                INSERT INTO deliveries VALUES(6, 5,datetime('now','-2 day'),datetime('now','-1 day'));
                                INSERT INTO deliveries VALUES(7, 6,datetime('now','-1 day'),NULL);
                                INSERT INTO deliveries VALUES(8, 7,datetime('now','-6 day'),NULL);
                                INSERT INTO deliveries VALUES(9, 8,datetime('now'),NULL);
                                INSERT INTO deliveries VALUES(10, 9,datetime('now'),NULL);

                                ''')
    conn.commit()
   
    read_curser_agents = conn.cursor()
    read_curser_agents.execute("SELECT * FROM agents;")
    rows_agents =  read_curser_agents.fetchall()
    for each in rows_agents:
        print (each[0], each[1], each[2])
    read_curser_customers = conn. cursor()
    read_curser_customers.execute("SELECT * FROM customers")
    rows_customers = read_curser_customers.fetchall()
    for each in rows_customers:
        print ((each[0:(len(rows_customers)+1)]))
    
    read_curser_customers.execute("SELECT * FROM carries")
    rows_customers1 = read_curser_customers.fetchall()
    for each in rows_customers1:
        print ((each[0:(len(rows_customers1)+1)]))
    
    #read_curser_customers.execute("SELECT*FROM customers WHERE cid=? and pwd=?;",('c2','1'))
    #rows_customers = read_curser_customers.fetchall() 
    
    #print (rows_customers)
    #print(len(rows_customers))
    
    
    conn.close()
main()
    