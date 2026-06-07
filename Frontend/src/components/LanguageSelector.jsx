function LanguageSelector({
  language,
  setLanguage
}) {
  return (
    <div>
      <label>Language: </label>

      <select
        value={language}
        onChange={(e) =>
          setLanguage(e.target.value)
        }
      >
        <option value="python">
          Python
        </option>
      
        <option value="cpp">
          C++
        </option>
      </select>
    </div>
  );
}

export default LanguageSelector;