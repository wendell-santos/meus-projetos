{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "285294e7-d68b-4674-8b80-57bc2a2e624d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#amostragem simples"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "ae84cec1-7a4a-47d8-b58f-6b222616e1bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "#importação das bibliotecas: pandas para carregar os arquivos .csv e numpy para gerar números aleatórios\n",
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "72523291-4953-4aac-8ef6-b1b306bbdf3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>sepal length</th>\n",
       "      <th>sepal width</th>\n",
       "      <th>petal length</th>\n",
       "      <th>petal width</th>\n",
       "      <th>class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>5.1</td>\n",
       "      <td>3.5</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>4.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>4.7</td>\n",
       "      <td>3.2</td>\n",
       "      <td>1.3</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4.6</td>\n",
       "      <td>3.1</td>\n",
       "      <td>1.5</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5.0</td>\n",
       "      <td>3.6</td>\n",
       "      <td>1.4</td>\n",
       "      <td>0.2</td>\n",
       "      <td>Iris-setosa</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>145</th>\n",
       "      <td>6.7</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.2</td>\n",
       "      <td>2.3</td>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>146</th>\n",
       "      <td>6.3</td>\n",
       "      <td>2.5</td>\n",
       "      <td>5.0</td>\n",
       "      <td>1.9</td>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>147</th>\n",
       "      <td>6.5</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.2</td>\n",
       "      <td>2.0</td>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>148</th>\n",
       "      <td>6.2</td>\n",
       "      <td>3.4</td>\n",
       "      <td>5.4</td>\n",
       "      <td>2.3</td>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>149</th>\n",
       "      <td>5.9</td>\n",
       "      <td>3.0</td>\n",
       "      <td>5.1</td>\n",
       "      <td>1.8</td>\n",
       "      <td>Iris-virginica</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>150 rows × 5 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     sepal length  sepal width  petal length  petal width           class\n",
       "0             5.1          3.5           1.4          0.2     Iris-setosa\n",
       "1             4.9          3.0           1.4          0.2     Iris-setosa\n",
       "2             4.7          3.2           1.3          0.2     Iris-setosa\n",
       "3             4.6          3.1           1.5          0.2     Iris-setosa\n",
       "4             5.0          3.6           1.4          0.2     Iris-setosa\n",
       "..            ...          ...           ...          ...             ...\n",
       "145           6.7          3.0           5.2          2.3  Iris-virginica\n",
       "146           6.3          2.5           5.0          1.9  Iris-virginica\n",
       "147           6.5          3.0           5.2          2.0  Iris-virginica\n",
       "148           6.2          3.4           5.4          2.3  Iris-virginica\n",
       "149           5.9          3.0           5.1          1.8  Iris-virginica\n",
       "\n",
       "[150 rows x 5 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#carregamento da base de dados (o arquivo .csv precisa estar na mesma pasta do código fonte) e visualização dos dados\n",
    "base = pd.read_csv('iris.csv')\n",
    "base"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "9bb1eb8a-1590-4e37-8512-3bf24c6ce6b5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(150, 5)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#verificar quantas linhas e colunas existem na base de dados\n",
    "base.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "7fab4ee1-b2d2-4873-a78b-b74748890fed",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "101"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#mudança da semente aleatória randômica para manter os resultados em várias execuções\n",
    "np.random.seed(2345)\n",
    "#150 amostras, de 0 a 1, com reposição, probabilidades equivalentes\n",
    "amostra = np.random.choice(a = [0, 1], size = 150, replace = True, p = [0.7, 0.3])\n",
    "#verificar tamanho da amostra\n",
    "len(amostra)\n",
    "#verificar tamanho da amostra para valores igual a 1 e 0\n",
    "len(amostra[amostra == 1])\n",
    "len(amostra[amostra == 0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "ea4f1a59-1ee4-4911-b963-f971da7c51c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(101, 5)"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "base_final = base.loc[amostra == 0]\n",
    "base_final.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a58b9a3-e3a3-4316-86dc-1e8a8bb85857",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
