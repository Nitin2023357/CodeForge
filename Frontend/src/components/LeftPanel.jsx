import TopicSelector from "./TopicSelector";
import ProblemSelector from "./ProblemSelector";
import ProblemPanel from "./ProblemPanel";

function LeftPanel({
  topic,
  setTopic,
  topics,
  problemList,
  setProblemId,
  problemId,
  filteredProblems,
  problem
}) {
  return (
    <div
      style={{
        flex: 1.2,
        maxHeight: "85vh",
        overflowY: "auto",
        borderRight: "1px solid #333"
      }}
    >
      <div
        style={{
          display: "flex",
          justifyContent: "flex-end",
          gap: "10px",
          padding: "10px",
          borderBottom: "1px solid #333"
        }}
      >
        <TopicSelector
          topic={topic}
          setTopic={setTopic}
          topics={topics}
          problemList={problemList}
          setProblemId={setProblemId}
        />

        <ProblemSelector
          problemId={problemId}
          setProblemId={setProblemId}
          filteredProblems={filteredProblems}
        />
      </div>

      <ProblemPanel problem={problem} />
    </div>
  );
}

export default LeftPanel;