# -*- encoding: UTF-8 -*-
import numpy as np
from scipy.stats import skew, kurtosis

# Seus arrays
arrays = [
    np.array([[0.15920848, 0.01877106, 0.15091988, 0.02978689, 0.2916951 , 0.27763632, 0.07198224]], dtype=np.float32),
    np.array([[0.1443957 , 0.0720441 , 0.10651037, 0.3683149 , 0.11398377, 0.1657229 , 0.02902822]], dtype=np.float32),
    np.array([[0.13053113, 0.06142964, 0.12200181, 0.38826537, 0.09863172, 0.17504877, 0.02409145]], dtype=np.float32)
]

test = np.array([0.15920848,0.1443957,0.13053113])

# Concatenando os arrays em um único array
combined_array = np.concatenate(arrays, axis=0)


# Calculando a média de cada coluna
means = np.mean(combined_array, axis=0)



# # Calculando a obliquidade (skewness) de cada coluna
skews = skew(combined_array, axis=0)

# # Calculando a curtose (kurtosis) de cada coluna
# kurtoses = kurtosis(combined_array, axis=0)

# # Imprimindo os resultados
# for col, (mean, skewness, kurt) in enumerate(zip(means, skews, kurtoses)):
#     print(f"Coluna {col+1}:")
#     print(f"Média: {mean}")
#     print(f"Obliquidade: {skewness}")
#     print(f"Curtose: {kurt}\n")
