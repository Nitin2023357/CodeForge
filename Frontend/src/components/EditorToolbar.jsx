import LanguageSelector from "./LanguageSelector";

function EditorToolbar({
  language,
  setLanguage,
  sendData,
  submitSolution
}) {
  return (
    <div
      style={{
        display: "flex",
        justifyContent: "space-between",
        alignItems: "center",
        marginBottom: "10px"
      }}
    >
      <LanguageSelector
        language={language}
        setLanguage={setLanguage}
      />

      <div>
        <button onClick={sendData}>
          Run Code
        </button>

        <button
          onClick={submitSolution}
          style={{
            marginLeft: "10px"
          }}
        >
          Submit
        </button>
      </div>
    </div>
  );
}

export default EditorToolbar;