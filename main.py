def eng_kichigi(a, b, c):
    return min(a, b, c)

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

print("Eng kichigi:", eng_kichigi(a, b, c))
```

```python
def eng_kichigi(*sonlar):
    return min(sonlar)

a = int(input("Birinchi sonni kiriting: "))
b = int(input("Ikkinchi sonni kiriting: "))
c = int(input("Uchinchi sonni kiriting: "))

print("Eng kichigi:", eng_kichigi(a, b, c))
