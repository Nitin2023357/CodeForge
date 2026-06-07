function OutputBox({ response }) {
  return (
    <div
      style={{
        backgroundColor: "#1e1e1e",
        padding: "10px",
        borderRadius: "5px",
        marginTop: "10px",
        whiteSpace: "pre-wrap",
        overflowWrap: "break-word",
        wordBreak: "break-word"
      }}
    >
      {response}
    </div>
  );
}

export default OutputBox;