import streamlit as st
import pandas as pd
import requests

st.title("Prediksi Risiko Gagal Bayar 🚀")

# Upload file CSV
uploaded_file = st.file_uploader("Upload file CSV", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Preview Data:")
    st.write(df.head())

    # Kirim ke API FastAPI
    api_url = "https://nama-app.railway.app/predict"  # Ganti dengan URL FastAPI kamu
    response = requests.post(api_url, files={"file": uploaded_file.getvalue()})

    if response.status_code == 200:
        # Tampilkan hasil prediksi
        prediksi = pd.DataFrame(response.json())
        st.write("Hasil Prediksi:")
        st.write(prediksi)

        # Download hasil
        csv = prediksi.to_csv(index=False).encode()
        st.download_button("Download Hasil", data=csv, file_name="hasil_prediksi.csv")
    else:
        st.error("Terjadi kesalahan pada API.")
