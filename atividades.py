{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
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
       "      <th>userId</th>\n",
       "      <th>movieId</th>\n",
       "      <th>rating</th>\n",
       "      <th>timestamp</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964982703</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964981247</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964982224</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964983815</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>50</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964982931</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>1</td>\n",
       "      <td>70</td>\n",
       "      <td>3.0</td>\n",
       "      <td>964982400</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   userId  movieId  rating  timestamp\n",
       "0       1        1     4.0  964982703\n",
       "1       1        3     4.0  964981247\n",
       "2       1        6     4.0  964982224\n",
       "3       1       47     5.0  964983815\n",
       "4       1       50     5.0  964982931\n",
       "5       1       70     3.0  964982400"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notas = pd.read_csv(\"ratings.csv\")\n",
    "notas.head(6)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Dimensão da Base de dados "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(100836, 4)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notas.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Alterar nome do cabeçalho"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
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
       "      <th>usuarioId</th>\n",
       "      <th>filmeId</th>\n",
       "      <th>nota</th>\n",
       "      <th>momento</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964982703</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>3</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964981247</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>6</td>\n",
       "      <td>4.0</td>\n",
       "      <td>964982224</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>47</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964983815</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>50</td>\n",
       "      <td>5.0</td>\n",
       "      <td>964982931</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   usuarioId  filmeId  nota    momento\n",
       "0          1        1   4.0  964982703\n",
       "1          1        3   4.0  964981247\n",
       "2          1        6   4.0  964982224\n",
       "3          1       47   5.0  964983815\n",
       "4          1       50   5.0  964982931"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notas.columns = [\"usuarioId\", \"filmeId\", \"nota\", \"momento\"]\n",
    "notas.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Notas existentes em nossa Base"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([4. , 5. , 3. , 2. , 1. , 4.5, 3.5, 2.5, 0.5, 1.5])"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notas['nota'].unique()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Quantas notas tiveram o mesmo valor "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.0    26818\n",
       "3.0    20047\n",
       "5.0    13211\n",
       "3.5    13136\n",
       "4.5     8551\n",
       "2.0     7551\n",
       "2.5     5550\n",
       "1.0     2811\n",
       "1.5     1791\n",
       "0.5     1370\n",
       "Name: nota, dtype: int64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notas['nota'].value_counts()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Média das notas"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.501556983616962"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notas['nota'].mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Plotar os dados da coluna nota"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    4.0\n",
       "1    4.0\n",
       "2    4.0\n",
       "3    5.0\n",
       "4    5.0\n",
       "Name: nota, dtype: float64"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notas.nota.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Frequency'>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZEAAAD4CAYAAAAtrdtxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMiwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8qNh9FAAAACXBIWXMAAAsTAAALEwEAmpwYAAATHElEQVR4nO3df+xddX3H8edLfkxEGTg6xtqy4ta5dW5D/Aokus1phAKbxf1wmCmNI3aJJdHMZFazDKcjwWTqxubY6mwE56xs6OikjlVGZkwGtCDjp4QGy2hF2lkUmUaGe++P+/mOS/m23J5+7/d8L9/nI7n5nvO+58f73j/66jnnc89JVSFJUhfP6bsBSdLkMkQkSZ0ZIpKkzgwRSVJnhogkqbPD+25grh1//PG1bNmyvtuQpIlyyy23/FdVLdq3vuBCZNmyZWzbtq3vNiRpoiR5YKa6p7MkSZ0ZIpKkzgwRSVJnhogkqTNDRJLUmSEiSerMEJEkdWaISJI6M0QkSZ0tuF+sS5o/lq27tpf97rj03F72+2zkkYgkqTNDRJLUmSEiSerMEJEkdWaISJI6M0QkSZ0ZIpKkzgwRSVJnhogkqTNDRJLU2dhCJMnSJDckuTvJXUne3urvTbIryW3tdc7QOu9Osj3JvUnOGqqvbLXtSdYN1U9OclOrfzrJkeP6PJKkpxvnkcgTwDuragVwBrA2yYr23oer6pT22gzQ3jsf+BlgJfCXSQ5LchjwEeBsYAXwxqHtfKBt6yeAR4ALx/h5JEn7GFuIVNVDVXVrm/42cA+w+ACrrAI2VtX3quqrwHbgtPbaXlX3V9XjwEZgVZIArwb+oa1/BXDeWD6MJGlGc3JNJMky4KXATa10UZLbk2xIclyrLQYeHFptZ6vtr/5DwDer6ol96jPtf02SbUm27dmzZzY+kiSJOQiRJM8HrgbeUVWPApcDPw6cAjwEfHDcPVTV+qqaqqqpRYsWjXt3krRgjPV5IkmOYBAgn6yqzwBU1cND738U+Fyb3QUsHVp9Sauxn/o3gGOTHN6ORoaXlyTNgXGOzgrwMeCeqvrQUP3EocVeD9zZpjcB5yf5gSQnA8uBm4GtwPI2EutIBhffN1VVATcAv9HWXw1cM67PI0l6unEeibwCeDNwR5LbWu09DEZXnQIUsAP4XYCquivJVcDdDEZ2ra2q7wMkuQi4DjgM2FBVd7XtvQvYmOSPgS8zCC1J0hwZW4hU1ZeAzPDW5gOscwlwyQz1zTOtV1X3Mxi9JUnqgb9YlyR1ZohIkjozRCRJnRkikqTODBFJUmeGiCSpM0NEktSZISJJ6swQkSR1ZohIkjozRCRJnRkikqTODBFJUmeGiCSpM0NEktSZISJJ6swQkSR1ZohIkjozRCRJnRkikqTODBFJUmeGiCSpM0NEktSZISJJ6swQkSR1ZohIkjozRCRJnRkikqTODBFJUmdjC5EkS5PckOTuJHcleXurvzDJliT3tb/HtXqSXJZke5Lbk5w6tK3Vbfn7kqweqr8syR1tncuSZFyfR5L0dOM8EnkCeGdVrQDOANYmWQGsA66vquXA9W0e4GxgeXutAS6HQegAFwOnA6cBF08HT1vmrUPrrRzj55Ek7WNsIVJVD1XVrW3628A9wGJgFXBFW+wK4Lw2vQq4sgZuBI5NciJwFrClqvZW1SPAFmBle++Yqrqxqgq4cmhbkqQ5cPhc7CTJMuClwE3ACVX1UHvr68AJbXox8ODQajtb7UD1nTPUZ9r/GgZHN5x00kmH8Emk8Vm27tre9r3j0nN727cm29gvrCd5PnA18I6qenT4vXYEUePuoarWV9VUVU0tWrRo3LuTpAVjrCGS5AgGAfLJqvpMKz/cTkXR/u5u9V3A0qHVl7TagepLZqhLkubIOEdnBfgYcE9VfWjorU3A9Air1cA1Q/UL2iitM4BvtdNe1wFnJjmuXVA/E7iuvfdokjPavi4Y2pYkaQ6M85rIK4A3A3ckua3V3gNcClyV5ELgAeAN7b3NwDnAduA7wFsAqmpvkvcDW9ty76uqvW36bcDHgaOAz7eXJGmOjC1EqupLwP5+t/GaGZYvYO1+trUB2DBDfRvwkkNoU5J0CPzFuiSpM0NEktSZISJJ6swQkSR1ZohIkjozRCRJnRkikqTODBFJUmeGiCSpM0NEktSZISJJ6swQkSR1ZohIkjozRCRJnRkikqTODBFJUmeGiCSps5FCJMnPjrsRSdLkGfVI5C+T3JzkbUl+cKwdSZImxkghUlW/APw2sBS4JcnfJXntWDuTJM17I18Tqar7gD8A3gX8EnBZkq8k+bVxNSdJmt9GvSbyc0k+DNwDvBr41ar66Tb94TH2J0maxw4fcbk/B/4GeE9VfXe6WFVfS/IHY+lMkjTvjRoi5wLfrarvAyR5DvDcqvpOVX1ibN1Jkua1Ua+JfAE4amj+ea0mSVrARg2R51bVY9Mzbfp542lJkjQpRg2R/05y6vRMkpcB3z3A8pKkBWDUayLvAP4+ydeAAD8C/Na4mpIkTYaRQqSqtib5KeDFrXRvVf3P+NqSJE2CUY9EAF4OLGvrnJqEqrpyLF1JkibCqD82/ATwJ8ArGYTJy4GpZ1hnQ5LdSe4cqr03ya4kt7XXOUPvvTvJ9iT3JjlrqL6y1bYnWTdUPznJTa3+6SRHjvypJUmzYtQjkSlgRVXVQWz748BfAPserXy4qv5kuJBkBXA+8DPAjwJfSPKT7e2PAK8FdgJbk2yqqruBD7RtbUzyV8CFwOUH0Z8k6RCNOjrrTgYX00dWVV8E9o64+CpgY1V9r6q+CmwHTmuv7VV1f1U9DmwEViUJg1uu/ENb/wrgvIPpT5J06EY9EjkeuDvJzcD3potV9boO+7woyQXANuCdVfUIsBi4cWiZna0G8OA+9dOBHwK+WVVPzLD80yRZA6wBOOmkkzq0LEmayagh8t5Z2t/lwPuBan8/CPzOLG17v6pqPbAeYGpq6mBOyUmSDmDUIb7/luTHgOVV9YUkzwMOO9idVdXD09NJPgp8rs3uYvCskmlLWo391L8BHJvk8HY0Mry8JGmOjDo6660Mrj/8dSstBv7xYHeW5MSh2dczuNYCsAk4P8kPJDkZWA7cDGwFlreRWEcyuPi+qV3gvwH4jbb+auCag+1HknRoRj2dtZbBRe6bYPCAqiQ/fKAVknwKeBVwfJKdwMXAq5KcwuB01g7gd9v27kpyFXA38ASwduiOwRcB1zE48tlQVXe1XbwL2Jjkj4EvAx8b8bNIkmbJqCHyvap6fDAoCpIcziAI9quq3jhDeb//0FfVJcAlM9Q3A5tnqN/PINgkST0ZdYjvvyV5D3BUe7b63wP/NL62JEmTYNQQWQfsAe5gcApqM4PnrUuSFrBRR2f9L/DR9pIkCRgxRJJ8lRmugVTVi2a9I0nSxDiYe2dNey7wm8ALZ78dSdIkGemaSFV9Y+i1q6r+FDh3vK1Jkua7UU9nnTo0+xwGRyYH8ywSSdKz0KhB8MGh6ScY/FDwDbPejSRpoow6OuuXx92IpP4sW3dt3y0sGH191zsuHc8ViFFPZ/3egd6vqg/NTjuSpElyMKOzXs7gRokAv8rgBon3jaMpSdJkGDVElgCnVtW3YfCsdODaqnrTuBqTJM1/o9725ATg8aH5x1tNkrSAjXokciVwc5LPtvnzGDzXXJK0gI06OuuSJJ8HfqGV3lJVXx5fW5KkSTDq6SyA5wGPVtWfATvbEwglSQvYqI/HvZjBkwTf3UpHAH87rqYkSZNh1COR1wOvA/4boKq+BrxgXE1JkibDqCHyeFUV7XbwSY4eX0uSpEkxaohcleSvgWOTvBX4Aj6gSpIWvGccnZUkwKeBnwIeBV4M/GFVbRlzb5Kkee4ZQ6SqKsnmqvpZwOCQJP2/UU9n3Zrk5WPtRJI0cUb9xfrpwJuS7GAwQisMDlJ+blyNSZLmvwOGSJKTquo/gbPmqB9J0gR5piORf2Rw994HklxdVb8+Bz1JkibEM10TydD0i8bZiCRp8jxTiNR+piVJesbTWT+f5FEGRyRHtWl48sL6MWPtTpI0rx3wSKSqDquqY6rqBVV1eJuenj9ggCTZkGR3kjuHai9MsiXJfe3vca2eJJcl2Z7k9iSnDq2zui1/X5LVQ/WXJbmjrXNZ+1GkJGkOHcyt4A/Wx4GV+9TWAddX1XLg+jYPcDawvL3WAJfDIHSAixkMMT4NuHg6eNoybx1ab999SZLGbGwhUlVfBPbuU17Fk09EvILBExKn61fWwI0M7tF1IoOhxVuqam9VPcLgF/Mr23vHVNWN7caQVw5tS5I0R8Z5JDKTE6rqoTb9dZ58Tvti4MGh5Xa22oHqO2eoS5Lm0FyHyP8bvrX8uCVZk2Rbkm179uyZi11K0oIw1yHycDsVRfu7u9V3AUuHllvSageqL5mhPqOqWl9VU1U1tWjRokP+EJKkgbkOkU3A9Air1cA1Q/UL2iitM4BvtdNe1wFnJjmuXVA/E7iuvfdokjPaqKwLhrYlSZojo96A8aAl+RTwKuD4JDsZjLK6lMEDri4EHgDe0BbfDJwDbAe+A7wFoKr2Jnk/sLUt976qmr5Y/zYGI8COAj7fXpKkOTS2EKmqN+7nrdfMsGwBa/eznQ3Ahhnq24CXHEqPkqRD09uFdUnS5DNEJEmdGSKSpM4MEUlSZ4aIJKkzQ0SS1NnYhvhK0ny1bN21fbfwrOGRiCSpM0NEktSZISJJ6swQkSR1ZohIkjozRCRJnTnEV/NSn0Mwd1x6bm/7liaNRyKSpM4MEUlSZ4aIJKkzQ0SS1JkhIknqzBCRJHVmiEiSOjNEJEmdGSKSpM4MEUlSZ4aIJKkzQ0SS1JkhIknqzBCRJHVmiEiSOvN5ItI++nyWiTRpejkSSbIjyR1JbkuyrdVemGRLkvva3+NaPUkuS7I9ye1JTh3azuq2/H1JVvfxWSRpIevzdNYvV9UpVTXV5tcB11fVcuD6Ng9wNrC8vdYAl8MgdICLgdOB04CLp4NHkjQ35tM1kVXAFW36CuC8ofqVNXAjcGySE4GzgC1VtbeqHgG2ACvnuGdJWtD6CpEC/iXJLUnWtNoJVfVQm/46cEKbXgw8OLTuzlbbX/1pkqxJsi3Jtj179szWZ5CkBa+vC+uvrKpdSX4Y2JLkK8NvVlUlqdnaWVWtB9YDTE1Nzdp2JWmh6+VIpKp2tb+7gc8yuKbxcDtNRfu7uy2+C1g6tPqSVttfXZI0R+Y8RJIcneQF09PAmcCdwCZgeoTVauCaNr0JuKCN0joD+FY77XUdcGaS49oF9TNbTZI0R/o4nXUC8Nkk0/v/u6r65yRbgauSXAg8ALyhLb8ZOAfYDnwHeAtAVe1N8n5ga1vufVW1d+4+hiRpzkOkqu4Hfn6G+jeA18xQL2Dtfra1Adgw2z1KkkYzn4b4SpImjCEiSerMEJEkdWaISJI6M0QkSZ0ZIpKkzgwRSVJnhogkqTNDRJLUmSEiSerMEJEkddbX80R0EJatu7a3fe+49Nze9i1p/vNIRJLUmSEiSerMEJEkdWaISJI6M0QkSZ0ZIpKkzgwRSVJn/k5EB9Tnb1QkzX8eiUiSOjNEJEmdeTrrIHhqR5KeyiMRSVJnhogkqTNDRJLUmSEiSerMEJEkdWaISJI6M0QkSZ1NfIgkWZnk3iTbk6zrux9JWkgmOkSSHAZ8BDgbWAG8McmKfruSpIVjokMEOA3YXlX3V9XjwEZgVc89SdKCMem3PVkMPDg0vxM4fd+FkqwB1rTZx5LcOwe9jdPxwH/13cQ84XfxVH4fT+X30eQDh/xd/NhMxUkPkZFU1Xpgfd99zJYk26pqqu8+5gO/i6fy+3gqv48njeu7mPTTWbuApUPzS1pNkjQHJj1EtgLLk5yc5EjgfGBTzz1J0oIx0aezquqJJBcB1wGHARuq6q6e25oLz5pTc7PA7+Kp/D6eyu/jSWP5LlJV49iuJGkBmPTTWZKkHhkikqTODJEJkmRDkt1J7uy7l74lWZrkhiR3J7krydv77qlPSZ6b5OYk/9G+jz/qu6e+JTksyZeTfK7vXvqWZEeSO5LclmTbrG7bayKTI8kvAo8BV1bVS/rup09JTgROrKpbk7wAuAU4r6ru7rm1XiQJcHRVPZbkCOBLwNur6saeW+tNkt8DpoBjqupX+u6nT0l2AFNVNes/vPRIZIJU1ReBvX33MR9U1UNVdWub/jZwD4M7GCxINfBYmz2ivRbs/xCTLAHOBf6m716e7QwRTbwky4CXAjf13Eqv2umb24DdwJaqWsjfx58Cvw/8b899zBcF/EuSW9ptoGaNIaKJluT5wNXAO6rq0b776VNVfb+qTmFw54bTkizIU55JfgXYXVW39N3LPPLKqjqVwR3P17ZT47PCENHEauf+rwY+WVWf6buf+aKqvgncAKzsuZW+vAJ4XbsOsBF4dZK/7belflXVrvZ3N/BZBndAnxWGiCZSu5D8MeCeqvpQ3/30LcmiJMe26aOA1wJf6bWpnlTVu6tqSVUtY3ArpH+tqjf13FZvkhzdBp+Q5GjgTGDWRngaIhMkyaeAfwdenGRnkgv77qlHrwDezOB/mbe11zl9N9WjE4EbktzO4J5yW6pqwQ9tFQAnAF9K8h/AzcC1VfXPs7Vxh/hKkjrzSESS1JkhIknqzBCRJHVmiEiSOjNEJEmdGSKSpM4MEUlSZ/8HybJTTQ5x0rYAAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "notas.nota.plot(kind='hist')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Descrevendo os Dados"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "count    100836.000000\n",
       "mean          3.501557\n",
       "std           1.042529\n",
       "min           0.500000\n",
       "25%           3.000000\n",
       "50%           3.500000\n",
       "75%           4.000000\n",
       "max           5.000000\n",
       "Name: nota, dtype: float64"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notas.nota.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Plotando Notas usando Boxplot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\seiff\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\seaborn\\_decorators.py:36: FutureWarning: Pass the following variable as a keyword arg: x. From version 0.12, the only valid positional argument will be `data`, and passing other arguments without an explicit keyword will result in an error or misinterpretation.\n",
      "  warnings.warn(\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='nota'>"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot(notas.nota)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Trabalhando com a base de filmes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
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
       "      <th>filmeId</th>\n",
       "      <th>titulo</th>\n",
       "      <th>generos</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Toy Story (1995)</td>\n",
       "      <td>Adventure|Animation|Children|Comedy|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Jumanji (1995)</td>\n",
       "      <td>Adventure|Children|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Grumpier Old Men (1995)</td>\n",
       "      <td>Comedy|Romance</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Waiting to Exhale (1995)</td>\n",
       "      <td>Comedy|Drama|Romance</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Father of the Bride Part II (1995)</td>\n",
       "      <td>Comedy</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   filmeId                              titulo  \\\n",
       "0        1                    Toy Story (1995)   \n",
       "1        2                      Jumanji (1995)   \n",
       "2        3             Grumpier Old Men (1995)   \n",
       "3        4            Waiting to Exhale (1995)   \n",
       "4        5  Father of the Bride Part II (1995)   \n",
       "\n",
       "                                       generos  \n",
       "0  Adventure|Animation|Children|Comedy|Fantasy  \n",
       "1                   Adventure|Children|Fantasy  \n",
       "2                               Comedy|Romance  \n",
       "3                         Comedy|Drama|Romance  \n",
       "4                                       Comedy  "
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "filmes = pd.read_csv(\"movies.csv\")\n",
    "filmes.columns= ['filmeId', 'titulo', 'generos']\n",
    "filmes.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Manipulando a base filmes\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Média das notas do filmeId 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3.9209302325581397"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notas.query(\"filmeId == 1\").nota.mean()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Média das Notas dos filmes "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "filmeId\n",
       "1    3.920930\n",
       "2    3.431818\n",
       "3    3.259615\n",
       "4    2.357143\n",
       "5    3.071429\n",
       "Name: nota, dtype: float64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "medias_por_filmes = notas.groupby(\"filmeId\").mean()['nota']\n",
    "medias_por_filmes.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Montando Gráficos "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:ylabel='Frequency'>"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "medias_por_filmes.plot(kind='hist')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:title={'center':'Titulo'}, ylabel='nota'>"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 360x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(5,8))\n",
    "plt.title('Titulo')\n",
    "sns.boxplot(y=medias_por_filmes)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "c:\\Users\\seiff\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\seaborn\\distributions.py:2619: FutureWarning: `distplot` is a deprecated function and will be removed in a future version. Please adapt your code to use either `displot` (a figure-level function with similar flexibility) or `histplot` (an axes-level function for histograms).\n",
      "  warnings.warn(msg, FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='nota', ylabel='Density'>"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.distplot(medias_por_filmes)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Usando outra base - tmdb_5000"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
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
       "      <th>budget</th>\n",
       "      <th>genres</th>\n",
       "      <th>homepage</th>\n",
       "      <th>id</th>\n",
       "      <th>keywords</th>\n",
       "      <th>original_language</th>\n",
       "      <th>original_title</th>\n",
       "      <th>overview</th>\n",
       "      <th>popularity</th>\n",
       "      <th>production_companies</th>\n",
       "      <th>production_countries</th>\n",
       "      <th>release_date</th>\n",
       "      <th>revenue</th>\n",
       "      <th>runtime</th>\n",
       "      <th>spoken_languages</th>\n",
       "      <th>status</th>\n",
       "      <th>tagline</th>\n",
       "      <th>title</th>\n",
       "      <th>vote_average</th>\n",
       "      <th>vote_count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>237000000</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>http://www.avatarmovie.com/</td>\n",
       "      <td>19995</td>\n",
       "      <td>[{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...</td>\n",
       "      <td>en</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>In the 22nd century, a paraplegic Marine is di...</td>\n",
       "      <td>150.437577</td>\n",
       "      <td>[{\"name\": \"Ingenious Film Partners\", \"id\": 289...</td>\n",
       "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
       "      <td>2009-12-10</td>\n",
       "      <td>2787965087</td>\n",
       "      <td>162.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...</td>\n",
       "      <td>Released</td>\n",
       "      <td>Enter the World of Pandora.</td>\n",
       "      <td>Avatar</td>\n",
       "      <td>7.2</td>\n",
       "      <td>11800</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>300000000</td>\n",
       "      <td>[{\"id\": 12, \"name\": \"Adventure\"}, {\"id\": 14, \"...</td>\n",
       "      <td>http://disney.go.com/disneypictures/pirates/</td>\n",
       "      <td>285</td>\n",
       "      <td>[{\"id\": 270, \"name\": \"ocean\"}, {\"id\": 726, \"na...</td>\n",
       "      <td>en</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>Captain Barbossa, long believed to be dead, ha...</td>\n",
       "      <td>139.082615</td>\n",
       "      <td>[{\"name\": \"Walt Disney Pictures\", \"id\": 2}, {\"...</td>\n",
       "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
       "      <td>2007-05-19</td>\n",
       "      <td>961000000</td>\n",
       "      <td>169.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>At the end of the world, the adventure begins.</td>\n",
       "      <td>Pirates of the Caribbean: At World's End</td>\n",
       "      <td>6.9</td>\n",
       "      <td>4500</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>245000000</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>http://www.sonypictures.com/movies/spectre/</td>\n",
       "      <td>206647</td>\n",
       "      <td>[{\"id\": 470, \"name\": \"spy\"}, {\"id\": 818, \"name...</td>\n",
       "      <td>en</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>A cryptic message from Bond’s past sends him o...</td>\n",
       "      <td>107.376788</td>\n",
       "      <td>[{\"name\": \"Columbia Pictures\", \"id\": 5}, {\"nam...</td>\n",
       "      <td>[{\"iso_3166_1\": \"GB\", \"name\": \"United Kingdom\"...</td>\n",
       "      <td>2015-10-26</td>\n",
       "      <td>880674609</td>\n",
       "      <td>148.0</td>\n",
       "      <td>[{\"iso_639_1\": \"fr\", \"name\": \"Fran\\u00e7ais\"},...</td>\n",
       "      <td>Released</td>\n",
       "      <td>A Plan No One Escapes</td>\n",
       "      <td>Spectre</td>\n",
       "      <td>6.3</td>\n",
       "      <td>4466</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>250000000</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 80, \"nam...</td>\n",
       "      <td>http://www.thedarkknightrises.com/</td>\n",
       "      <td>49026</td>\n",
       "      <td>[{\"id\": 849, \"name\": \"dc comics\"}, {\"id\": 853,...</td>\n",
       "      <td>en</td>\n",
       "      <td>The Dark Knight Rises</td>\n",
       "      <td>Following the death of District Attorney Harve...</td>\n",
       "      <td>112.312950</td>\n",
       "      <td>[{\"name\": \"Legendary Pictures\", \"id\": 923}, {\"...</td>\n",
       "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
       "      <td>2012-07-16</td>\n",
       "      <td>1084939099</td>\n",
       "      <td>165.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>The Legend Ends</td>\n",
       "      <td>The Dark Knight Rises</td>\n",
       "      <td>7.6</td>\n",
       "      <td>9106</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>260000000</td>\n",
       "      <td>[{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...</td>\n",
       "      <td>http://movies.disney.com/john-carter</td>\n",
       "      <td>49529</td>\n",
       "      <td>[{\"id\": 818, \"name\": \"based on novel\"}, {\"id\":...</td>\n",
       "      <td>en</td>\n",
       "      <td>John Carter</td>\n",
       "      <td>John Carter is a war-weary, former military ca...</td>\n",
       "      <td>43.926995</td>\n",
       "      <td>[{\"name\": \"Walt Disney Pictures\", \"id\": 2}]</td>\n",
       "      <td>[{\"iso_3166_1\": \"US\", \"name\": \"United States o...</td>\n",
       "      <td>2012-03-07</td>\n",
       "      <td>284139100</td>\n",
       "      <td>132.0</td>\n",
       "      <td>[{\"iso_639_1\": \"en\", \"name\": \"English\"}]</td>\n",
       "      <td>Released</td>\n",
       "      <td>Lost in our world, found in another.</td>\n",
       "      <td>John Carter</td>\n",
       "      <td>6.1</td>\n",
       "      <td>2124</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      budget                                             genres  \\\n",
       "0  237000000  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "1  300000000  [{\"id\": 12, \"name\": \"Adventure\"}, {\"id\": 14, \"...   \n",
       "2  245000000  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "3  250000000  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 80, \"nam...   \n",
       "4  260000000  [{\"id\": 28, \"name\": \"Action\"}, {\"id\": 12, \"nam...   \n",
       "\n",
       "                                       homepage      id  \\\n",
       "0                   http://www.avatarmovie.com/   19995   \n",
       "1  http://disney.go.com/disneypictures/pirates/     285   \n",
       "2   http://www.sonypictures.com/movies/spectre/  206647   \n",
       "3            http://www.thedarkknightrises.com/   49026   \n",
       "4          http://movies.disney.com/john-carter   49529   \n",
       "\n",
       "                                            keywords original_language  \\\n",
       "0  [{\"id\": 1463, \"name\": \"culture clash\"}, {\"id\":...                en   \n",
       "1  [{\"id\": 270, \"name\": \"ocean\"}, {\"id\": 726, \"na...                en   \n",
       "2  [{\"id\": 470, \"name\": \"spy\"}, {\"id\": 818, \"name...                en   \n",
       "3  [{\"id\": 849, \"name\": \"dc comics\"}, {\"id\": 853,...                en   \n",
       "4  [{\"id\": 818, \"name\": \"based on novel\"}, {\"id\":...                en   \n",
       "\n",
       "                             original_title  \\\n",
       "0                                    Avatar   \n",
       "1  Pirates of the Caribbean: At World's End   \n",
       "2                                   Spectre   \n",
       "3                     The Dark Knight Rises   \n",
       "4                               John Carter   \n",
       "\n",
       "                                            overview  popularity  \\\n",
       "0  In the 22nd century, a paraplegic Marine is di...  150.437577   \n",
       "1  Captain Barbossa, long believed to be dead, ha...  139.082615   \n",
       "2  A cryptic message from Bond’s past sends him o...  107.376788   \n",
       "3  Following the death of District Attorney Harve...  112.312950   \n",
       "4  John Carter is a war-weary, former military ca...   43.926995   \n",
       "\n",
       "                                production_companies  \\\n",
       "0  [{\"name\": \"Ingenious Film Partners\", \"id\": 289...   \n",
       "1  [{\"name\": \"Walt Disney Pictures\", \"id\": 2}, {\"...   \n",
       "2  [{\"name\": \"Columbia Pictures\", \"id\": 5}, {\"nam...   \n",
       "3  [{\"name\": \"Legendary Pictures\", \"id\": 923}, {\"...   \n",
       "4        [{\"name\": \"Walt Disney Pictures\", \"id\": 2}]   \n",
       "\n",
       "                                production_countries release_date     revenue  \\\n",
       "0  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   2009-12-10  2787965087   \n",
       "1  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   2007-05-19   961000000   \n",
       "2  [{\"iso_3166_1\": \"GB\", \"name\": \"United Kingdom\"...   2015-10-26   880674609   \n",
       "3  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   2012-07-16  1084939099   \n",
       "4  [{\"iso_3166_1\": \"US\", \"name\": \"United States o...   2012-03-07   284139100   \n",
       "\n",
       "   runtime                                   spoken_languages    status  \\\n",
       "0    162.0  [{\"iso_639_1\": \"en\", \"name\": \"English\"}, {\"iso...  Released   \n",
       "1    169.0           [{\"iso_639_1\": \"en\", \"name\": \"English\"}]  Released   \n",
       "2    148.0  [{\"iso_639_1\": \"fr\", \"name\": \"Fran\\u00e7ais\"},...  Released   \n",
       "3    165.0           [{\"iso_639_1\": \"en\", \"name\": \"English\"}]  Released   \n",
       "4    132.0           [{\"iso_639_1\": \"en\", \"name\": \"English\"}]  Released   \n",
       "\n",
       "                                          tagline  \\\n",
       "0                     Enter the World of Pandora.   \n",
       "1  At the end of the world, the adventure begins.   \n",
       "2                           A Plan No One Escapes   \n",
       "3                                 The Legend Ends   \n",
       "4            Lost in our world, found in another.   \n",
       "\n",
       "                                      title  vote_average  vote_count  \n",
       "0                                    Avatar           7.2       11800  \n",
       "1  Pirates of the Caribbean: At World's End           6.9        4500  \n",
       "2                                   Spectre           6.3        4466  \n",
       "3                     The Dark Knight Rises           7.6        9106  \n",
       "4                               John Carter           6.1        2124  "
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tmdb = pd.read_csv('tmdb_5000_movies.csv')\n",
    "tmdb.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['en', 'ja', 'fr', 'zh', 'es', 'de', 'hi', 'ru', 'ko', 'te', 'cn',\n",
       "       'it', 'nl', 'ta', 'sv', 'th', 'da', 'xx', 'hu', 'cs', 'pt', 'is',\n",
       "       'tr', 'nb', 'af', 'pl', 'he', 'ar', 'vi', 'ky', 'id', 'ro', 'fa',\n",
       "       'no', 'sl', 'ps', 'el'], dtype=object)"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "tmdb.original_language.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
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
       "      <th>original_ling</th>\n",
       "      <th>Qts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>en</td>\n",
       "      <td>4505</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>fr</td>\n",
       "      <td>70</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>es</td>\n",
       "      <td>32</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>zh</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>de</td>\n",
       "      <td>27</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  original_ling   Qts\n",
       "0            en  4505\n",
       "1            fr    70\n",
       "2            es    32\n",
       "3            zh    27\n",
       "4            de    27"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "contagem_de_linguas = tmdb['original_language'].value_counts().to_frame().reset_index()\n",
    "contagem_de_linguas.columns = ['original_ling', 'Qts']\n",
    "contagem_de_linguas.head()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Plotando Graficos"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='original_ling', ylabel='Qts'>"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x = 'original_ling' , y = 'Qts', data = contagem_de_linguas)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x1ec6f657b80>"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 360x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.catplot(x = 'original_language', kind='count', data = tmdb)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "4505 298\n"
     ]
    }
   ],
   "source": [
    "total_por_lingua = tmdb['original_language'].value_counts()\n",
    "total_geral = total_por_lingua.sum()\n",
    "total_de_ingles = total_por_lingua.loc['en']\n",
    "total_do_resto = total_geral - total_de_ingles\n",
    "print(total_de_ingles, total_do_resto )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Criando DateFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "dados = {\n",
    "    'lingua' : ['ingles', 'outros'],\n",
    "    'total' : [total_de_ingles, total_do_resto]\n",
    "}\n",
    "dados = pd.DataFrame(dados)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='lingua', ylabel='total'>"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.barplot(x = 'lingua', y = 'total', data = dados)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [],
   "source": [
    "filmes_sem_lingua_original_em_ingles = tmdb.query(\"original_language != 'en'\")\n",
    "total_por_lingua_de_outros_filmes = filmes_sem_lingua_original_em_ingles.original_language.value_counts()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<seaborn.axisgrid.FacetGrid at 0x1ec6f169780>"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x360 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "sns.catplot(x = 'original_language', kind='count',\n",
    "             data = filmes_sem_lingua_original_em_ingles,\n",
    "             palette= \"GnBu_d\",\n",
    "             aspect=2, order=total_por_lingua_de_outros_filmes.index )"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Análise de Média, Mediana, Desvio Padrão em alguns filmes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
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
       "      <th>filmeId</th>\n",
       "      <th>titulo</th>\n",
       "      <th>generos</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Toy Story (1995)</td>\n",
       "      <td>Adventure|Animation|Children|Comedy|Fantasy</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Jumanji (1995)</td>\n",
       "      <td>Adventure|Children|Fantasy</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   filmeId            titulo                                      generos\n",
       "0        1  Toy Story (1995)  Adventure|Animation|Children|Comedy|Fantasy\n",
       "1        2    Jumanji (1995)                   Adventure|Children|Fantasy"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "filmes.head(2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "215 110\n"
     ]
    }
   ],
   "source": [
    "notas_do_toy_story = notas.query(\"filmeId == 1\")\n",
    "notas_do_jumanji = notas.query(\"filmeId == 2\")\n",
    "print(len(notas_do_toy_story),len(notas_do_jumanji))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Cálculo de Média"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Média de notas do Toy Story 3.92\n",
      "Média de notas do Jumanji 3.43\n"
     ]
    }
   ],
   "source": [
    "print(\"Média de notas do Toy Story %.2f\" % notas_do_toy_story.nota.mean())\n",
    "print(\"Média de notas do Jumanji %.2f\" % notas_do_jumanji.nota.mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Cálculo de Mediana"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Mediana de notas do Toy Story 4.00\n",
      "Mediana de notas do Jumanji 3.50\n"
     ]
    }
   ],
   "source": [
    "print(\"Mediana de notas do Toy Story %.2f\" % notas_do_toy_story.nota.median())\n",
    "print(\"Mediana de notas do Jumanji %.2f\" % notas_do_jumanji.nota.median())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# BoxPlot das notas\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'whiskers': [<matplotlib.lines.Line2D at 0x1ec6f94a860>,\n",
       "  <matplotlib.lines.Line2D at 0x1ec6f94ab30>,\n",
       "  <matplotlib.lines.Line2D at 0x1ec6f94bc10>,\n",
       "  <matplotlib.lines.Line2D at 0x1ec6f94bee0>],\n",
       " 'caps': [<matplotlib.lines.Line2D at 0x1ec6f94ae00>,\n",
       "  <matplotlib.lines.Line2D at 0x1ec6f94b0d0>,\n",
       "  <matplotlib.lines.Line2D at 0x1ec6f97c1f0>,\n",
       "  <matplotlib.lines.Line2D at 0x1ec6f97c4c0>],\n",
       " 'boxes': [<matplotlib.lines.Line2D at 0x1ec6f94a590>,\n",
       "  <matplotlib.lines.Line2D at 0x1ec6f94b940>],\n",
       " 'medians': [<matplotlib.lines.Line2D at 0x1ec6f94b3a0>,\n",
       "  <matplotlib.lines.Line2D at 0x1ec6f97c790>],\n",
       " 'fliers': [<matplotlib.lines.Line2D at 0x1ec6f94b670>,\n",
       "  <matplotlib.lines.Line2D at 0x1ec6f97ca60>],\n",
       " 'means': []}"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.boxplot([notas_do_toy_story.nota, notas_do_jumanji.nota])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='filmeId', ylabel='nota'>"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "sns.boxplot (x = \"filmeId\" , y = \"nota\", data = notas.query(\"filmeId in [1,2,3,4,5]\"))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Desvio Padrão"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.8817134921476455"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "notas_do_jumanji.nota.std()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.10.2 64-bit",
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
   "version": "3.10.2"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "2869b0a8da65935b51a16db953b63f967ece7a54cd2a4817b7c1e4f17895eae4"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
