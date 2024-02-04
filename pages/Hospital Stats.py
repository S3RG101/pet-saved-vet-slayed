from streamlit_apexjs import st_apexcharts

st.title('Hospital Stats')
st.header('1 Month Antimicrobial Resistance')

options2 = {
    "chart": {
        "id": "lol2",
        "toolbar": {
            "show": False
        }
    },

    "xaxis": {
        "categories":
            ['MRSA', 'Campylobacter spp.', 'Salmonella spp.', 'Staphylococcus spp.']
    }
    ,
    "legend": {
        "show": True,
        "position": "bottom",
    }
}

series2 = [{
"name": 'example',
"data": [15, 17, 23, 44]
}]

st_apexcharts(options2, series2, 'bar', '200%')
