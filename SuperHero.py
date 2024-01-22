import streamlit as st
import requests

# st.title('SuperHero')
st.write("""# Hello👋 This program gives you stats of a superhero.""")
name = st.text_input(label='Enter name of a superhero!')

if st.button('Get Stats'):
    api = f'https://superheroapi.com/api/Your-Access-key/search/{name}'
    response = requests.get(api)
    
    if response.status_code == 200:
        superhero_data = response.json()['results'][0]
        
        # st.write(superhero_data)
        st.write(f"### Showing stats for {superhero_data['name']}")
        st.image(superhero_data['image']['url'] , caption=superhero_data['name'])

        st.write('### Biography💪')
        st.write(f"**Full Name:** {superhero_data['biography']['full-name']}")
        st.write(f"**First Appearance:** {superhero_data['biography']['first-appearance']}")
        st.write(f"**Place of Birth:** {superhero_data['biography']['place-of-birth']}")

        st.write('### Appearance 🥰')
        st.write(f"**Gender:** {superhero_data['appearance']['gender']}")
        st.write(f"**Race:** {superhero_data['appearance']['race']}")
        st.write(f"**Height:** {superhero_data['appearance']['height']}")
        st.write(f"**Weight:** {superhero_data['appearance']['weight']}")

        st.write('### Work ⚒️')
        st.write(f"**Occupation:** {superhero_data['work']['occupation']}")
        st.write(f"**Base:** {superhero_data['work']['base']}")
    else:
        st.write(f'No superhero named {name}')

