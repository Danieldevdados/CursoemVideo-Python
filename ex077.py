palavras =  ('aprender', 'progamar', 'linguaguem', 'python',
             'curso', 'gratis', 'estudar', 'praticar',
             'trabalhar', 'mercado', 'progamador', 'futuro')
for p in palavras:
    print(f' \n Na palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end='')