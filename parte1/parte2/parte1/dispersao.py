import pandas as pd
import matplotlib.pyplot as plt

datas = [
    "03/01/2017", "04/01/2017", "05/01/2017", "06/01/2017", "09/01/2017", 
    "10/01/2017", "11/01/2017", "12/01/2017", "13/01/2017", "17/01/2017", 
    "18/01/2017", "19/01/2017", "20/01/2017", "23/01/2017", "24/01/2017", 
    "25/01/2017", "26/01/2017", "27/01/2017", "30/01/2017", "31/01/2017", 
    "01/02/2017", "02/02/2017", "03/02/2017", "06/02/2017", "07/02/2017", 
    "08/02/2017", "09/02/2017", "10/02/2017", "13/02/2017", "14/02/2017", 
    "15/02/2017", "16/02/2017", "17/02/2017", "21/02/2017", "22/02/2017", 
    "23/02/2017", "24/02/2017", "27/02/2017", "28/02/2017", "01/03/2017", 
    "02/03/2017", "03/03/2017", "06/03/2017", "07/03/2017", "08/03/2017", 
    "09/03/2017", "10/03/2017", "13/03/2017", "14/03/2017", "15/03/2017", 
    "16/03/2017", "17/03/2017", "20/03/2017", "21/03/2017", "22/03/2017", 
    "23/03/2017", "24/03/2017", "27/03/2017", "28/03/2017", "29/03/2017", 
    "30/03/2017", "31/03/2017", "03/04/2017", "04/04/2017", "05/04/2017", 
    "06/04/2017", "07/04/2017", "10/04/2017", "11/04/2017", "12/04/2017", 
    "13/04/2017", "17/04/2017", "18/04/2017", "19/04/2017", "20/04/2017", 
    "21/04/2017", "24/04/2017", "25/04/2017", "26/04/2017", "27/04/2017", 
    "28/04/2017", "01/05/2017", "02/05/2017", "03/05/2017", "04/05/2017", 
    "05/05/2017", "08/05/2017", "09/05/2017", "10/05/2017", "11/05/2017", 
    "12/05/2017", "15/05/2017", "16/05/2017", "17/05/2017", "18/05/2017", 
    "19/05/2017", "22/05/2017", "23/05/2017", "24/05/2017", "25/05/2017", 
    "26/05/2017", "30/05/2017", "31/05/2017", "01/06/2017"
]

valoresApple = [
    116.15, 116.02, 116.61, 117.91, 118.99, 119.11, 119.75, 119.25, 119.04, 120.0,
    119.99, 119.78, 120.0, 120.08, 119.97, 121.88, 121.94, 121.95, 121.63, 121.35,
    128.75, 128.53, 129.08, 130.29, 131.53, 132.04, 132.42, 132.12, 133.29, 135.02,
    135.51, 135.34, 135.72, 136.7, 137.11, 136.53, 136.66, 136.93, 136.99, 139.79,
    138.96, 139.78, 139.34, 139.52, 139.0, 138.68, 139.14, 139.2, 138.99, 140.46,
    140.69, 139.99, 141.46, 139.84, 141.42, 140.92, 140.64, 140.88, 143.8, 144.12,
    143.93, 143.66, 143.7, 144.77, 144.02, 143.66, 143.34, 143.17, 141.63, 141.8,
    141.05, 141.83, 141.2, 140.68, 142.44, 142.27, 143.64, 144.53, 143.68, 143.79,
    143.65, 146.58, 147.51, 147.06, 146.53, 148.96, 153.01, 153.99, 153.26, 153.95,
    156.1, 155.7, 155.47, 150.25, 152.54, 153.06, 153.99, 153.8, 153.34, 153.87,
    153.61, 153.67, 152.76, 153.18
]

