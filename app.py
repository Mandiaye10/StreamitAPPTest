import streamlit as st

def main():
    st.title("🧮 Calculatrice Simple")
    
    # Saisie des nombres
    num1 = st.number_input("Entrez le premier nombre", value=0.0, step=0.1)
    num2 = st.number_input("Entrez le deuxième nombre", value=0.0, step=0.1)
    
    # Sélection de l'opération
    operation = st.selectbox("Choisissez une opération", ["Addition", "Soustraction", "Multiplication", "Division"])
    
    # Calcul et affichage du résultat
    if st.button("Calculer"):
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Soustraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("❌ Erreur : Division par zéro non autorisée")
                return
        
        st.success(f"✅ Résultat : {result}")

if __name__ == "__main__":
    main()
