class cosmatic:
    def __init__ (c,name,brand,price):
        c.name = name
        c.brand = brand
        c.price = price
    def return_detail(c):
        return c.name, c.brand, c.price


a=cosmatic("lipstic","nayaka",500)
print(a.return_detail())              #('lipstic', 'nayaka', 500)
b=cosmatic("powder","ponds",150)
print(b.return_detail())              #('powder', 'ponds', 150)
c=cosmatic("cream","fair & lovely",60)
print(c.return_detail())              #('cream', 'fair & lovely', 60)
d=cosmatic("oil","coconut",800)
print(d.return_detail())              #('oil', 'coconut', 800)
e=cosmatic("perfume","foog",350)
print(e.return_detail())
('perfume', 'foog', 350)
