{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "daaeb655-4b74-4536-a6e5-067f235ba20d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#importação das bibliotecas\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "from math import ceil"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "40a5539f-bf99-4ab7-9e9d-4637679bd5d6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#criação das variáveis para representar a população, a amostra e o valor de k\n",
    "população = 150\n",
    "amostra = 15\n",
    "k = ceil(amostra/população)\n",
    "print(k)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "889ec42f-e002-43e0-b7ad-f5ccdee3a370",
   "metadata": {},
   "outputs": [],
   "source": [
    "r = np.random.randint(low = 1, high = k + 1, size = 1)\n",
    "print(r)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0982b3df-8b5f-4407-a1ae-db09446aa2a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "#criamos um for para somar os próximos valores, baseado no primeiro valor r que foi definido acima.\n",
    "acumulador = r[0]\n",
    "sorteados = []\n",
    "for i in range(amostra):\n",
    "    #print(acumulador)\n",
    "    sorteados.append(acumulador)\n",
    "    acumulador += k\n",
    "print(sorteados)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1503e5fe-07e1-4ca9-8fdd-86aef3837a07",
   "metadata": {},
   "outputs": [],
   "source": [
    "len(sorteados)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec65b623-364e-45c5-be9e-39a05d9c3046",
   "metadata": {},
   "outputs": [],
   "source": [
    "#carregamos a base de dados e criamos a base_final somente com os valores sorteados\n",
    "base = pd.read_csv('iris.csv')\n",
    "base_final = base.loc[sorteados]\n",
    "base_final"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a480db0b-a8d8-4460-8d95-f6c986ff66bd",
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
