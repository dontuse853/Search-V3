import streamlit as st

st.set_page_config(page_title="Custom Search", page_icon="🔍", layout="centered")

# Chrome sends searches to: https://<your-app>.streamlit.app/?q=<search terms>
query = st.query_params.get("q", "")

st.title("🔍 Custom Search")

# Search box (prefilled with the query from the URL)
new_query = st.text_input("Search", value=query, placeholder="Type something...")

# Keep the URL in sync if the user searches again from the page
if new_query != query:
    st.query_params["q"] = new_query
    st.rerun()

if query:
    st.subheader(f"Results for: {query}")

    # ---- Replace this section with your own search logic ----
    st.info("Hook up your own data source, API, or model here.")
    st.write(f"You searched for **{query}**.")
    # ----------------------------------------------------------
else:
    st.write("Enter a search term above, or search from Chrome's address bar.")
