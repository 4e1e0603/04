
true_value: bool = True
false_value: bool = False


# Podmínka

expression = 1.0

if expression: # expression True
    ...

if true_value: # Pokud je vyhodnoceno na logickou pravdu
    print(true_value) # Tiskni

if false_value:
    print(false_value)

if not false_value:
    print(false_value)

if 1:
    print(1)

if 0:
    print(0)

if -1:
    print(-1)

if 1.0:
    print(1.0)

if -1.0:
    print(-1.0)

if bool(1):
    print(1)

if int(1).__bool__():
    print("....")

if " ":
    print("True")

if "":
    print("False")

expression = False and (False or True)
expression = 1 and 1

# class Klass:
#     pass
# a = Klass()
# if bool(a):
#     print(a)

if expression:
    ...
else:
    ...

result = 2
if condition:
    result = 1

if condition:
    result = 1
else:
    result = 2

if condition:
    ...
elif condition2:
    ...
else:
    ...

condition = False

if ((condition1 and condition2) or (condition3)):
    print("v")

if (not condition):
    print("v")
