function InputBox({ inputText, setInputText }) {
  return (
    <textarea
      value={inputText}
      onChange={(e) => setInputText(e.target.value)}
    />
  );
}

export default InputBox;