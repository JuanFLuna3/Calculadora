# importamos las clases y metodos
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET',"POST"])
def aritmetica():
    if request.method == "POST":
        # valores que recibo de form n1,n2 son pasados
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))
        # realizamos operaciones aritmeticas
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        return render_template('index.html', total_suma=suma,
                                             total_resta=resta,
                                             total_multiplicacion=multiplicacion,
                                             total_division=division )
    return render_template('index.html')



from flask import Flask, render_template, request
from datetime import datetime

@app.route('/Fechas', methods=['GET', 'POST'])
def fechas():
    if request.method == "POST":
        try:
            # Obtener las fechas del formulario
            fecha1_str = request.form.get('fecha1')
            fecha2_str = request.form.get('fecha2')

            # Convertir las fechas de string a objetos datetime
            fecha1 = datetime.strptime(fecha1_str, '%Y-%m-%d')
            fecha2 = datetime.strptime(fecha2_str, '%Y-%m-%d')

            # Calcular la diferencia en días
            diferencia_dias = (fecha1 - fecha2).days
            
            return render_template('fechas.html', diferencia_dias=diferencia_dias)
        except ValueError:
            # En caso de que las fechas no sean válidas
            return render_template('fechas.html', error="Por favor ingresa fechas válidas")
    return render_template('fechas.html')

if __name__ == "__main__":
    app.run(debug=True)
