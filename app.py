import streamlit as st
import pandas as pd
from Bio import SeqIO
from Bio.SeqUtils.ProtParam import ProteinAnalysis

st.set_page_config(page_title="Protein Physicochemical Analysis Toolkit")

st.title("Protein Physicochemical Analysis Toolkit")

st.write("Upload a FASTA file for automated protein physicochemical analysis.")

uploaded_file = st.file_uploader(
    "Upload FASTA File",
    type=["fasta", "fa", "txt"]
)

if uploaded_file:

    results = []

    sequences = SeqIO.parse(uploaded_file, "fasta")

    for record in sequences:

        seq = str(record.seq)

        analysed_seq = ProteinAnalysis(seq)

        mw = analysed_seq.molecular_weight()
        pi = analysed_seq.isoelectric_point()
        gravy = analysed_seq.gravy()
        instability = analysed_seq.instability_index()

        results.append({
            "Protein ID": record.id,
            "Molecular Weight": round(mw, 2),
            "Isoelectric Point": round(pi, 2),
            "GRAVY": round(gravy, 3),
            "Instability Index": round(instability, 2)
        })

    df = pd.DataFrame(results)

    st.subheader("Analysis Results")

    st.dataframe(df)

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Results CSV",
        data=csv,
        file_name="physicochemical_results.csv",
        mime="text/csv"
    )
