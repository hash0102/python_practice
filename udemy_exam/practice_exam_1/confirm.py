import datetime

print(datetime.datetime.strptime("2025-10-30 14:45", "%Y-%m-%d %H:%M"))

print('----------------------------------')

pi = 3.14159

print(f"pi is {pi:2}")
print(f"pi is {pi:2f}")
print(f"pi is {pi:.2f}")
print(f"pi is {pi:.2}")

print('-'*30)

from dateutil import parser

parser_time = parser.parse("2025-10-30 14:45")
print(parser_time)
print(type(parser_time))
