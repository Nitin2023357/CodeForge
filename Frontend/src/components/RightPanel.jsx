import EditorToolbar from "./EditorToolbar";
import CodeEditor from "./CodeEditor";
import BottomPanel from "./BottomPanel";

function RightPanel({
  language,
  setLanguage,
  sendData,
  submitSolution,
  text,
  setText,
  inputText,
  setInputText,
  response
}) {
  return (
    <div
      style={{
        flex: 1,
        height: "85vh",
        display: "flex",
        flexDirection: "column"
      }}
    >
      <EditorToolbar
        language={language}
        setLanguage={setLanguage}
        sendData={sendData}
        submitSolution={submitSolution}
      />

      <div
        style={{
          height: "55%"
        }}
      >
        <CodeEditor
          text={text}
          setText={setText}
          language={language}
        />
      </div>

      <BottomPanel
        inputText={inputText}
        setInputText={setInputText}
        response={response}
      />
    </div>
  );
}

export default RightPanel;