function ProblemPanel({ problem }) {
  return (
    <div
      style={{
        textAlign: "left",
        padding: "20px",
        maxHeight: "80vh",
        overflowY: "auto"
      }}
    >
      <h2>
        Problem {problem.id}. {problem.title}
      </h2>

      <p>
        <strong>Difficulty:</strong> {problem.difficulty}
      </p>

      <hr />

      <h3>Description</h3>

      <p
        style={{
          whiteSpace: "pre-line",
          lineHeight: "1.6"
        }}
      >
        {problem.statement}
      </p>

      <hr />

      <h3>Examples</h3>

      {problem.examples.map((example, index) => (
        <div
          key={index}
          style={{
            marginBottom: "25px"
          }}
        >
          <h4>Example {index + 1}</h4>

          <p>
            <strong>Input:</strong>
          </p>

          <pre
            style={{
              backgroundColor: "#1e1e1e",
              padding: "10px",
              borderRadius: "5px",
              overflowX: "auto"
            }}
          >
            {example.input}
          </pre>

          <p>
            <strong>Output:</strong>
          </p>

          <pre
            style={{
              backgroundColor: "#1e1e1e",
              padding: "10px",
              borderRadius: "5px",
              overflowX: "auto"
            }}
          >
            {example.output}
          </pre>

          <p>
            <strong>Explanation:</strong>
          </p>

          <pre
            style={{
              backgroundColor: "#1e1e1e",
              padding: "10px",
              borderRadius: "5px",
              overflowX: "auto"
            }}
          >
            {example.explanation}
          </pre>
        </div>
      ))}

      <hr />

      <h3>Constraints</h3>

      <ul
        style={{
          paddingLeft: "20px"
        }}
      >
        {problem.constraints.map((constraint, index) => (
          <li
            key={index}
            style={{
              marginBottom: "8px"
            }}
          >
            {constraint}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProblemPanel;