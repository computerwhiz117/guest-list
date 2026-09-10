#This program will print a list of guests invited to a party

guests = ['Nathan Vetterlain','Charlet Chung', 'LilyPiuchu']

cannot_make_it = 'Nathan Vetterlain'
guests.remove(cannot_make_it)
guests.insert(0, 'Robert Downey Jr.')
guests.insert(1, 'Caitlin Glass')
guests.append('Scarlett Johansson')

print(f"\n {cannot_make_it} cannot make it for dinner.")
print("I could only invite two people for the dinner")
cannot_come = guests.pop(0)
too_full = guests.pop(2)
sorry = guests.pop()
print(f"\n Sorry {cannot_come}, {too_full}, and {sorry} I can't invite you due to limited space.")

print(f"\n {guests} you are all still invited to have dinner.")
del guests[0:2]
print(f"\n Hello, {guests} you are all invited to have dinner in my house.")