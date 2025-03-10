mysql> select * from etudiant where age between 18 and 25
    -> order by age;
+----+-----------+----------+-----+---------------------------------+
| id | nom       | prenom   | age | email                           |
+----+-----------+----------+-----+---------------------------------+
|  3 | doe       | john     |  18 | john.doe@laplateforme.io        |
|  6 | dupuis    | martin   |  18 | martin.dupuis@laplateforme.io   |
|  5 | dupuis    | gertrude |  20 | gertrude.dupuis@laplateforme.io |
|  1 | spaghetti | betty    |  23 | betty.spaghetti@laplateforme.io |
+----+-----------+----------+-----+---------------------------------+
4 rows in set (0.00 sec)