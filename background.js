// Background service worker (Manifest V3).
// The default search engine override itself is declared in manifest.json
// under "chrome_settings_overrides.search_provider", so Chrome applies it
// automatically. This worker just handles lifecycle events.

chrome.runtime.onInstalled.addListener((details) => {
  if (details.reason === "install") {
    console.log("Custom Streamlit Search installed. Default search engine set.");
  } else if (details.reason === "update") {
    console.log("Custom Streamlit Search updated to", chrome.runtime.getManifest().version);
  }
});
