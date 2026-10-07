import { useState } from "react";

function ChatBox({
  askQuestion,
  answer,
  sources,
  loading
}) {

  const [question, setQuestion] = useState("");


  const submitQuestion = (event) => {

    event.preventDefault();

    if (!question.trim()) return;

    askQuestion(question);

    setQuestion("");
  };


  return (

    <div className="chat-box">

      <h2>
        Ask about your PDF
      </h2>


      <form onSubmit={submitQuestion}>

        <textarea
          value={question}
          onChange={(event) =>
            setQuestion(event.target.value)
          }
          placeholder="Ask something about your study material..."
        />


        <button type="submit">

          {loading
            ? "Thinking..."
            : "Ask AI"
          }

        </button>

      </form>


      {answer && (

        <div className="answer">

          <h3>
            AI Answer
          </h3>

          <p>
            {answer}
          </p>


          {sources.length > 0 && (

            <div className="sources">

              <h4>
                Sources
              </h4>

              {[...new Set(
                sources.map(
                  source => source.page
                )
              )].map(page => (

                <span
                  key={page}
                  className="source"
                >
                  Page {page}
                </span>

              ))}

            </div>

          )}

        </div>

      )}

    </div>
  );
}

export default ChatBox;