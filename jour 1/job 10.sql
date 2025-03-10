mysql> select * from etudiant
    -> order by age desc;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  2 | steak     | chuck    |  45 | chuck.steak@laplateforme.io     |
|  1 | spaghetti | betty    |  23 | betty.spaghetti@laplateforme.io |
|  5 | dupuis    | gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  3 | doe       | john     |  18 | john.doe@laplateforme.io        |
|  4 | barnes    | binkie   |  16 | binkie.barnes@laplateforme.io   |
+----+-----------+----------+-----+---------------------------------+
5 rows in set (0.00 sec)