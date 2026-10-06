import './App.css'

function App() {
  function handleSubmit(event) {
    event.preventDefault();
    console.log("Form submitted");
  }

  return (
    <main className="app">
      <header className="site-header">
        <div className="brand-mark"></div>

        <div>
          <p className="brand-name">Highlight Creator</p>
          <p className="description">Soccer highlights, automatically</p>
        </div>
      </header>

      <section className="creator-section">
        <p className="eyebrow"></p>

        <h1>Paste a match. Find the moments.</h1>

        <p className="intro">
          Enter a public soccer video URL and we’ll find the most exciting
          moments from the match.
        </p>

        <form className="url-form" onSubmit={handleSubmit}>
          {/* htmlFor connects this label to the input with the matching id. */}
          <label htmlFor="video-url">Match video URL</label>

          <div className="form-row">
            <input
              id="video-url"
              name="videoUrl"
              type="url"
              placeholder="https://youtube.com/watch?v=..."
              required
            />

            <button type="submit">Create highlights</button>
          </div>

          <p className="form-help">
            Use a public video URL that the processing service can access.
          </p>
        </form>

        <div className="steps">
          <article className="step">
            <span>01</span>
            <h2>Submit</h2>
            <p>Paste the URL of a soccer match.</p>
          </article>

          <article className="step">
            <span>02</span>
            <h2>Process</h2>
            <p>The backend analyzes the match commentary.</p>
          </article>

          <article className="step">
            <span>03</span>
            <h2>Review</h2>
            <p>Preview the detected highlight moments.</p>
          </article>
        </div>
      </section>

      <footer className="footer">
      </footer>
    </main>
  );
}

export default App;