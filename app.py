import streamlit as st
from PIL import Image
import imagenes
import style
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title=" M y R Pintores ",page_icon="👨🎨",layout="wide")
email_contac = ("matiasandresrey@gmail.com")
def css_load(css_file):
   with open(css_file) as file:
      st.markdown(f"<style>{file.read()}</style>",unsafe_allow_html=True)
css_load("style/main.css")


with st.container():
   
    st.header(" MYR: Transformando espacios, inspirando hogares. Tu remodelación de interiores de confianza. ")
    st.title("Renova tu hogar ,con ayuda de profeccionales ") 
    image_colum, text_colum= st.columns((1,2))
with image_colum:
    image=Image.open("imagenes/myr.jpeg")
    st.image(image, use_column_width=True)
    st.write("Nos dedicamos a la remodelacion de interior ,con multiples diseños para diferentes estilos , cocina , baño , living")
    st.write("[sabermas >](https://reypintores.com)" )
    

with st.container():
    st.write("---")
    text_colum, animation_colum, = st.columns(2)
    with text_colum:
        st.header(" Nostoros somos  📜")
        st.write(
            """
                 
                 MYR - Transformando espacios, inspirando hogares ,En MYR, nos apasiona convertir tus espacios en lugares que reflejen tu estilo y personalidad. Somos un equipo de expertos en remodelación de interiores dedicados a brindarte un servicio profesional y de alta calidad que superará tus expectativas.

Nuestro objetivo es transformar cada rincón de tu hogar en un oasis acogedor y funcional. Ya sea que desees renovar una habitación específica o darle una nueva vida a toda tu casa, estamos aquí para hacerlo realidad.

Nuestros diseñadores y especialistas trabajan mano a mano contigo para entender tus necesidades, gustos y presupuesto. A partir de ahí, creamos un plan personalizado que aproveche al máximo el potencial de tus espacios, utilizando materiales y acabados de primera calidad.

La atención meticulosa al detalle y el enfoque en la excelencia son nuestra firma. Cada proyecto es llevado a cabo con pasión y profesionalismo, asegurando que cada aspecto de la remodelación se realice con precisión y dedicación.

En MYR, creemos que tu hogar debe ser tu santuario, un lugar donde te sientas completamente a gusto y feliz. Nuestra misión es llevar a cabo tus sueños de diseño, convirtiendo tus visiones en realidad y creando interiores que te inspiren cada día.

Confía en nosotros para transformar tu hogar en un espacio impresionante y funcional que dejará una impresión duradera en ti y en tus seres queridos. Descubre la magia de la remodelación de interiores con MYR y comienza a crear el hogar que siempre has deseado"
""")
    st.write("[sabermas >](https://reypintores.com)" )
with animation_colum:
    st.empty()


#SERVICIOS 
with st.container():
 st.write("---")
 st.header("remodelaciones 👨🎨")
 st.write("##")


image_colum, text_colum= st.columns((1,2))
with image_colum:
    image=Image.open("imagenes/myr.jpeg")
    st.image(image, use_column_width=True)
with image_colum:
    image=Image.open("imagenes/presentacion.jpeg")
    st.image(image, use_column_width=True)
image_colum, text_colum= st.columns((1,2))
with image_colum:
    image=Image.open("imagenes/presentacion.jpeg")
    st.image(image, use_column_width=True)
with text_colum:
   st.subheader("remodelacion y diseño de interiores")
   st.write(
      """
            Juntos, haremos de tu casa un santuario acogedor, donde la magia del diseño se fusiona con la excelencia y la pasión por los detalles
           ¡Crea recuerdos inolvidables en un entorno que te inspire y enamore cada día! Contrata a MYR y da vida a tus sueños de hogar 
            """
            )
   st.write("[sabermas >](https://reypintores.com/services/)" )
with st.container():
    st.write("---")
    st.write("##")
    image_colum, text_colum= st.columns((1,2))
    with image_colum:
       image=Image.open("imagenes/diseño.jpeg")
       st.image(image, use_column_width=True)
       st.write(
          """
          si quiere mejorar su hogar no dude en consultarnos , ofrecemos garantia  de trabajo profesional 
          """ )
       st.write("[sabermas >](https://reypintores.com/services/)" )
    with image_colum:
       image=Image.open("imagenes/trabajo2a.jpeg")
       st.image(image, use_column_width=True)
    with image_colum:
       image=Image.open("imagenes/trabajo2b.jpeg")
       st.image(image, use_column_width=True)
       st.write(
          """
"MYR  - Tu Hogar, Tu Inspiración. Transformando Espacios, Creando Sueños.
""")
with st.container():
   st.write("---")
   st.write ("""
             *Cotactanos a traves de whatsapp 📱 : 11 3653-6304
              *buscanos en nuestras redes sociales :
               instagram: @mtupintor (https://www.instagram.com/mtupintor/?hl=es-la)
               facebook: Rey Pintores (https://www.facebook.com/zapas.rey)

             """)
   st.write("##")
   contac_from= f"""
   <form action="https://formsubmit.co/{email_contac}" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" Name="name" placeholder="Tu nombre" required>
     <input type="email" Name="email"placeholder="Tu email" required>
     <textarea type="mensaje " Name="mensaje"placeholder= "Deja tu mensaje "required></textarea>
     <button type="submit">enviar</button>
</form>
"""

left_column,right_cloumn=st.columns(2)
with left_column:
   st.markdown(contac_from,unsafe_allow_html=True)
with right_cloumn:
   st.empty()
