mysql> update etudiant
    -> set age=20
    -> where id=1;
Query OK, 1 row affected (0.00 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from etudiant;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  1 | spaghetti | betty    |  20 | betty.spaghetti@laplateforme.io |
|  2 | steak     | chuck    |  45 | chuck.steak@laplateforme.io     |
|  3 | doe       | john     |  18 | john.doe@laplateforme.io        |
|  4 | barnes    | binkie   |  16 | binkie.barnes@laplateforme.io   |
|  5 | dupuis    | gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  6 | dupuis    | martin   |  18 | martin.dupuis@laplateforme.io   |
+----+-----------+----------+-----+---------------------------------+
6 rows in set (0.00 sec)