valoresGoogle = [
    808.01, 807.77, 813.02, 825.21, 827.18, 826.01, 829.86, 829.53, 830.94, 827.46,
    829.02, 824.37, 828.17, 844.43, 849.53, 858.45, 856.98, 845.03, 823.83, 820.19,
    815.24, 818.26, 820.13, 821.62, 829.23, 829.88, 830.06, 834.85, 838.96, 840.03,
    837.32, 842.17, 846.55, 849.27, 851.36, 851.0, 847.81, 849.67, 844.93, 856.75,
    849.85, 849.08, 847.27, 851.15, 853.64, 857.84, 861.4, 864.58, 865.91, 868.39,
    870.0, 872.37, 867.91, 850.14, 849.8, 839.65, 835.14, 838.51, 840.63, 849.87,
    849.48, 847.8, 856.75, 852.57, 848.91, 845.1, 842.1, 841.7, 839.88, 841.46,
    840.18, 855.13, 853.99, 856.51, 860.08, 858.95, 878.93, 888.84, 889.14, 891.44,
    924.52, 932.82, 937.09, 948.45, 954.72, 950.28, 958.69, 956.71, 954.84, 955.89,
    955.14, 959.22, 964.61, 942.17, 950.5, 954.65, 964.07, 970.55, 977.61, 991.86,
    993.27, 996.17, 987.09, 988.29
]

valoresBankOfAmerica = [
    22.53, 22.95, 22.68, 22.68, 22.55, 22.94, 23.07, 22.92, 23.01, 22.05, 22.63,
    22.53, 22.64, 22.56, 22.95, 23.37, 23.44, 23.36, 22.95, 22.64, 22.89, 22.72,
    23.29, 23.12, 22.9, 22.67, 23.12, 23.08, 23.4, 24.06, 24.58, 24.58, 24.52,
    24.78, 24.79, 24.58, 24.23, 24.57, 24.68, 25.5, 25.23, 25.44, 25.25, 25.21,
    25.26, 25.35, 25.31, 25.3, 25.32, 25.18, 25.22, 24.86, 24.44, 23.02, 22.94,
    23.07, 23.12, 23.03, 23.48, 23.35, 23.87, 23.59, 23.59, 23.44, 23.17, 23.26,
    23.16, 23.02, 22.92, 22.65, 22.34, 22.81, 22.71, 22.74, 23.07, 22.71, 23.63,
    23.98, 23.89, 23.65, 23.34, 23.61, 23.53, 23.77, 23.85, 23.74, 23.96, 23.98,
    24.15, 24.07, 24.0, 24.06, 23.99, 22.57, 22.74, 23.05, 23.04, 23.39, 23.36,
    23.25, 23.24, 22.91, 22.41, 22.63
]

# Calculando os valores mínimos e máximos
min_apple = min(valoresApple)
max_apple = max(valoresApple)
min_google = min(valoresGoogle)
max_google = max(valoresGoogle)
min_boa = min(valoresBankOfAmerica)
max_boa = max(valoresBankOfAmerica)

print(min_apple, min_boa)

# Plotando os gráficos
plt.figure(figsize=(12, 4))

# Gráfico Apple vs Google
plt.subplot(1, 3, 1)
plt.scatter(valoresApple, valoresGoogle)
plt.title('Apple vs Google')
plt.xlabel('Apple')
plt.ylabel('Google')
plt.xlim(min(min_apple, min_google), max(max_apple, max_google))
plt.ylim(min(min_apple, min_google), max(max_apple, max_google))

# Gráfico Apple vs Bank of America
plt.subplot(1, 3, 2)
plt.scatter(valoresApple, valoresBankOfAmerica)
plt.title('Apple vs Bank of America')
plt.xlabel('Apple')
plt.ylabel('Bank of America')
plt.xlim(110, 180)
plt.ylim(21,28)

# Gráfico Google vs Bank of America
plt.subplot(1, 3, 3)
plt.scatter(valoresGoogle, valoresBankOfAmerica)
plt.title('Google vs Bank of America')
plt.xlabel('Google')
plt.ylabel('Bank of America')
plt.xlim(min(min_google, min_boa), max(max_google, max_boa))
plt.ylim(min(min_google, min_boa), max(max_google, max_boa))

plt.tight_layout()
plt.show()


