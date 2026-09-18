import operaciones

OPERACIONES = {
    "**": lambda x, y: x ** y,
    "$" : lambda x, y: operaciones.raiz_enesima(x, y),
    "//": lambda x, y: operaciones.division_entera(x, y),
    "%" : lambda x, y: operaciones.modulo(x, y),
    "/" : lambda x, y: operaciones.division(x, y),
    "*" : lambda x, y: x * y,
    "-" : lambda x, y: x - y,
    "+" : lambda x, y: x + y
} 

SIMBOLOS = {"+", "-", "*", "/", "%", "$", "//", "**"}

OPERADORES_SIMPLES = {
    "+" : "SUMA",
    "-" : "RESTA",
    "*" : "MULTI",
    "/" : "DIV",
    "$" : "RAIZ_ENESIMA",
    "%" : "MOD",
    "[" : "LIS_IZQ",
    "]" : "LIS_DER"
}

OPERADORES_DOBLES = {
    "**" : "POTENCIA",
    "//" : "DIV_ENTERA",
}


