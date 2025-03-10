mysql> select * from etudiant
    -> where prenom like "b%";
+----+-----------+--------+-----+---------------------------------+
| id | nom       | prenom | age | email                           |
+----+-----------+--------+-----+---------------------------------+
|  1 | spaghetti | betty  |  23 | betty.spaghetti@laplateforme.io |
|  4 | barnes    | binkie |  16 | binkie.barnes@laplateforme.io   |
+----+-----------+--------+-----+---------------------------------+
2 rows in set (0.00 sec)