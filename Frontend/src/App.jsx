// React Hooks
import { useEffect, useState } from "react";

// Layout Components
import Header from "./components/Header";
import Layout from "./components/Layout";

// Feature Components
import LeftPanel from "./components/LeftPanel";
import RightPanel from "./components/RightPanel";

// Static Data
import problemList from "./data/problemList";
import topics from "./data/topics";


function App() {
  

  // =====================
  // Application State
  // =====================

  const [text, setText] = useState("");
  const [response, setResponse] = useState("");
  const [language, setLanguage] = useState("python");
  const [inputText, setInputText] = useState("");
  const [problem, setProblem] = useState(null);
  const [problemId, setProblemId] = useState(1);
  const [topic, setTopic] = useState("Arrays");

  // Problems available for currently selected topic
  const filteredProblems = problemList.filter(
    (problem) => problem.topic === topic
  );


  // =====================
  // Effects
  // =====================

  // Fetch problem whenever selected problem changes
  useEffect(() => {
    fetch(`http://127.0.0.1:8000/problem/${problemId}`)
      .then((res) => res.json())
      .then((data) => {
        setProblem(data);
      });
  }, [problemId]);


  // =====================
  // API Functions
  // =====================

   // Run code against visible example testcase
  const sendData = () => {
    fetch("http://127.0.0.1:8000/run-example", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
          text,
          language,
          problem_id: problemId
      })
    })
      .then((res) => res.json())
      .then((data) => {
        let output = "";
        output += `Verdict: ${data.verdict}\n\n`;
        if (data.input) {
          output += `Example Input:\n${data.input}\n\n`;
          output += `Expected Output:\n${data.expected}\n\n`;
          output += `Your Output:\n${data.actual}`;
        }
        setResponse(output);
      });
  };

  // Submit code against hidden testcase set
  const submitSolution = () => {
    fetch("http://127.0.0.1:8000/submit", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        text: text,
        language: language,
        problem_id: problemId
      })
    })
      .then((res) => res.json())
      .then((data) => {
        let output = "";
        output += `Verdict: ${data.verdict}\n\n`;
        output += `Passed: ${data.passed}/${data.total}\n\n`;
        if (data.verdict === "Wrong Answer") {
          output += `Failed Input:\n${data.failed_input}\n\n`;
          output += `Expected Output:\n${data.expected_output}\n\n`;
          output += `Your Output:\n${data.actual_output}`;
        }
        setResponse(output);
      });
  };


  // ===========================
  // Conditional Rendering
  // ===========================
  if (!problem) {
    return <h2>Loading...</h2>;
  }


  // ==================================================
  // UI Composition
  // ==================================================
  return (
    <div>
      <Header />
  
      <Layout
        leftPanel={
          <LeftPanel
            topic={topic}
            setTopic={setTopic}
            topics={topics}
            problemList={problemList}
            setProblemId={setProblemId}
            problemId={problemId}
            filteredProblems={filteredProblems}
            problem={problem}
          />
        }
        rightPanel={
          <RightPanel
            language={language}
            setLanguage={setLanguage}
            sendData={sendData}
            submitSolution={submitSolution}
            text={text}
            setText={setText}
            inputText={inputText}
            setInputText={setInputText}
            response={response}
          />
        }
      />
  
    </div>
  );
}

export default App;