import InputBox from "./InputBox";
import OutputBox from "./OutputBox";

function BottomPanel({
  inputText,
  setInputText,
  response
}) {
  return (
    <div
      style={{
        marginTop: "10px",
        border: "1px solid #333",
        borderRadius: "8px",
        overflow: "hidden",
        display: "flex",
        flexDirection: "column",
        flex: 1,
        minHeight: 0
      }}
    >
      {/* Tabs */}

      <div
        style={{
          display: "flex",
          borderBottom: "1px solid #333"
        }}
      >
        <div
          style={{
            padding: "12px",
            fontWeight: "bold"
          }}
        >
          Testcase
        </div>

        <div
          style={{
            padding: "12px",
            fontWeight: "bold"
          }}
        >
          Result
        </div>
      </div>

      {/* Content */}

      <div
        style={{
          flex: 1,
          overflowY: "auto",
          padding: "10px"
        }}
      >
        <InputBox
          inputText={inputText}
          setInputText={setInputText}
        />

        <OutputBox response={response} />
      </div>
    </div>
  );
}

export default BottomPanel;