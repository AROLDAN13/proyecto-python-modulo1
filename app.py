import streamlit as st

col1, col2, col3 = st.sidebar.columns([1, 2, 1])

with col2: st.image("logo.png",width=150)

menu_navegacion = ("Home", "Ejercicio 1", "Ejercicio 2", "Ejercicio 3", "Ejercicio 4")

opcion_seleccionada = st.sidebar.selectbox(
    "Menú de Navegación", 
    menu_navegacion
)

# 1. Lógica del módulo Home
if opcion_seleccionada == "Home":

    st.title("Proyecto Aplicado en Streamlit") 

    st.write("**Desarrollado por:** Alex Enrique Roldan Talledo")
    st.write("**Nombre del módulo:** Módulo 1 – Python Fundamentals")
    st.write("**Año:** 2026")
    
    st.markdown("---")
    
    st.write("**Objetivo del trabajo:**")
    st.write("Desarrollar una aplicación interactiva en Streamlit que integre los conceptos fundamentales aprendidos durante el Módulo 1 del curso, incluyendo variables, estructuras de datos, control de flujo, funciones, programación funcional y programación orientada a objetos (POO).") #
    
    st.write("**Tecnologías utilizadas:**")
    st.write("- Python")
    st.write("- Streamlit")

# 2. Lógica del módulo Ejercicio 1
elif opcion_seleccionada == "Ejercicio 1":
    st.title("Ejercicio 1 – Variables y Condicionales")
    st.write("Determinar si el gasto está dentro o fuera del presupuesto.") #
    st.markdown("---")

    presupuesto = st.number_input("Ingresa tu presupuesto:", min_value=0.0, step=10.0)
    gasto = st.number_input("Ingresa tu gasto:", min_value=0.0, step=10.0)

    if st.button("Evaluar"):
        
        if gasto <= presupuesto:
            st.success("¡Excelente! El gasto está dentro de tu presupuesto.")
        else:
            st.warning("¡Cuidado! Has excedido tu presupuesto.")

        diferencia = round(abs(presupuesto - gasto),2)
        st.write(f"La diferencia entre tu presupuesto y tu gasto es: **{diferencia}**")

# 3. Lógica del módulo Ejercicio 2
elif opcion_seleccionada == "Ejercicio 2":
    st.title("Ejercicio 2 – Listas y Diccionarios")
    st.write("Registro y evaluación de actividades financieras.")
    st.markdown("---")

    if 'actividades' not in st.session_state:
        st.session_state.actividades = []

    st.subheader("Ingreso de nueva actividad")
    
    nombre = st.text_input("Nombre de la actividad", placeholder="Ejm: Depósito a Plazo Fijo, Compra de Acciones, Fondo Mutuo...")
    tipo = st.selectbox("Tipo de actividad", ["Ahorro Bancario", "Fondo Mutuo", "Inversión en Bolsa", "Criptomonedas", "Bienes Raíces", "Otro"])
    presupuesto = st.number_input("Presupuesto asignado:", min_value=0.0, step=50.0)
    gasto_real = st.number_input("Gasto real:", min_value=0.0, step=50.0)

    if st.button("Agregar actividad"):
        if gasto_real <= presupuesto:
            estado = "✅ Dentro del presupuesto"
        else:
            estado = "❌ Presupuesto excedido"

        nueva_actividad = {
            "nombre": nombre,
            "tipo": tipo,
            "presupuesto": presupuesto,
            "gasto_real": gasto_real,
            "estado": estado
        }
        
        st.session_state.actividades.append(nueva_actividad)
        st.success(f"¡Actividad '{nombre}' agregada con éxito!")

    st.markdown("---")

    if len(st.session_state.actividades) > 0:
        
        st.subheader("Lista de Actividades")
        
        st.dataframe(
            st.session_state.actividades,
            use_container_width=True,
            hide_index=True,
            column_config={
                "nombre": "Nombre de la Actividad",
                "tipo": "Categoría",
                "presupuesto": st.column_config.NumberColumn(
                    "Presupuesto",
                    format="$ %.2f"
                ),
                "gasto_real": st.column_config.NumberColumn(
                    "Gasto Real",
                    format="$ %.2f"
                ),
                "estado": "Estado de la Actividad"
            }
        )
    else:
        st.warning("⚠️ Aún no has registrado ninguna actividad. Ingresa una arriba para comenzar.")

