#hemoglobiini

sukupuoli = input("mikä on biologinen sukupuolesi?" )

if sukupuoli == "nainen":
    hemoglobiini = float(input("anna hemoglobiniarvosi g/l: "))

if sukupuoli == "nainen" and hemoglobiini <= 116:
    print("hemoglobiiniarvosi on alhainen.")

if sukupuoli == "nainen" and hemoglobiini >= 117 and hemoglobiini <=175:
    print("hemoglobiiniarvosi on normaali.")

if sukupuoli == "nainen" and hemoglobiini >= 176:
    print("hemoglobiiniarvosi on korkea.")


if sukupuoli == "mies":
    hemoglobiini = float(input("anna hemoglobiiniarvosi g/l: "))

if sukupuoli == "mies" and hemoglobiini <= 133:
    print("hemoglobiiniarvosi on alhainen.")

if sukupuoli == "mies" and hemoglobiini >= 134 and hemoglobiini <=195:
    print("hemoglobiiniarvosi on normaali.")

if sukupuoli == "mies" and hemoglobiini >=196:
    print("hemoglobiiniarvosi on korkea.")
