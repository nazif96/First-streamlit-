import streamlit as st 

st.set_page_config(page_icon="😂", page_title="PyApp")

st.title("😁 Ma premiere app super stylée" )

st.markdown(""" Du *markdown* dans l'app? **Rien de plus simple !**
            
            On peut aller à la ligne aussi.:) 
            """
            )

st.markdown(""" 
            > Des couleurs? :orange[orange]
            """)
st.code(""" 
        [[for i in range(5)] for j in range(2)]
        #Du code non-exécutable 
        """,
        language="python")

st.divider()

st.header("Ajoutons du $\LaTeX$")
st.subheader("Identité de Euler*", divider="blue")
st.latex("e^{i \pi} +1 = 0")

st.caption(
    "Lidentité d'Euler est souvent citée comme un exemple de **béauté** mathématique"
)
#Guillaume(tres bon)
fruit = st.selectbox(
    "Fruit",
    ("Fraise", "Pomme", "Banane"),
    index=None,
    placeholder= "Selectionner un fruit"
)

bouton= st.button("Voir les details  du fruit selectionnée")

if bouton :
    st.write(f"t'as la dalle ! graille une **{fruit}** c'est une dinguerie")


colonne_1, colonne_2 = st.columns([0.3, 0.8])

with st.container(border= True):
    with colonne_1:
        st.write("contenu colonne 1")
    

    with colonne_2:
        st.write("contenu colonne 2")


with st.sidebar:
    prénom = st.text_input("😂 Ecris ton prénom")
    reussite = st.checkbox("Tu pense avoir ton année")
    note_pf = st.number_input(
        "Ta note en concurrence & Innovation",
        min_value= 0,
        max_value= 5,
        step=1
    )
    
    epanouissement = st.select_slider(
        "Ton epanouissement en master",
        range(11)
    )
    
tab_1, tab_2, tab_3 =  st.tabs(["info sur l'année", "dataframe", "Graphique"])

if prénom:
    with tab_1:
        if reussite:
            st.balloons()
            st.write(f"bien joué pour ton année")
        else:
            st.snow()
            st.write(f"Raté {prénom}")
            
       
with st.sidebar: 
    with st.expander("On regarde quelques messages ?"):
        st.info(f"Ton epanouissement en Master : {epanouissement}/10",)
        st.error(f" Ta note en Favard: {note_pf}")
        
        
import polars as pl     

@st.cache_data
def import_covid_usa(link:str) -> pl.DataFrame:
    """ """
    return pl.read_csv(link) 

df_covid = import_covid_usa("https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv")


with tab_2:
    st.dataframe(
        df_covid,
        hide_index=True,
        use_container_width=True,
        column_config={
            "data": st.column_config.DateColumn("Date", format="DD/MM/YYYY"),
            "deaths": st.column_config.NumberColumn("MORTS")
            }
    )
    