# 4. Lógica del módulo Ejercicio 3
elif opcion_seleccionada == "Ejercicio 3":
    st.title("Ejercicio 3 – Funciones y Programación Funcional")
    st.write("Calculo del retorno esperado de las actividades que se registró en el Ejercicio 2.")
    st.markdown("---")

    # Función de retorno
    def calcular_retorno(actividad, tasa, meses):
        retorno = actividad["presupuesto"] * tasa * meses
        return {
            "Actividad": actividad["nombre"],
            "Categoría": actividad["tipo"],
            "Presupuesto Base": actividad["presupuesto"],
            "Retorno Esperado": retorno
        }

    if 'actividades' not in st.session_state or len(st.session_state.actividades) == 0:
        st.warning("⚠️ No tienes actividades registradas. Ve al **Ejercicio 2** en el menú para agregar algunas.")
    else:
        
        col1, col2 = st.columns(2)
        with col1:
            tasa = st.number_input("Tasa de retorno (Ejm. 0.05 para 5%)", min_value=0.0, max_value=1.0, value=0.05, step=0.01)
        with col2:
            meses = st.number_input("Cantidad de meses", min_value=1, value=12, step=1)

        if st.button("Calcular Retorno de mis Actividades"):
            
            resultados = list(map(lambda act: calcular_retorno(act, tasa, meses), st.session_state.actividades))
            
            st.write("### Resultados del Cálculo")
            
            st.dataframe(
                resultados,
                use_container_width=True,
                hide_index=True,
                column_config={
                    "Presupuesto Base": st.column_config.NumberColumn(format="$ %.2f"),
                    "Retorno Esperado": st.column_config.NumberColumn(format="$ %.2f")
                }
            )

# 5. Lógica del módulo Ejercicio 4
elif opcion_seleccionada == "Ejercicio 4":
    st.title("Ejercicio 4 – Programación Orientada a Objetos (POO)")
    st.write("Modelado de actividades financieras utilizando clases y objetos.")
    st.markdown("---")

    class Actividad:
        def __init__(self, nombre, tipo, presupuesto, gasto_real):
            self.nombre = nombre
            self.tipo = tipo
            self.presupuesto = presupuesto
            self.gasto_real = gasto_real

        def esta_en_presupuesto(self):
            if self.gasto_real <= self.presupuesto:
                return True
            else:
                return False

        def mostrar_info(self):
            return f"**Actividad:** {self.nombre} | **Tipo:** {self.tipo} | **Presupuesto:** \${self.presupuesto:,.2f} | **Gasto Real:** \${self.gasto_real:,.2f}"

    if 'actividades' not in st.session_state or len(st.session_state.actividades) == 0:
        st.warning("⚠️ No hay actividades para analizar. Por favor, registra al menos una en el **Ejercicio 2**.")
    else:
        st.subheader("Evaluación de Actividades")
        
        lista_objetos = []
        for act in st.session_state.actividades:
            nuevo_objeto = Actividad(act["nombre"], act["tipo"], act["presupuesto"], act["gasto_real"])
            lista_objetos.append(nuevo_objeto)

        for obj in lista_objetos:
            st.write(obj.mostrar_info())
            
            if obj.esta_en_presupuesto():
                st.success("Esta actividad se mantuvo dentro del presupuesto.")
            else:
                st.warning("¡Cuidado! El gasto real superó el presupuesto asignado.")