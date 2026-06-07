function TopicSelector({
  topic,
  setTopic,
  topics,
  problemList,
  setProblemId
}) {
  return (
    <select
      value={topic}
      onChange={(e) => {
        const selectedTopic = e.target.value;

        setTopic(selectedTopic);

        const firstProblem = problemList.find(
          (problem) => problem.topic === selectedTopic
        );

        setProblemId(firstProblem.id);
      }}
    >
      {topics.map((t) => (
        <option
          key={t}
          value={t}
        >
          {t}
        </option>
      ))}
    </select>
  );
}

export default TopicSelector;