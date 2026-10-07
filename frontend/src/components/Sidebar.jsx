function Sidebar({
  activeFeature,
  setActiveFeature,
  generateFeature
}) {

  return (

    <aside className="sidebar">

      <button
        className={
          activeFeature === "ask"
            ? "active"
            : ""
        }
        onClick={() =>
          setActiveFeature("ask")
        }
      >
        💬 Ask AI
      </button>


      <button
        className={
          activeFeature === "summary"
            ? "active"
            : ""
        }
        onClick={() =>
          setActiveFeature("summary")
        }
      >
        📝 Summary
      </button>


      <button
        className={
          activeFeature === "quiz"
            ? "active"
            : ""
        }
        onClick={() =>
          setActiveFeature("quiz")
        }
      >
        ❓ Quiz
      </button>


      <button
        className={
          activeFeature === "flashcards"
            ? "active"
            : ""
        }
        onClick={() =>
          setActiveFeature("flashcards")
        }
      >
         Flashcards
      </button>

    </aside>
  );
}

export default Sidebar;