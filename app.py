import streamlit as st
from langgraph_workflow import run_pipeline  # Import your pipeline function

st.title("Agentic Workflow Demo")

query = st.text_input("Enter your query:")
if st.button("Run Workflow"):
    if query:
        with st.spinner("Running agentic workflow..."):
            result = run_pipeline(query)
            st.success("Done!")
            st.markdown("### Output:")
            st.write(result)
    else:
        st.warning("Please enter a query.")
    
