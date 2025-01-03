import csv

with open("aluno_star_wars.csv","w", encoding="utf-8"):
     csv.writer(f,delimiter=",", lineterminator="\n").writerows()