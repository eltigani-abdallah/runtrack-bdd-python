mysql> select * from etudiant
    -> order by nom;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  4 | barnes    | binkie   |  16 | binkie.barnes@laplateforme.io   |
|  3 | doe       | john     |  18 | john.doe@laplateforme.io        |
|  5 | dupuis    | gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  6 | dupuis    | martin   |  18 | martin.dupuis@laplateforme.io   |
|  1 | spaghetti | betty    |  23 | betty.spaghetti@laplateforme.io |
|  2 | steak     | chuck    |  45 | chuck.steak@laplateforme.io     |
+----+-----------+----------+-----+---------------------------------+
6 rows in set (0.00 sec)