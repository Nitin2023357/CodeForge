import Editor from "@monaco-editor/react";

function CodeEditor({ text, setText, language }) {
  return (
    <Editor
      height="400px"
      language={language}
      value={text}
      onChange={(value) => setText(value || "")}
      theme="vs-dark"
    />
  );
}

export default CodeEditor;