day = int(input())
year = day//365
day -= year*365
month = day//30
day -= month*30
print(f"{year} ano(s)")
print(f"{month} mes(es)")
print(f"{day} dia(s)")