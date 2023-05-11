#1
numerals = [2, 3, 6, 9, 12, 15]
del numerals[2]
print(numerals)

len(numerals)
print(f"délka je {len(numerals)}")
sum(numerals)
print(f"součet je {sum(numerals)}")

#2
data = [1945, 1889, 2006, 2001, 1999, 2015, 1212]
min(data)
print(f"nejmenší je {min(data)}")
max(data)
print(f"největší je {max(data)}")
data[0], data[1] = data[1], data[0]
data[5], data[6] = data[6], data[5]
print("novy seznam dat:", data)

#3
salary = [16000, 18000, 20000, 25000, 30000, 45500]
high_salary = salary[4:]
print("vysoke platy:", high_salary)
salary[2] = 23458
print("platy:", salary)
salary.sort(reverse=True)
print("serazeny seznam platu:", salary)

#4 
cisla = [2, 4, 6, 8]
cisla_na_druhou = [4, 16, 36, 64]
vysledny_seznam = cisla + cisla_na_druhou
print(vysledny_seznam)