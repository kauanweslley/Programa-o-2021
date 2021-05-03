{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "exerciciosII.ipynb",
      "provenance": [],
      "collapsed_sections": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "2mNhvN2Oe9t1"
      },
      "source": [
        "Lista de Exercicios II - Estrutura de Decisão\n"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "v53IchVuiyeo"
      },
      "source": [
        "lado1 = int(input(\"informe o lado 1 do triangulo: \"))\n",
        "lado2 = int(input(\"informe o lado 2 do triangulo: \"))\n",
        "lado3 = int(input(\"informe o lado 3 do triangulo: \"))\n",
        "\n",
        "if lado1+lado2 <= lado3:\n",
        "  print (\"Não pode ser um triangulo\")\n",
        "  print (\"\\nFIM\\n\")\n",
        "elif lado1 != lado2:\n",
        "  print (\"Pode ser um triangulo\")\n",
        "  print (\"É um triangulo escaleno\")\n",
        "  print (\"\\nFIM\\n\")\n",
        "elif lado1 == lado2:\n",
        "  print (\"Pode ser um triangulo\")\n",
        "  print (\"É um triangulo isóceles\")\n",
        "  print (\"\\nFIM\\n\")\n",
        "else:\n",
        "  print (\"Pode ser um triangulo\")\n",
        "  print (\"É um triangulo equilátero\")\n",
        "  print (\"\\nFIM\\n\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "mFkfQRlOqAzz"
      },
      "source": [
        "ano = int(input(\"Digite quantos dias tem seu ano: \"))\n",
        "\n",
        "if ano > 365:\n",
        "  print(\"É um ano bissexto!\")\n",
        "else:\n",
        "  print(\"Não é um ano bissexto!\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "E1gzm0Wvq1Ps"
      },
      "source": [
        "peixes = int(input(\"Digite o peso dos peixes: \"))\n",
        "multa = 4\n",
        "if peixes > 50: \n",
        "  excesso = peixes - 50\n",
        "  valor_multa = excesso * multa\n",
        "  print(\"Quantidade que tem de excesso\", excesso)\n",
        "  print(\"João deve pagar um valor de R$\", valor_multa)\n",
        "else:\n",
        "  print(\"João não precisa pagar multa\")"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "Ke1vVJBvt2TK"
      },
      "source": [
        "v1 = int(input(\"informe o valor de v1: \"))\n",
        "v2 = int(input(\"informe o valor de v2: \"))\n",
        "v3 = int(input(\"informe o valor de v3: \"))\n",
        "\n",
        "if v1 > v2 and v1 > v3:\n",
        "  print(\"o maior valor é\", v1)\n",
        "elif v2 > v3:\n",
        "  print(\"o maior valor é\", v2)\n",
        "else:\n",
        "  print(\"o maior valor é\", v3)"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "SWVMtl2Dv0MP"
      },
      "source": [
        "v1 = int(input(\"informe o valor de v1: \"))\n",
        "v2 = int(input(\"informe o valor de v2: \"))\n",
        "v3 = int(input(\"informe o valor de v3: \"))\n",
        "\n",
        "if v1 > v2 and v1 > v3:\n",
        "  print(\"o maior valor é\", v1)\n",
        "elif v2 > v3:\n",
        "  print(\"o maior valor é\", v2)\n",
        "else:\n",
        "  print(\"o maior valor é\", v3)\n",
        "\n",
        "if v1 < v2 and v1 < v3:\n",
        "  print(\"o menor valor é\", v1)\n",
        "elif v2 < v3:\n",
        "  print(\"o menor valor é\", v2)\n",
        "else:\n",
        "  print(\"o menor valor é\", v3)\n"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "uNMPBzLOGR9r"
      },
      "source": [
        "ganho_hora = int(input(\"Digite o valor que você recebe por hora: \"))\n",
        "hora_mes = int(input(\"Digite as horas que você trabalha por mês: \"))\n",
        "salario_bruto = ganho_hora*hora_mes\n",
        "print(\"Esse é o seu sálario por mês: \", salario_bruto)\n",
        "IR = salario_bruto * 11 / 100\n",
        "INSS = salario_bruto * 8 / 100\n",
        "SIND = salario_bruto * 5 / 100\n",
        "salario_liquido = salario_bruto - IR - INSS - SIND\n",
        "print(\"Esse é o seu sálario por mês com desconto: \", salario_liquido) "
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Bg4VuXf9JyXO",
        "outputId": "c15541dc-8061-4917-cc74-446a8260b359"
      },
      "source": [
        "m2 = int(input(\"Informe o tamanho do m2 da área a ser pintada: \"))\n",
        "cobertura = 1 * m2 / 3\n",
        "if cobertura <= 18:\n",
        "  print(\"Você deve comprar 1 lata de tinta\")\n",
        "  print(\"O preço total é de R$80\")\n",
        "else: \n",
        "  latas = cobertura // 18\n",
        "  print(\"Total de latas que voce deve comprar: \", latas )\n",
        "  preco_total = latas * 80\n",
        "  print(\"O preço total é de R$\", preco_total)\n",
        "\n"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "Informe o tamanho do m2 da área a ser pintada: 162\n",
            "Total de latas que voce deve comprar:  3.0\n",
            "O preço total é de R$ 240.0\n"
          ],
          "name": "stdout"
        }
      ]
    }
  ]
}