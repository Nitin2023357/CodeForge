function ProblemSelector({
  problemId,
  setProblemId,
  filteredProblems
}) {
  return (
    <select
      value={problemId}
      onChange={(e) =>
        setProblemId(Number(e.target.value))
      }
    >
      {filteredProblems.map((problem) => (
        <option
          key={problem.id}
          value={problem.id}
        >
          {problem.title}
        </option>
      ))}
    </select>
  );
}

export default ProblemSelector;